import unittest
from TestData.TestData import TestData
import setupTest
from api import Api
import constructURL
import re
import json

setuptest = setupTest.setupTest

class Testcase1(unittest.TestCase):
        
    @classmethod
    def setup_class(cls):
        try:
            testData = TestData(location=setuptest['location'], 
                                fileName=setuptest['fileName'])
            
            json_str = testData.data()
            return json_str
        except Exception as e:
            print ("Exception occurred during setup", e)
    
    def testRun(self):
        """Verify plain RestAPI GET request"""
        try:
            json_str = self.setup_class()
            if json_str['url4']['path']:
                url = constructURL.constURL(baseurl=json_str['url4']['baseurl'], 
                                            path=json_str['url4']['path'])
            else:
                url = json_str['url4']['baseurl']
            
            json = json_str['url4']['json']
                
            req = Api(url=url)
            
            resp = req.put(json=json)
            self.assertEqual(200, resp.status_code)
            response_type = resp.headers["content-type"]
            if re.search(r'json', response_type):
                response = resp.json()
            else:
                raise Exception("Response type is not json") 
        except Exception as e:
            print ("Exception occurred during test run", e)
                
        self.assertEqual("zion resident", response['job'])
        

if __name__ == '__main__':
    unittest.main()
    
    