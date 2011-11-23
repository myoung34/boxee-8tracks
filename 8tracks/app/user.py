'''
Created on Nov 23, 2011

@author: civascu
'''
import mc
from app import api

def getUser():
    global _user
    try:
        if not _user:
            _user = User()
    except:
        _user = User()
    return _user

class User(object):
    isAuthenticated = False
    config = mc.GetApp().GetLocalConfig()
    
    def __init__(self):
        try:
            self.userName = self.config.GetValue("username")
            self.userPassword = self.config.GetValue("password")
        except:
            self.userName = ''
            self.userPassword = ''
        if (len(self.userName) > 0 and len(self.userPassword) > 0):
            self.authenticate(self.userName, self.userPassword)
            
    def authenticate(self, user, password):
        if (api.doLogin(user, password)):
            self.config.SetValue('username', user)
            self.config.SetValue('password', password)
            self.isAuthenticated = True
    
    def logout(self):
        self.config.Reset('username')
        self.config.Reset('password')
        self.config.Reset('user-token')
        self.config.Reset('auth-token')
        self.isAuthenticated = False
        