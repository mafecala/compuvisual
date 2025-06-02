using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class UVController : MonoBehaviour
{
    [Header("Material to Control")]
    public Material targetMaterial;
    
    [Header("UV Controls")]
    public Slider tilingXSlider;
    public Slider tilingYSlider;
    public Slider offsetXSlider;
    public Slider offsetYSlider;
        
    void Start()
    {
        // Configurar rangos de sliders
        tilingXSlider.minValue = 0.1f;
        tilingXSlider.maxValue = 5f;
        tilingXSlider.value = 1f;
        
        tilingYSlider.minValue = 0.1f;
        tilingYSlider.maxValue = 5f;
        tilingYSlider.value = 1f;
        
        offsetXSlider.minValue = -2f;
        offsetXSlider.maxValue = 2f;
        offsetXSlider.value = 0f;
        
        offsetYSlider.minValue = -2f;
        offsetYSlider.maxValue = 2f;
        offsetYSlider.value = 0f;
    }
    
    void Update()
    {
        if (targetMaterial != null)
        {
            // Actualizar tiling
            Vector2 tiling = new Vector2(tilingXSlider.value, tilingYSlider.value);
            targetMaterial.mainTextureScale = tiling;
            
            // Actualizar offset
            Vector2 offset = new Vector2(offsetXSlider.value, offsetYSlider.value);
            targetMaterial.mainTextureOffset = offset;
    
        }
    }
}