import mc
def toggleLoginVisibility(visibility=True):
    if visibility:
        logoutBtnVisibility = False
    else:
        logoutBtnVisibility = True 
    mc.GetActiveWindow().GetControl(991).SetVisible(visibility)
    mc.GetActiveWindow().GetControl(992).SetVisible(visibility)
    mc.GetActiveWindow().GetControl(993).SetVisible(visibility)
    mc.GetActiveWindow().GetControl(994).SetVisible(logoutBtnVisibility)


def showErrorMessage(message):
    mc.ShowDialogNotification(message)