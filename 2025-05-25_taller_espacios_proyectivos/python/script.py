import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button
import time

class CamaraVirtual:
    """
    Clase que simula una cámara virtual con proyecciones ortográficas y perspectivas
    """
    
    def __init__(self):
        self.posicion = np.array([0, 0, 5])  # Posición de la cámara en el mundo
        self.target = np.array([0, 0, 0])    # Punto al que mira la cámara
        self.up = np.array([0, 1, 0])        # Vector "arriba" de la cámara
        
        # Parámetros para proyección perspectiva
        self.fov = 60  # Field of view en grados
        self.aspect_ratio = 1.0
        self.near = 0.1
        self.far = 100.0
        
        # Parámetros para proyección ortográfica
        self.left = -3
        self.right = 3
        self.bottom = -3
        self.top = 3
        
    def matriz_vista(self):
        """
        Calcula la matriz de vista (view matrix) que transforma coordenadas del mundo
        al espacio de la cámara
        """
        # Vector dirección de la cámara (mirando hacia el target)
        forward = (self.target - self.posicion)
        forward = forward / np.linalg.norm(forward)
        
        # Vector derecha (cross product de forward y up)
        right = np.cross(forward, self.up)
        right = right / np.linalg.norm(right)
        
        # Vector arriba recalculado
        up = np.cross(right, forward)
        
        # Matriz de rotación
        R = np.array([
            [right[0], right[1], right[2], 0],
            [up[0], up[1], up[2], 0],
            [-forward[0], -forward[1], -forward[2], 0],
            [0, 0, 0, 1]
        ])
        
        # Matriz de traslación
        T = np.array([
            [1, 0, 0, -self.posicion[0]],
            [0, 1, 0, -self.posicion[1]],
            [0, 0, 1, -self.posicion[2]],
            [0, 0, 0, 1]
        ])
        
        return R @ T
    
    def matriz_proyeccion_perspectiva(self):
        """
        Calcula la matriz de proyección perspectiva
        """
        fov_rad = np.radians(self.fov)
        f = 1.0 / np.tan(fov_rad / 2.0)
        
        return np.array([
            [f / self.aspect_ratio, 0, 0, 0],
            [0, f, 0, 0],
            [0, 0, (self.far + self.near) / (self.near - self.far), 
             (2 * self.far * self.near) / (self.near - self.far)],
            [0, 0, -1, 0]
        ])
    
    def matriz_proyeccion_ortografica(self):
        """
        Calcula la matriz de proyección ortográfica
        """
        return np.array([
            [2/(self.right - self.left), 0, 0, -(self.right + self.left)/(self.right - self.left)],
            [0, 2/(self.top - self.bottom), 0, -(self.top + self.bottom)/(self.top - self.bottom)],
            [0, 0, -2/(self.far - self.near), -(self.far + self.near)/(self.far - self.near)],
            [0, 0, 0, 1]
        ])
    
    def proyectar_puntos(self, puntos, tipo_proyeccion='perspectiva'):
        """
        Proyecta puntos 3D a coordenadas 2D usando la matriz especificada
        
        Args:
            puntos: array de puntos 3D (3xN)
            tipo_proyeccion: 'perspectiva' o 'ortografica'
        
        Returns:
            puntos_2d: coordenadas 2D proyectadas
        """
        # Convertir a coordenadas homogéneas
        puntos_hom = np.vstack([puntos, np.ones(puntos.shape[1])])
        
        # Aplicar matriz de vista
        vista = self.matriz_vista()
        puntos_vista = vista @ puntos_hom
        
        # Aplicar matriz de proyección
        if tipo_proyeccion == 'perspectiva':
            proj_matrix = self.matriz_proyeccion_perspectiva()
        else:
            proj_matrix = self.matriz_proyeccion_ortografica()
        
        puntos_proj = proj_matrix @ puntos_vista
        
        # División de perspectiva (normalización)
        if tipo_proyeccion == 'perspectiva':
            # Evitar división por cero
            w = puntos_proj[3, :]
            w[w == 0] = 1e-10
            puntos_proj = puntos_proj / w
        
        return puntos_proj[:2, :]

def generar_escena_3d():
    """
    Genera una escena 3D con varios objetos a diferentes distancias
    """
    # Cubo en el origen
    cubo = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # cara trasera
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]       # cara frontal
    ]).T
    
    # Pirámide más alejada
    piramide = np.array([
        [-1, -1, -3], [1, -1, -3], [1, 1, -3], [-1, 1, -3],  # base
        [0, 0, -1]  # punta
    ]).T
    
    # Esfera cercana (simulada con puntos)
    theta = np.linspace(0, 2*np.pi, 20)
    phi = np.linspace(0, np.pi, 15)
    THETA, PHI = np.meshgrid(theta, phi)
    X = 0.5 * np.sin(PHI) * np.cos(THETA) + 2
    Y = 0.5 * np.sin(PHI) * np.sin(THETA)
    Z = 0.5 * np.cos(PHI) + 2
    esfera = np.vstack([X.flatten(), Y.flatten(), Z.flatten()])
    
    return cubo, piramide, esfera

