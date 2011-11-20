import mc

def show_message():
    mc.ShowDialogOk("MSG", 'Starting?')

tabs = [10, 11, 12, 13, 14]

def toggleTabs(tabIndex):
    global tabs
    
    for tab in tabs:
        if tab != tabIndex:
            toggle = mc.GetActiveWindow().GetToggleButton(tab)
            if toggle.IsSelected():
                toggle.SetSelected(False);
        else:
            mc.GetActiveWindow().GetToggleButton(tabIndex).SetSelected(True)