using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MouseCameraController : MonoBehaviour
{
    public float sensitivity = 5.0f;      // Sensibilidad del mouse
    public float verticalClamp = 80f;     // Límite de rotación vertical

    private float rotationX = 0f;
    private float rotationY = 0f;

    void Start()
    {
        // Inicializar la rotación con la rotación actual de la cámara
        Vector3 rotation = transform.eulerAngles;
        rotationX = rotation.y;
        rotationY = rotation.x;
    }

    void Update()
    {
        if (Input.GetMouseButton(1)) // Click derecho presionado
        {
            float mouseX = Input.GetAxis("Mouse X") * sensitivity;
            float mouseY = Input.GetAxis("Mouse Y") * sensitivity;

            rotationX += mouseX;
            rotationY -= mouseY; // Se invierte para que el movimiento sea natural
            rotationY = Mathf.Clamp(rotationY, -verticalClamp, verticalClamp);

            transform.rotation = Quaternion.Euler(rotationY, rotationX, 0f);
        }
    }
}
