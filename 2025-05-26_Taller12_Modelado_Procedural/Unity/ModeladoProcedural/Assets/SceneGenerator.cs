using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SceneGenerator : MonoBehaviour
{
    public Material customMaterial;
    public int gridSize = 5;
    public int spiralCount = 30;
    public float spiralRadius = 5f;
    public int fractalDepth = 2;
    private GameObject contentParent;
    private GameObject GeneratedObjects;

    void Start()
    {
        GameObject existing = GameObject.Find("GeneratedObjects");
        if (existing != null)
        {
            DestroyImmediate(existing);
        }
    }

    public void OnSliderChanged(float value)
    {
        int mode = Mathf.RoundToInt(value);
        GenerateMode(mode); 
    }

    public void GenerateMode(int mode)
    {
        ClearPrevious();

        switch (mode)
        {
            case 0:
                break;
            case 1:
                GenerateCubeGrid();
                break;
            case 2:
                GenerateCylinderSpiral();
                break;
            case 3:
                GenerateFractalPyramid(Vector3.zero, 5, fractalDepth);
                break;
            case 4:
                GenerateCustomMesh();
                break;
        }
    }

    void ClearPrevious()
    {
        if (contentParent != null)
            DestroyImmediate(contentParent);

        contentParent = new GameObject("GeneratedObjects");
    }

    void GenerateCubeGrid()
    {
        float spacing = 2f;
        for (int x = 0; x < gridSize; x++)
        {
            for (int z = 0; z < gridSize; z++)
            {
                GameObject cube = GameObject.CreatePrimitive(PrimitiveType.Cube);
                cube.transform.position = new Vector3(x * spacing, 0, z * spacing);
                cube.transform.localScale = Vector3.one * 1.5f;
                cube.transform.parent = contentParent.transform;
                cube.GetComponent<Renderer>().material = customMaterial;
            }
        }
    }

    void GenerateCylinderSpiral()
    {
        for (int i = 0; i < spiralCount; i++)
        {
            float angle = i * 20f * Mathf.Deg2Rad;
            float height = i * 0.5f;
            Vector3 pos = new Vector3(Mathf.Cos(angle) * spiralRadius, height, Mathf.Sin(angle) * spiralRadius);
            GameObject cylinder = GameObject.CreatePrimitive(PrimitiveType.Cylinder);
            cylinder.transform.position = pos;
            cylinder.transform.Rotate(Vector3.up, i * 10f);
            cylinder.transform.parent = contentParent.transform;
            cylinder.GetComponent<Renderer>().material = customMaterial;
        }
    }

    void GenerateFractalPyramid(Vector3 pos, float size, int depth)
    {
        if (depth <= 0) return;

        GameObject pyramid = GameObject.CreatePrimitive(PrimitiveType.Cube);
        pyramid.transform.position = pos;
        pyramid.transform.localScale = new Vector3(size, size, size);
        pyramid.transform.parent = contentParent.transform;
        pyramid.GetComponent<Renderer>().material = customMaterial;

        float offset = size / 2f;
        float newSize = size / 2f;

        GenerateFractalPyramid(pos + new Vector3(offset, offset, 0), newSize, depth - 1);
        GenerateFractalPyramid(pos + new Vector3(-offset, offset, 0), newSize, depth - 1);
        GenerateFractalPyramid(pos + new Vector3(0, offset, offset), newSize, depth - 1);
        GenerateFractalPyramid(pos + new Vector3(0, offset, -offset), newSize, depth - 1);
    }

    void GenerateCustomMesh()
    {
        GameObject customObject = new GameObject("CustomPyramid", typeof(MeshFilter), typeof(MeshRenderer));
        Mesh mesh = new Mesh();

        Vector3[] vertices = new Vector3[]
        {
            new Vector3(0, 1, 0),
            new Vector3(-1, 0, 1),
            new Vector3(1, 0, 1),
            new Vector3(1, 0, -1),
            new Vector3(-1, 0, -1)
        };

        int[] triangles = new int[]
        {
            1, 2, 3,
            1, 3, 4,
            0, 1, 2,
            0, 2, 3,
            0, 3, 4,
            0, 4, 1
        };

        mesh.vertices = vertices;
        mesh.triangles = triangles;
        mesh.RecalculateNormals();

        customObject.GetComponent<MeshFilter>().mesh = mesh;
        customObject.GetComponent<MeshRenderer>().material = new Material(Shader.Find("Standard"));
        customObject.transform.position = Vector3.zero;
        customObject.transform.parent = contentParent.transform;
        customObject.GetComponent<Renderer>().material = customMaterial;
    }
}
