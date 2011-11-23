import urllib
import simplejson
import mc
baseUrl = "http://8tracks.com"
loginPath = "sessions.jsonp"
apiKey = "api_key=a07ee2f7cc1577f749ed10d2c796fc52515243cc"
apiVersion = "api_version=2"

def doLogin(user, password):
    params = urllib.urlencode({'login': user, 'password':password})
    url = "%s/%s?%s&%s" % (baseUrl, loginPath, apiKey, apiVersion)
    fd = urllib.urlopen(url, params)
    response = simplejson.loads(fd.read())
    config = mc.GetApp().GetLocalConfig()
    if (response['status'] != '200 OK'):
        config.Reset('auth-token')
        config.Reset('user-token')
        return False
    else: 
        config.SetValue("auth-token", str(response['auth_token']))
        config.SetValue('user-token', str(response['user_token']))
        return True