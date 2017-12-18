import json

class TestData(object):
    def __init__(self, location, fileName):
        self.location = location
        self.fileName = fileName
   
  
    def data(self):
        try:
            fileName = self.location+'\\'+self.fileName
            test_data = open(fileName, 'r')
        except Exception as e:
            print ("Issue with test data file", e)
        json_str = json.load(test_data)
        test_data.close()
        return json_str
    
    
            
    

