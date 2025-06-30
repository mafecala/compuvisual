using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class AIController : MonoBehaviour
{
    public enum EstadoIA { Patrolling, Chasing }
    public EstadoIA estadoActual = EstadoIA.Patrolling;

    public Transform[] puntosPatrullaje;
    public Transform jugador;
    private float rangoVision = 60f;
    private float anguloVision = 220f;

    private float velocidadPatrulla = 3f;
    private float velocidadPersecucion = 8f;

    public LayerMask obstaculo; // capa que incluye muros u obstáculos

    private NavMeshAgent agent;
    private Animator animator;
    private int index = 0;

    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        animator = GetComponent<Animator>();
        IrAlSiguientePunto();
    }

    void Update()
    {
        // Cambiar entre estados según línea de visión
        if (PuedeVerJugador())
        {
            estadoActual = EstadoIA.Chasing;
        }
        else if (estadoActual == EstadoIA.Chasing)
        {
            estadoActual = EstadoIA.Patrolling;
            IrAlSiguientePunto();
        }

        switch (estadoActual)
        {
            case EstadoIA.Patrolling:
                agent.speed = velocidadPatrulla;
                animator.SetBool("corriendo", false);
                Patrullar();
                break;

            case EstadoIA.Chasing:
                agent.speed = velocidadPersecucion;
                animator.SetBool("corriendo", true);
                Perseguir();
                break;
        }
    }

    void Patrullar()
    {
        if (!agent.pathPending && agent.remainingDistance < 0.5f)
        {
            index = (index + 1) % puntosPatrullaje.Length;
            IrAlSiguientePunto();
        }
    }

    void Perseguir()
    {
        Vector3 direccion = (jugador.position - transform.position).normalized;

        // Rotar suavemente hacia el jugador
        Quaternion rotacionDeseada = Quaternion.LookRotation(direccion);
        transform.rotation = Quaternion.Slerp(transform.rotation, rotacionDeseada, Time.deltaTime * 5f);

        agent.SetDestination(jugador.position);
    }
    bool PuedeVerJugador()
    {
        Vector3 origen = transform.position + Vector3.up*0.8f;
        Vector3 destino = jugador.position + Vector3.up *0.8f;
        Vector3 direccion = destino - origen;
        float distancia = direccion.magnitude;

        if (distancia > rangoVision)
            return false;

        float angulo = Vector3.Angle(transform.forward, direccion.normalized);
        if (angulo > anguloVision / 2f)
            return false;

        // Aquí solo hacemos raycast si ya está dentro del cono
        if (Physics.Linecast(origen, destino, out RaycastHit hit))
        {
            if (hit.collider.CompareTag("Player"))
            {
                return true;
            }
        }

        return false;
    }

    void IrAlSiguientePunto()
    {
        if (puntosPatrullaje.Length == 0) return;
        agent.SetDestination(puntosPatrullaje[index].position);
    }
}
