import cv2
import numpy as np
import glob
import os

# === CONFIGURACIÓN ===
chessboard_size = (9, 6)
square_size = 1.0
left_folder = './images/stereo/left/'
right_folder = './images/stereo/right/'
save_path = './calibration_output/stereo_params.npz'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# === Preparar patrón 3D (coordenadas del mundo) ===
objp = np.zeros((chessboard_size[0]*chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)
objp *= square_size

objpoints = []
imgpoints_left = []
imgpoints_right = []

# === Leer imágenes con soporte para varias extensiones ===
left_images = []
right_images = []
for ext in ['*.jpg', '*.jpeg', '*.png']:
    left_images.extend(glob.glob(os.path.join(left_folder, ext)))
    right_images.extend(glob.glob(os.path.join(right_folder, ext)))

left_images.sort()
right_images.sort()

print(f"📷 Izquierda: {len(left_images)} imágenes")
print(f"📷 Derecha:   {len(right_images)} imágenes")

assert len(left_images) == len(right_images), "❌ Cantidad desigual de imágenes izquierda/derecha"

img_shape = None

# === Detección de esquinas ===
for imgL_path, imgR_path in zip(left_images, right_images):
    imgL = cv2.imread(imgL_path)
    imgR = cv2.imread(imgR_path)

    if imgL is None or imgR is None:
        print(f"⚠️ No se pudo leer {imgL_path} o {imgR_path}")
        continue

    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    retL, cornersL = cv2.findChessboardCorners(grayL, chessboard_size, None)
    retR, cornersR = cv2.findChessboardCorners(grayR, chessboard_size, None)

    if retL and retR:
        cornersL = cv2.cornerSubPix(grayL, cornersL, (11, 11), (-1, -1),
                                    (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001))
        cornersR = cv2.cornerSubPix(grayR, cornersR, (11, 11), (-1, -1),
                                    (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001))

        objpoints.append(objp)
        imgpoints_left.append(cornersL)
        imgpoints_right.append(cornersR)

        if img_shape is None:
            img_shape = grayL.shape[::-1]

        # Visualización opcional
        cv2.drawChessboardCorners(imgL, chessboard_size, cornersL, retL)
        cv2.drawChessboardCorners(imgR, chessboard_size, cornersR, retR)
        cv2.imshow("Left", imgL)
        cv2.imshow("Right", imgR)
        cv2.waitKey(300)
    else:
        print(f"🔸 No se detectaron esquinas en:\n - {imgL_path}\n - {imgR_path}")

cv2.destroyAllWindows()

print(f"\n✅ Imágenes válidas para calibración estéreo: {len(objpoints)}")

# === Validación previa a la calibración ===
if len(objpoints) == 0:
    print("❌ No se encontraron pares válidos de esquinas para calibrar.")
    exit()

# === Calibración individual ===
_, mtxL, distL, _, _ = cv2.calibrateCamera(objpoints, imgpoints_left, img_shape, None, None)
_, mtxR, distR, _, _ = cv2.calibrateCamera(objpoints, imgpoints_right, img_shape, None, None)

# === Calibración estéreo ===
flags = cv2.CALIB_FIX_INTRINSIC
criteria = (cv2.TermCriteria_EPS + cv2.TermCriteria_MAX_ITER, 30, 0.001)

_, _, _, _, _, R, T, E, F = cv2.stereoCalibrate(
    objpoints, imgpoints_left, imgpoints_right,
    mtxL, distL, mtxR, distR, img_shape,
    criteria=criteria, flags=flags
)

print("\n=== 📌 RESULTADOS ESTÉREO ===")
print("🌀 Matriz de rotación R:\n", R)
print("📍 Vector de traslación T:\n", T)

# === Rectificación estéreo ===
R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(
    mtxL, distL, mtxR, distR, img_shape, R, T)

# === Guardar parámetros ===
np.savez(save_path,
         mtxL=mtxL, distL=distL,
         mtxR=mtxR, distR=distR,
         R=R, T=T, R1=R1, R2=R2, P1=P1, P2=P2, Q=Q)

print(f"\n💾 Parámetros estéreo guardados en: {save_path}")
