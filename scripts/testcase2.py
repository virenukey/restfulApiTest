import unittest
from TestData.TestData import TestData
import setupTest
from api import Api
import constructURL
import re

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
            if json_str['url1']['path']:
                url = constructURL.constURL(baseurl=json_str['url1']['baseurl'], 
                                            path=json_str['url1']['path'])
            else:
                url = json_str['url1']['baseurl']
                
            req = Api(url=url)
            
            resp = req.get()
            self.assertEqual(200, resp.status_code)
            response_type = resp.headers["content-type"]
            if re.search(r'json', response_type):
                response = resp.json()
        except Exception as e:
            print ("Exception occurred during test run", e)
                
        #self.assertEqual("Afghanistan", response['RestResponse']['result'][0]['name'])
        

if __name__ == '__main__':
    unittest.main()
    
    