using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro; 

public class Interpolador : MonoBehaviour
{
    public Transform puntoInicio;
    public Transform puntoFinal;
    public float duracion = 3f;

    public AnimationCurve curvaSuavizado;

    private float tiempo;
    public TMP_Text textoTiempo;

    void Update()
    {
        
        tiempo += Time.deltaTime;
        float t = Mathf.Clamp01(tiempo / duracion);
        float tCurvado = curvaSuavizado.Evaluate(t);

        if (textoTiempo != null && duracion>tiempo)
        {
            textoTiempo.text = $"{tiempo:F2}s";
        }

        transform.position = Vector3.Lerp(puntoInicio.position, puntoFinal.position, tCurvado);

        // Interpolación de rotación suave
        Quaternion rotInicial = Quaternion.identity;
        Quaternion rotFinal = Quaternion.Euler(0, 180, 0);
        transform.rotation = Quaternion.Slerp(rotInicial, rotFinal, tCurvado);

        if (Input.GetKeyDown("space"))
        {
            tiempo = 0f;
        }
    }
}
