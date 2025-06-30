using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IKSolverCCD : MonoBehaviour
{
    [Header("Configuración IK")]
    [SerializeField] private Transform[] joints; // Articulaciones de la cadena
    [SerializeField] private Transform target;   // Objetivo a alcanzar
    [SerializeField] private Transform endEffector; // Punto final (mano)
    
    [Header("Parámetros del Solver")]
    [SerializeField] private int maxIterations = 10;
    [SerializeField] private float maxAngleStep = 10f;

    [SerializeField] private float tolerance = 0.01f;
    [SerializeField] private bool enableIK = true;
    
    [Header("Visualización")]
    [SerializeField] private bool showDebugLines = true;
    [SerializeField] private Color debugLineColor = Color.red;
    
    private Vector3[] originalRotations;
    
    void Start()
    {
        // Guardar rotaciones originales
        originalRotations = new Vector3[joints.Length];
        for (int i = 0; i < joints.Length; i++)
        {
            originalRotations[i] = joints[i].eulerAngles;
        }
    }
    
    void Update()
    {
        if (enableIK && target != null && endEffector != null)
        {
            SolveIK();
        }
        
        if (showDebugLines)
        {
            DrawDebugLines();
        }
    }
    
    void SolveIK()
{
    for (int iteration = 0; iteration < maxIterations; iteration++)
    {
        float distanceToTarget = Vector3.Distance(endEffector.position, target.position);
        if (distanceToTarget < tolerance)
        {
            break;
        }

        for (int i = joints.Length - 1; i >= 0; i--)
        {
            Vector3 toEndEffector = endEffector.position - joints[i].position;
            Vector3 toTarget = target.position - joints[i].position;

            float angle = Vector3.Angle(toEndEffector, toTarget);
            if (angle > 0.01f)
            {
                Vector3 rotationAxis = Vector3.Cross(toEndEffector, toTarget).normalized;

                // Factor de influencia según la distancia al end effector
                float weight = (float)(i + 1) / joints.Length;

                // Clampeo del ángulo a un valor máximo por paso
                float clampedAngle = Mathf.Min(angle, maxAngleStep * weight);

                // Rotación deseada con interpolación suave
                Quaternion targetRotation = Quaternion.AngleAxis(clampedAngle, rotationAxis) * joints[i].rotation;
                joints[i].rotation = Quaternion.Slerp(joints[i].rotation, targetRotation, 0.5f);
            }
        }
    }
}

    
    void DrawDebugLines()
    {
        // Dibujar línea desde end effector hasta objetivo
        Debug.DrawLine(endEffector.position, target.position, debugLineColor, 0.1f);
        
        // Dibujar la cadena de articulaciones
        for (int i = 0; i < joints.Length - 1; i++)
        {
            Debug.DrawLine(joints[i].position, joints[i + 1].position, Color.white, 0.1f);
        }
        
        // Línea desde la última articulación al end effector
        if (joints.Length > 0)
        {
            Debug.DrawLine(joints[joints.Length - 1].position, endEffector.position, Color.white, 0.1f);
        }
    }
}
