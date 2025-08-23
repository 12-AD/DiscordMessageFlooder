Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Ask user if they want consoles visible
choice = MsgBox("Do you want to run the bots with console windows?", vbYesNo + vbQuestion, "Bot Launcher")

' Set paths
botsFolder = ".\bots\"   ' Folder containing your .py bot files
pythonExe = "python.exe"
pythonwExe = "pythonw.exe"

' Get all .py files in the bots folder
Set folder = fso.GetFolder(botsFolder)
For Each file In folder.Files
    If LCase(fso.GetExtensionName(file.Name)) = "py" Then
        If choice = vbYes Then
            ' Run with console
            WshShell.Run """" & pythonExe & """ """ & file.Path & """", 1, False
        Else
            ' Run hidden
            WshShell.Run """" & pythonwExe & """ """ & file.Path & """", 0, False
        End If
    End If
Next
