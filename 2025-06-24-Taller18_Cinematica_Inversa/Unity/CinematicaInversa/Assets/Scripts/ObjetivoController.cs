using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjetivoController : MonoBehaviour
{
    [Header("Configuración de Movimiento")]
    [SerializeField] private float moveSpeed = 5f;
   
    private Camera mainCamera;
    
    void Start()
    {
        mainCamera = Camera.main;
    }
    
    void Update()
    {
        HandleKeyboardControl();

    }
        
    void HandleKeyboardControl()
    {
        Vector3 movement = new Vector3();
        
        if (Input.GetKey(KeyCode.W)) movement += Vector3.forward;
        if (Input.GetKey(KeyCode.S)) movement += Vector3.back;
        if (Input.GetKey(KeyCode.A)) movement += Vector3.left;
        if (Input.GetKey(KeyCode.D)) movement += Vector3.right;
        if (Input.GetKey(KeyCode.Space)) movement += Vector3.up;
        
        transform.position += movement * moveSpeed * Time.deltaTime;
    }
    
}