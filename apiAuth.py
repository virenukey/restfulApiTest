from api import Api
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests_oauthlib import OAuth1

class ApiAuth(Api):
    def __init__(self, url, auth):
        super(ApiAuth, self).__init__(url)
        self.auth = auth
        
    def httpBasicAuth(self):
        r = self.get(self.url, auth=HTTPBasicAuth(self.auth['user'], self.auth['pass']))
        return r
    
    def httpDigestAuth(self):
        r = self.get(self.url, auth=HTTPDigestAuth(self.auth['user'], self.auth['pass']))
        return r
    
    def oAuth(self):
        r = self.get(self.url, auth=OAuth1(self.auth['apiKey'], self.auth['appSecret'], 
                                           self.auth['oAuthToken'], self.auth['oAuthTokenSecret']))
        return r
    
    