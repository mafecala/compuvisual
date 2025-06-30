using UnityEngine;
using UnityEngine.UI;

public class UIController : MonoBehaviour
{
    [Header("Referencias")]
    public RobotArmController robotArmController;
    
    [Header("Sliders")]
    public Slider brazo1Slider;
    public Slider brazo2Slider;
    public Slider pinzaSlider;
    
    [Header("Controles")]
    public Toggle autoAnimateToggle;
    
    void Start()
    {
        // Configurar eventos de sliders
        brazo1Slider.onValueChanged.AddListener(OnBrazo1SliderChanged);
        brazo2Slider.onValueChanged.AddListener(OnBrazo2SliderChanged);
        pinzaSlider.onValueChanged.AddListener(OnPinzaSliderChanged);
        
        // Configurar eventos de controles
        autoAnimateToggle.onValueChanged.AddListener(OnAutoAnimateToggle);
    }
        
    void OnBrazo1SliderChanged(float value)
    {
        if (robotArmController != null)
            robotArmController.brazo1Angle = value;
    }
    
    void OnBrazo2SliderChanged(float value)
    {
        if (robotArmController != null)
            robotArmController.brazo2Angle = value;
    }
    
    void OnPinzaSliderChanged(float value)
    {
        if (robotArmController != null)
            robotArmController.pinzaAngle = value;
    }
    
    void OnAutoAnimateToggle(bool value)
    {
        if (robotArmController != null)
            robotArmController.autoAnimate = value;
    }
    
}