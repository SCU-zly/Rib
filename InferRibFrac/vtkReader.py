#!/usr/bin/env python
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOXML import vtkXMLPolyDataReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
def get_program_parameters():
    import argparse
    description = 'Read a polydata file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='Torso.vtp')
    parser.add_argument('--Rendername', help='ReadPolyData',default='ReadPolyData',required=False)

    args = parser.parse_args()
    return args.filename,args.Rendername

def main():
    colors = vtkNamedColors()

    filename,Rendername= get_program_parameters()

    # Read all the data from the file
    reader = vtkXMLPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()

    # Visualize
    mapper = vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())

    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor(colors.GetColor3d('NavajoWhite'))

    renderer = vtkRenderer()
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d('Black'))
    renderer.GetActiveCamera().Pitch(90)
    renderer.GetActiveCamera().SetViewUp(0, 0, 1)
    renderer.ResetCamera()

    renderWindow.SetSize(600, 600)
    renderWindow.Render()
    renderWindow.SetWindowName(Rendername)
    renderWindowInteractor.Start()


if __name__ == '__main__':
    main()