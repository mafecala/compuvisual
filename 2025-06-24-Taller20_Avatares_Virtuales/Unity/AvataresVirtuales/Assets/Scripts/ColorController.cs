using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ColorControlller : MonoBehaviour
{
    public Slider sliderR, sliderG, sliderB;
    public Renderer targetRenderer;

    void Update()
    {
        Color newColor = new Color(sliderR.value, sliderG.value, sliderB.value);
        targetRenderer.material.color = newColor;
    }
}
