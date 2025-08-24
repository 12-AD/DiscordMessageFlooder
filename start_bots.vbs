' start_bots.vbs
Set objArgs = WScript.Arguments
Dim autoNo
autoNo = False

If objArgs.Count > 0 Then
    If LCase(objArgs(0)) = "no" Then
        autoNo = True
    End If
End If

If autoNo = True Then
    runHidden = True
Else
    answer = MsgBox("Do you want to show the console windows?", vbYesNo + vbQuestion, "Start Bots")
    If answer = vbYes Then
        runHidden = False
    Else
        runHidden = True
    End If
End If

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

Set folder = objFSO.GetFolder(objFSO.BuildPath(objFSO.GetParentFolderName(WScript.ScriptFullName), "bots"))

For Each file In folder.Files
    If LCase(objFSO.GetExtensionName(file.Name)) = "py" And file.Name <> "manager.py" Then
        If runHidden Then
            objShell.Run "python " & Chr(34) & file.Path & Chr(34), 0
        Else
            objShell.Run "python " & Chr(34) & file.Path & Chr(34), 1
        End If
    End If
Next
