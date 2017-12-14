import unittest
from TestData.TestData import TestData
import setupTest
from api import Api
import re

setuptest = setupTest.setupTest

class Testcase2(unittest.TestCase):
        
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
        """Verify RestAPI GET request with input parameters"""
        try:
            json_str = self.setup_class()
            req = Api(json_str['url2']['url'])
            params = json_str['url2']['params']
            resp = req.get(params)
                    
            response_type = resp.headers["content-type"]
            if re.search(r'json', response_type):
                response = resp.json()
                
        except Exception as e:
            print ("Exception occurred during test run", e)
       
        self.assertEqual(200, resp.status_code)
      
                    
if __name__ == '__main__':
    unittest.main()
    
    