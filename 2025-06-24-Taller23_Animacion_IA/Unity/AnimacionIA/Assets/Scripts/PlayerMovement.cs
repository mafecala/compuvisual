using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    bool grounded;
    float speedMovement = 7f;
    float gravity = 50f;
    float jumpForce = 15f;
    Vector3 jumpVector = Vector3.zero;
    CharacterController cc;

    private void Awake()
    {
        cc = GetComponent<CharacterController>();
    }

    void Update()
    {
        LayerMask mask = LayerMask.GetMask("Jumpable");

        if(Physics.Raycast(transform.position,Vector3.down,1.09f,mask))
        {
            grounded = true;
        }

        if (Input.GetKey(KeyCode.W))
        {
            cc.Move(transform.forward * speedMovement * Time.deltaTime);
        }

        if (Input.GetKey(KeyCode.S))
        {
           cc.Move(transform.forward * -speedMovement * Time.deltaTime);
        }

        if (Input.GetKey(KeyCode.D))
        {
            cc.Move(transform.right * speedMovement * Time.deltaTime);
        }
        if (Input.GetKey(KeyCode.A))
        {
            cc.Move(transform.right * -speedMovement * Time.deltaTime);
        }

        if (Input.GetKeyDown(KeyCode.Space) && grounded==true)
        {
            grounded = false;
            jumpVector.y = jumpForce; 
        }

        jumpVector.y -= gravity * Time.deltaTime;
        cc.Move(jumpVector*Time.deltaTime);
    }
    
}
