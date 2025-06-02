using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Video;

public class VideoPanoramico : MonoBehaviour
{
    [Header("Configuración Video 360°")]
    public string nombreVideo = "video360_1";
    public bool reproducirAlInicio = true;
    public bool enBucle = true;
    
    private VideoPlayer videoPlayer;
    private Renderer sphereRenderer;
    
    void Start()
    {
        ConfigurarComponentes();
        CargarVideo360();
    }
    
    void ConfigurarComponentes()
    {
        // Obtener o añadir VideoPlayer
        videoPlayer = GetComponent<VideoPlayer>();
        if (videoPlayer == null)
        {
            videoPlayer = gameObject.AddComponent<VideoPlayer>();
        }
        
        // Obtener renderer de la esfera
        sphereRenderer = GetComponent<Renderer>();
        
        // Configurar VideoPlayer
        videoPlayer.renderMode = VideoRenderMode.MaterialOverride;
        videoPlayer.targetMaterialRenderer = sphereRenderer;
        videoPlayer.targetMaterialProperty = "_MainTex";
        videoPlayer.aspectRatio = VideoAspectRatio.Stretch;
        videoPlayer.isLooping = enBucle;
    }
    
    void CargarVideo360()
    {
        // Cargar video desde Resources
        VideoClip videoClip = Resources.Load<VideoClip>("Videos/" + nombreVideo);
        
        if (videoClip != null)
        {
            videoPlayer.clip = videoClip;
            
            // Crear material base
            Material materialVideo = new Material(Shader.Find("Skybox/Panoramic"));
            sphereRenderer.material = materialVideo;
            
            if (reproducirAlInicio)
            {
                videoPlayer.Play();
            }
            
            Debug.Log("Video 360° cargado: " + nombreVideo);
        }
        else
        {
            Debug.LogError("No se pudo cargar el video: " + nombreVideo);
        }
    }
    
    // Métodos públicos para controlar reproducción
    public void ReproducirVideo()
    {
        videoPlayer.Play();
    }
    
    public void PausarVideo()
    {
        videoPlayer.Pause();
    }
    
    public void DetenerVideo()
    {
        videoPlayer.Stop();
    }
    
    public void CambiarVideo(string nuevoVideo)
    {
        nombreVideo = nuevoVideo;
        CargarVideo360();
    }
}