class VisualizadorProyecciones:
    """
    Clase principal para visualizar las diferentes proyecciones
    """
    
    def __init__(self):
        self.camara = CamaraVirtual()
        self.cubo, self.piramide, self.esfera = generar_escena_3d()
        self.tipo_proyeccion = 'perspectiva'
        
        # Configurar la figura
        self.fig = plt.figure(figsize=(15, 10))
        self.ax_3d = self.fig.add_subplot(221, projection='3d')
        self.ax_2d_persp = self.fig.add_subplot(222)
        self.ax_2d_orto = self.fig.add_subplot(223)
        self.ax_params = self.fig.add_subplot(224)
        
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        """Configura sliders y botones para la interfaz interactiva"""
        # Área para sliders
        plt.subplots_adjust(bottom=0.25)
        
        # Slider para FOV
        ax_fov = plt.axes([0.1, 0.15, 0.3, 0.03])
        self.slider_fov = Slider(ax_fov, 'FOV', 30, 120, valinit=self.camara.fov)
        self.slider_fov.on_changed(self.actualizar_fov)
        
        # Slider para distancia de cámara
        ax_dist = plt.axes([0.1, 0.1, 0.3, 0.03])
        self.slider_dist = Slider(ax_dist, 'Distancia', 1, 10, valinit=5)
        self.slider_dist.on_changed(self.actualizar_distancia)
        
        # Botón para cambiar tipo de proyección
        ax_btn = plt.axes([0.55, 0.1, 0.15, 0.06])
        self.btn_proyeccion = Button(ax_btn, 'Cambiar\nProyección')
        self.btn_proyeccion.on_clicked(self.cambiar_proyeccion)
        
        # Botón para animar
        ax_btn_anim = plt.axes([0.75, 0.1, 0.15, 0.06])
        self.btn_animar = Button(ax_btn_anim, 'Animar\nCámara')
        self.btn_animar.on_clicked(self.iniciar_animacion)
        
    def actualizar_fov(self, val):
        """Actualiza el field of view de la cámara"""
        self.camara.fov = val
        self.actualizar_visualizacion()
        
    def actualizar_distancia(self, val):
        """Actualiza la distancia de la cámara"""
        self.camara.posicion[2] = val
        self.actualizar_visualizacion()
        
    def cambiar_proyeccion(self, event):
        """Cambia entre proyección perspectiva y ortográfica"""
        self.tipo_proyeccion = 'ortografica' if self.tipo_proyeccion == 'perspectiva' else 'perspectiva'
        self.actualizar_visualizacion()
        
    def iniciar_animacion(self, event):
        """Inicia una animación de la cámara"""
        for angle in np.linspace(0, 2*np.pi, 60):
            self.camara.posicion[0] = 5 * np.cos(angle)
            self.camara.posicion[2] = 5 * np.sin(angle)
            self.actualizar_visualizacion()
            plt.pause(0.05)
    
    def dibujar_escena_3d(self):
        """Dibuja la escena 3D original"""
        self.ax_3d.clear()
        self.ax_3d.set_title('Escena 3D Original')
        
        # Dibujar cubo
        self.ax_3d.scatter(self.cubo[0], self.cubo[1], self.cubo[2], 
                          c='red', s=50, label='Cubo')
        
        # Dibujar pirámide
        self.ax_3d.scatter(self.piramide[0], self.piramide[1], self.piramide[2], 
                          c='blue', s=50, label='Pirámide')
        
        # Dibujar esfera
        self.ax_3d.scatter(self.esfera[0], self.esfera[1], self.esfera[2], 
                          c='green', s=20, alpha=0.6, label='Esfera')
        
        # Dibujar posición de la cámara
        self.ax_3d.scatter(self.camara.posicion[0], self.camara.posicion[1], 
                          self.camara.posicion[2], c='black', s=100, marker='^', label='Cámara')
        
        self.ax_3d.set_xlabel('X')
        self.ax_3d.set_ylabel('Y')
        self.ax_3d.set_zlabel('Z')
        self.ax_3d.legend()
        self.ax_3d.set_xlim([-5, 5])
        self.ax_3d.set_ylim([-5, 5])
        self.ax_3d.set_zlim([-5, 5])
    
    def dibujar_proyeccion_2d(self, ax, tipo, titulo):
        """Dibuja la proyección 2D de la escena"""
        ax.clear()
        ax.set_title(f'{titulo} - {tipo.capitalize()}')
        
        # Proyectar todos los objetos
        cubo_2d = self.camara.proyectar_puntos(self.cubo, tipo)
        piramide_2d = self.camara.proyectar_puntos(self.piramide, tipo)
        esfera_2d = self.camara.proyectar_puntos(self.esfera, tipo)
        
        # Dibujar proyecciones
        ax.scatter(cubo_2d[0], cubo_2d[1], c='red', s=50, label='Cubo')
        ax.scatter(piramide_2d[0], piramide_2d[1], c='blue', s=50, label='Pirámide')
        ax.scatter(esfera_2d[0], esfera_2d[1], c='green', s=20, alpha=0.6, label='Esfera')
        
        ax.set_xlabel('X proyectado')
        ax.set_ylabel('Y proyectado')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        
        # Resaltar el tipo de proyección actual
        if tipo == self.tipo_proyeccion:
            ax.set_facecolor('#ffffcc')
        else:
            ax.set_facecolor('white')
    
    def mostrar_parametros(self):
        """Muestra los parámetros actuales de la cámara"""
        self.ax_params.clear()
        self.ax_params.set_title('Parámetros de la Cámara')
        
        parametros = [
            f"Tipo: {self.tipo_proyeccion.capitalize()}",
            f"Posición: ({self.camara.posicion[0]:.1f}, {self.camara.posicion[1]:.1f}, {self.camara.posicion[2]:.1f})",
            "",
            "Perspectiva:",
            f"  FOV: {self.camara.fov:.1f}°",
            f"  Near: {self.camara.near}",
            f"  Far: {self.camara.far}",
            "",
            "Ortográfica:",
            f"  Left/Right: {self.camara.left}/{self.camara.right}",
            f"  Bottom/Top: {self.camara.bottom}/{self.camara.top}"
        ]
        
        for i, param in enumerate(parametros):
            self.ax_params.text(0.1, 0.9 - i*0.08, param, transform=self.ax_params.transAxes,
                               fontsize=10, verticalalignment='top')
        
        self.ax_params.set_xlim([0, 1])
        self.ax_params.set_ylim([0, 1])
        self.ax_params.axis('off')
    
    def actualizar_visualizacion(self):
        """Actualiza toda la visualización"""
        self.dibujar_escena_3d()
        self.dibujar_proyeccion_2d(self.ax_2d_persp, 'perspectiva', 'Proyección Perspectiva')
        self.dibujar_proyeccion_2d(self.ax_2d_orto, 'ortografica', 'Proyección Ortográfica')
        self.mostrar_parametros()
        
        plt.tight_layout()
        self.fig.canvas.draw()
    
    def ejecutar(self):
        """Ejecuta el visualizador"""
        self.actualizar_visualizacion()
        plt.show()

