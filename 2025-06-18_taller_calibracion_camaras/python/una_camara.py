import cv2
import numpy as np
import glob
import os

# === CONFIGURACIÓN ===
chessboard_size = (9, 6)
square_size = 1.0  # Unidad arbitraria
image_folder = 'images/single/'
save_path = './calibration_output/single_camera_params.npz'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# === Preparar puntos 3D ===
objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

objpoints = []
imgpoints = []
img_shape = None

# === Leer imágenes con varias extensiones ===
extensions = ['*.jpg', '*.jpeg', '*.png']
images = []
for ext in extensions:
    images.extend(glob.glob(os.path.join(image_folder, ext)))

print(f'🔍 Imágenes encontradas: {len(images)}')
if len(images) == 0:
    print("❌ No se encontraron imágenes en la carpeta:", image_folder)
    exit()

# === Procesar imágenes ===
for fname in images:
    img = cv2.imread(fname)
    if img is None:
        print(f"⚠️ No se pudo leer {fname}")
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
    if ret:
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                                    (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001))
        objpoints.append(objp)
        imgpoints.append(corners2)

        if img_shape is None:
            img_shape = gray.shape[::-1]

        cv2.drawChessboardCorners(img, chessboard_size, corners2, ret)
        cv2.imshow('Esquinas detectadas', img)
        cv2.waitKey(100)
    else:
        print(f"🔸 No se detectaron esquinas en: {fname}")

cv2.destroyAllWindows()

# === Validación mínima ===
if len(objpoints) == 0 or len(imgpoints) == 0:
    print("❌ No se detectaron esquinas válidas en ninguna imagen. Revisa las fotos y el patrón.")
    exit()

# === Calibración ===
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
    objpoints, imgpoints, img_shape, None, None)

print("\n✅ Calibración exitosa")
print("📷 Matriz de cámara:\n", mtx)
print("🎯 Distorsión:\n", dist.ravel())

# === Guardar parámetros ===
np.savez(save_path, camera_matrix=mtx, dist_coeffs=dist)
print(f"💾 Parámetros guardados en: {save_path}")

# === Guardar imagen corregida de ejemplo ===
img = cv2.imread(images[0])
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
undistorted = cv2.undistort(img, mtx, dist, None, newcameramtx)
cv2.imwrite('./calibration_output/calibrated_image.jpg', undistorted)
print("🖼️ Imagen corregida guardada como 'calibrated_image.jpg'")
