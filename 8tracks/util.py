import mc
import urllib
import simplejson

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
            
def getFeaturedMixes():
    mc.ShowDialogWait()
    featured_url = "http://8tracks.com/mixes.json?api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc&api_version=2&per_page=30&page=1"
    fd = urllib.urlopen(featured_url)
    mix_sets = simplejson.loads(fd.read())
    listItems = mc.ListItems()
    for mix in mix_sets["mixes"]:
        item = mc.ListItem(mc.ListItem.MEDIA_AUDIO_OTHER)
        item.SetArtist(str(mix["user"]["login"]))
        year = mix['first_published_at'][1:4]
        month = mix['first_published_at'][6:7]
        day=mix['first_published_at'][9:10]
        item.SetDate(int(year), int(month), int(day))
        name = mix["name"].replace(u'\xbd', '')
        item.SetLabel(str(name))
        item.SetThumbnail(str(mix['cover_urls']['original']))
        item.SetIcon(str(mix['cover_urls']['sq100']))
        
        # get the real track url, so default actions like play would work
        trackD = urllib.urlopen("http://8tracks.com/sets/460486803/play.json?mix_id=%s&api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc&api_version=2" % mix["id"])
        trackInformation = simplejson.loads(trackD.read())
        item.SetPath(str(trackInformation['set']['track']['url']))
        item.SetProperty("id", str(mix['id']))
        listItems.append(item)
    mc.GetWindow(14000).GetList(201).SetItems(listItems)
    mc.GetWindow(14000).GetList(201).Refresh()
    mc.HideDialogWait()
    
def playMix():
    list = mc.GetActiveWindow().GetList(201)
    items = list.GetItems()
    selected = items[list.GetFocusedItem()]
    selectedId = selected.GetProperty("id")
    # get the actual url for this mix
    
    fd = urllib.urlopen("http://8tracks.com/sets/460486803/play.json?mix_id=438741&api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc&api_version=2")
    mc.ShowDialogOk("Play", "Play %s with ID: %s" % (selected.GetTitle(), selectedId))