using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class AnimationController : MonoBehaviour
{
    public Animator animator;
    public bool paused = false;

    public void SetAnimation(int index)
    {
        animator.SetInteger("animationIndex", index);
    }

    public void PauseAnimation()
    {
        paused = !paused;
        if (paused == true)
        {
            animator.speed = 0f;
        }
        else
        {
            animator.speed = 1f;
        }        
    }   

    public void RestartAnimation()
    {
        animator.Play(animator.GetCurrentAnimatorStateInfo(0).shortNameHash, -1, 0f);
    }

}