def demostrar_matrices():
    """
    Función para demostrar el cálculo de matrices de proyección
    """
    print("🔍 DEMOSTRACIÓN DE MATRICES DE PROYECCIÓN")
    print("=" * 50)
    
    camara = CamaraVirtual()
    
    # Punto de ejemplo
    punto_3d = np.array([[2], [1], [-3]])
    print(f"Punto 3D original: {punto_3d.flatten()}")
    
    # Proyección perspectiva
    punto_persp = camara.proyectar_puntos(punto_3d, 'perspectiva')
    print(f"Proyección perspectiva: ({punto_persp[0,0]:.3f}, {punto_persp[1,0]:.3f})")
    
    # Proyección ortográfica
    punto_orto = camara.proyectar_puntos(punto_3d, 'ortografica')
    print(f"Proyección ortográfica: ({punto_orto[0,0]:.3f}, {punto_orto[1,0]:.3f})")
    
    print("\n📐 MATRICES UTILIZADAS:")
    print("\nMatriz de Vista:")
    print(camara.matriz_vista())
    
    print("\nMatriz de Proyección Perspectiva:")
    print(camara.matriz_proyeccion_perspectiva())
    
    print("\nMatriz de Proyección Ortográfica:")
    print(camara.matriz_proyeccion_ortografica())

if __name__ == "__main__":
    print("🎯 TALLER: Proyecciones 3D - Cómo ve una Cámara Virtual")
    print("=" * 60)
    
    # Demostrar cálculos de matrices
    demostrar_matrices()
    
    print("\n🚀 Iniciando visualizador interactivo...")
    print("Controles:")
    print("- Usa los sliders para cambiar FOV y distancia")
    print("- Haz clic en 'Cambiar Proyección' para alternar entre perspectiva y ortográfica")
    print("- Haz clic en 'Animar Cámara' para ver una animación orbital")
    
    # Crear y ejecutar el visualizador
    visualizador = VisualizadorProyecciones()
    visualizador.ejecutar()