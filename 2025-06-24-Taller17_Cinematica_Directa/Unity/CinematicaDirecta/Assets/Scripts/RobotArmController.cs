using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RobotArmController : MonoBehaviour
{
    [Header("Articulaciones del Brazo")]
    public Transform brazo1Transform;
    public Transform brazo2Transform;
    public Transform pinzaTransform;
    public Transform MarcadorTransform;
    
    [Header("Control de Ángulos")]

    [Range(-120f, 120f)]
    public float brazo1Angle = 0f;
    
    [Range(-120f, 120f)]
    public float brazo2Angle = 0f;
    
    [Range(-120f, 120f)]
    public float pinzaAngle = 0f;
    
    [Header("Animación Automática")]
    public bool autoAnimate = true;
    public float animationSpeed = 1f;
    
    
    // Variables privadas
    private float timeCounter = 0f;
    
    void Start()
    {

    }
    
    void Update()
    {

        // Animación automática si está activada
        if (autoAnimate)
        {
            // Actualizar tiempo
            timeCounter += Time.deltaTime * animationSpeed;
            AnimateArm();
        }
        
        // Aplicar rotaciones
        ApplyRotations();
        
        // Debug información
        DebugInfo();
    }
    
    void AnimateArm()
    {
        // Animación sinusoidal para cada articulación
        brazo1Angle = Mathf.Sin(timeCounter * 0.8f) * 45f;
        brazo2Angle = Mathf.Sin(timeCounter * 1.2f) * 60f;
        pinzaAngle = Mathf.Sin(timeCounter * 1.5f) * 90f;
    }
    
    void ApplyRotations()
    {
        // Aplicar rotaciones locales a cada articulación        
        if (brazo1Transform != null)
            brazo1Transform.localRotation = Quaternion.Euler(brazo1Angle, 0, 0);
        
        if (brazo2Transform != null)
            brazo2Transform.localRotation = Quaternion.Euler(brazo2Angle, 0, 0);
        
        if (pinzaTransform != null)
            pinzaTransform.localRotation = Quaternion.Euler(0, 0, pinzaAngle);
    }
        
    void DebugInfo()
    {
        if (MarcadorTransform != null)
        {
            // Mostrar información de posición en consola cada segundo
            if (Time.time % 1f < Time.deltaTime)
            {
                Debug.Log($"End Effector Position: {MarcadorTransform.position}");
            }
            
            // Dibujar líneas de debug
            Debug.DrawLine(transform.position, MarcadorTransform.position, Color.green);
        }
    }
}