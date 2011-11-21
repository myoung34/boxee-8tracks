'''
Created on Nov 21, 2011

@author: civascu
'''
import urllib
import simplejson
import pprint
#import mc
            
def getFeaturedMixes():
    featured_url = "http://8tracks.com/mixes.jsonp?api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc&api_version=2&page=2"
    fd = urllib.urlopen(featured_url)
    mix_sets = simplejson.loads(fd.read())
    for mix in mix_sets["mixes"]:
        name = mix["name"].replace(u'\xbd', '')
        trackD = urllib.urlopen("http://8tracks.com/sets/460486803/play.json?mix_id=%s&api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc&api_version=2" % mix["id"])
        trackInformation = simplejson.loads(trackD.read())
        print trackInformation['set']['track']['url']
if __name__ == '__main__':
    getFeaturedMixes();
    