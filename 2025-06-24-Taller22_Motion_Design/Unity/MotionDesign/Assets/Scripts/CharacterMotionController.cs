using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharacterMotionController : MonoBehaviour
{
    Animator animator;

    void Start()
    {
        animator = GetComponent<Animator>();
    }

    void Update()
    {
        // Disparo animación Wave al presionar A
        if (Input.GetKeyDown(KeyCode.A))
        {
            animator.SetTrigger("Wave");
        }

        // Disparo animación Dancing al presionar Espacio
        if (Input.GetKeyDown(KeyCode.Space))
        {
            animator.SetTrigger("Dance");
        }

        // Activo Walk mientras se mantenga presionada la tecla W
        if (Input.GetKey(KeyCode.W))
        {
            animator.SetBool("IsWalking", true);
        }
        else
        {
            animator.SetBool("IsWalking", false);
        }
    }
}
