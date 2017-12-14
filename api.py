import requests

class Api(object):
    def __init__(self, url):
        self.url = url
            
    def get(self, params=None, headers=None, cookies=None, allow_redirects=False, auth=None, stream=None, timeout=None):
        try:
            r = requests.get(self.url, params=params, headers=headers, cookies=cookies, 
                             allow_redirects=allow_redirects, auth=auth, stream=stream, timeout=timeout, verify=True)
        except Exception as e:
            print("Exception occurred in get request", e)
        return r
                    
    def post(self, data=None, json=None, headers=None, files=None, timeout=None):
        try:
            r = requests.post(self.url, data=data, json=json, headers=headers, files=files, timeout=timeout)
        except Exception as e:
            print("Exception occurred in post request", e)
        return r
    
    def put(self):
        pass
    
    def delete(self):
        pass
        
        
        
    