using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MaterialController : MonoBehaviour
{
    [Header("Material to Control")]
    public Material targetMaterial;
    
    [Header("UI Sliders")]
    public Slider metallicSlider;
    public Slider smoothnessSlider;
    
    void Start()
    {
        // Inicializar sliders con valores actuales del material
        if (targetMaterial != null)
        {
            metallicSlider.value = targetMaterial.GetFloat("_Metallic");
            smoothnessSlider.value = targetMaterial.GetFloat("_Glossiness");
        }
    }
    
    void Update()
    {
        if (targetMaterial != null)
        {
            // Actualizar propiedades del material
            targetMaterial.SetFloat("_Metallic", metallicSlider.value);
            targetMaterial.SetFloat("_Glossiness", smoothnessSlider.value);
        }
    }
}
