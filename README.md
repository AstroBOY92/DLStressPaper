# Stress distribution analysis in ZrB2-SiC based thermal protection system using machine learning driven approach
## Carmine Zuccarini,Karthikeyan Ramachandran and Dr Doni Daniel Jayaseelan

This repository should help the recreation of the work carreied out as part of the paper above mentioned that is seeking publication in Applied Physics and ML Journals
In oder to use this repository following systems/software are required
1) Mathlab
2) Mathlab python engine (https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
3) Mathlab Deeplearning Toolkit
4) Python interpreter

### Files in the repository

(1) ShapeData.mat - this file is the code that allows the topological mapping of the Geometry
(2) Thermo.mat - Dataset generate from the Termo fluid analysys
(3) StressData.mat - Datasets for the material propreites
(4) Mathlab codes for Reading and Writing Polygon meshes and templates:ReadMeshFromVTKFile.m , ReadPolygonMeshFromVTKFile.m, WritePolygonMeshAsVTKFile.m,TemplateMesh2D.vtk. 
(5) DLStress.py - python code that generates the results on the model using matplotlib and numpy

The code and files provided are to be considered "As is" and without any express or implied warranties, including, without limitation the implied warraties of merchantability and fitness for a particular purpose.

