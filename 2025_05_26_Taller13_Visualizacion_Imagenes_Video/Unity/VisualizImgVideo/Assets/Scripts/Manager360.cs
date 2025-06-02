using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Manager360 : MonoBehaviour
{
    [Header("Referencias")]
    public GameObject esferapanoramica;
    public GameObject esferaVideo;
    public Slider sliderModo;
    
    private VideoPanoramico videoScript;
    
    void Start()
    {
        // Obtener scripts
        videoScript = esferaVideo.GetComponent<VideoPanoramico>();
        
        // Configurar slider
        if (sliderModo != null)
        {
            sliderModo.minValue = 1;
            sliderModo.maxValue = 2;
            sliderModo.wholeNumbers = true; // Solo números enteros
            sliderModo.value = 1; // Empezar con imagen
            
            // Agregar listener para cuando cambie el valor
            sliderModo.onValueChanged.AddListener(CambiarModo);
        }
        
        // Mostrar imagen por defecto
        CambiarModo(1);
    }
    
    public void CambiarModo(float valor)
    {
        int modoSeleccionado = Mathf.RoundToInt(valor);
        
        switch (modoSeleccionado)
        {
            case 1:
                MostrarImagen();
                break;
            case 2:
                MostrarVideo();
                break;
            default:
                Debug.LogWarning("Modo no válido: " + modoSeleccionado);
                break;
        }
    }
    
    private void MostrarImagen()
    {
        esferapanoramica.SetActive(true);
        esferaVideo.SetActive(false);
        
        // Pausar video si estaba reproduciéndose
        if (videoScript != null)
        {
            videoScript.DetenerVideo();
        }
        
    }
    
    private void MostrarVideo()
    {
        esferapanoramica.SetActive(false);
        esferaVideo.SetActive(true);
        
        // Iniciar reproducción automáticamente
        if (videoScript != null)
        {
            videoScript.ReproducirVideo();
        }
        
    }
    
    // Método público para cambiar modo desde código
    public void SetModo(int modo)
    {
        if (sliderModo != null)
        {
            sliderModo.value = modo;
        }
        else
        {
            CambiarModo(modo);
        }
    }
}