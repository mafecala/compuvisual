# Actividad en Python

  ![Animación de un triángulo rotando, trasladándose y creciendo en tamaño](https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22:%22animation.gif%22,%22type%22:%22image/gif%22,%22signedurl_expire%22:%222028-04-12T22:50:02.893Z%22,%22signedUrl%22:%22https://media-hosting.imagekit.io/66b26688a4734e30/animation.gif?Expires=1839192603&Key-Pair-Id=K2ZIVPTIP2VGHC&Signature=OW1zmVm-L~ql9wiPPLxnLKhexGoGopHa9b9oV9XiFVyWvHnQukz~SJIk6pMmhOD7vNw-v24qHxyX-eZby6FWX7ki2IPdMyjx83q1VjDyrtGDEwwXwalLz7pPCpGS0DMbPG7KAJ9EtVIMyJOUXo6fD71pqBpnHJJMj1HzqKQhPtDN3O-pnquekRqDq3MK2EXJurJj~pEzas4B4Vd9NXGtSZKP5srv3vbcIkroJFOo~t8WYszxpQaCQx7NGMgMPf~xj2sLkuDAEjzHhc99aBcXvOrqCpmSBas6kFZ9gBmdEe9lZqgKzTVFpVtFHvZrd~7GHtYWiZLc1Sng~NrNV2VPaA__%22%7D)

## Descripción
Proyecto en **Jupyter Notebook** que aplica transformaciones geométricas a un triángulo:
- **Traslación**
- **Rotación**  
- **Escala**

Usando multiplicación de matrices con `numpy` y visualización con `matplotlib`.

##  Características
- Usa matrices de transformación
- Hace una animación y genera un GIF
- Control de parámetros

## Cómo ejecutar

1.  Instalar requisitos:

`pip install numpy matplotlib pillow`    
    
2.  Ejecuta el Jupyter Notebook:

` jupyter notebook transformaciones.ipynb`

## Personalización

Se pueden modificar estos parámetros en el notebook:

    tx, ty = 3, 2          # traslación
    angulo = 60             # rotación en grados
    escala_inicial = 0.5    # escala
    escala_final = 1.5      

