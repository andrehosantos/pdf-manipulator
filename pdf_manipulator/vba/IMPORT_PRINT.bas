Attribute VB_Name = "IMPORTAR_IMPRIMIR"
Sub Importar_e_Imprimir()

  Dim file As String
  Dim i As Integer
  i = 1
  file = Dir(path)
  Do While file <> ""
    Importar (file)
    Imprimir
    file = Dir
    i = i + 1
  Loop
  
  
    Dim path As String
    path = TextBox1.Value
    Dim doc1 As Document
    Set doc1 = OpenDocumentEx("C:\Users\andre\Documents\DIGIX\Blocos\print\numeracao-0002.pdf", openopt)
    With doc1.PrintSettings
        .PrintRange = prnPageRange
        .PageRange = "1-5"
    End With
    doc1.PrintOut

End Sub

Function Importar(path As String)
  Dim file As String
  Dim i As Integer
  i = 1
  file = Dir(path)
  Do While file <> ""
    Dim impopt As StructImportOptions
    Set impopt = CreateStructImportOptions
    impopt.MaintainLayers = True
    Dim impflt As ImportFilter
    Set impflt = ActiveLayer.ImportEx(file, cdrAI9, impopt)
    impflt.Finish
    Dim s1 As Shape
    Set s1 = ActiveShape
    ActiveDocument.AddToSelection ActiveLayer.Shapes(2), ActiveLayer.Shapes(3), ActiveLayer.Shapes(4), ActiveLayer.Shapes(5), ActiveLayer.Shapes(6), ActiveLayer.Shapes(7), ActiveLayer.Shapes(8), ActiveLayer.Shapes(9), s1
    Dim grp1 As ShapeRange
    Set grp1 = ActiveSelection.UngroupEx
    Dim openopt As StructOpenOptions
    Set openopt = CreateStructOpenOptions
    With openopt.ColorConversionOptions
        .SourceColorProfileList = "sRGB IEC61966-2.1,Coated FOGRA27 (ISO 12647-2:2004),Dot Gain 20%"
        .TargetColorProfileList = "sRGB IEC61966-2.1,Coated FOGRA27 (ISO 12647-2:2004),Dot Gain 20%"
    End With
    file = Dir
    i = i + 1
  Loop
End Function

Function Imprimir()

End Function
