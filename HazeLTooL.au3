#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>
#include <FileConstants.au3>
#include <MsgBoxConstants.au3>

Global $hWelcomeGUI, $btnGetCoordinates, $btnRunBots
$hWelcomeGUI = GUICreate("HazeL Tool", 300, 110)
$btnGetCoordinates = GUICtrlCreateButton("Start Scanning a Website", 10, 10, 280, 40)
$btnRunLic = GUICtrlCreateButton("Licence", 10, 60, 280, 40)
GUISetState(@SW_SHOW)



While 1
    $msg = GUIGetMsg()
    Switch $msg
        Case $GUI_EVENT_CLOSE
            ExitLoop
        Case $btnGetCoordinates
            GUIDelete($hWelcomeGUI)
            ShowCoordinatesScript()
		Case $btnRunLic
		Licence()
    EndSwitch
WEnd

Func ShowCoordinatesScript()
    Global $hGUI, $Label, $SaveButton
    $hGUI = GUICreate("HazeL Tool", 300, 100)
    $Label = GUICtrlCreateLabel("Scan en cours ...", 10, 10, 280, 30)
    GUISetState(@SW_SHOW)

	startscript()

EndFunc

Func UpdateCoordinates()
    Local $MousePos = MouseGetPos()
    GUICtrlSetData($Label, "X: " & $MousePos[0] & ", Y: " & $MousePos[1])
EndFunc




Func Licence()
    MsgBox(0, "Licence", "Programme réalisé par HazeL, tous leaks, divulgations ou détournements sont interdits, si vous souhaitez me contacter, hazel_dev sur Discord. Ce programme est protégé contre les leaks !")
EndFunc

Func startscript()
	Run("cmd.exe /k ", "", @SW_SHOW)
EndFunc