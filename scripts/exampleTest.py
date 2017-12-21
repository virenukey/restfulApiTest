try:
    import unittest
    from TestData.TestData import TestData
    import setupTest
    from api import Api
    import constructURL
    import re
    import logging
    import sys
except ImportError as e:
    print ("Import of module in test failed", e)

logging.basicConfig(level=logging.DEBUG)
setuptest = setupTest.setupTest

class ExampleTest(unittest.TestCase):
    
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
        log = logging.getLogger('Running example test for REST GET Request')
        try:
            json_str = self.setup_class()
            log.debug("Constructing URL")
            if json_str['url1']['path']:
                url = constructURL.constURL(baseurl=json_str['url1']['baseurl'], 
                                            path=json_str['url1']['path'])
            else:
                url = json_str['url1']['baseurl']
                
            req = Api(url=url)
                        
            log.debug("Check response of GET Request")
            resp = req.get()
            print "Checking response type"
            print type(resp)
            self.assertEqual(200, resp.status_code)
        except Exception as e:
            print ("Exception occurred during test run", e)
            
        log.debug("Verifying response type is json")
        response_type = resp.headers["content-type"]
        if re.search(r'json', response_type):
            response = resp.json()
        else:
            sys.exit()
          
        log.debug("Finally verify test case expected output")        
        self.assertEqual("Afghanistan", response['RestResponse']['result'][0]['name'])
        

if __name__ == '__main__':
    unittest.main()
    
    