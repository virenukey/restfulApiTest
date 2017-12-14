import json
class TestData(object):
    def __init__(self, location, fileName):
        self.location = location
        self.fileName = fileName
     
    
    def data(self):
        try:
            test_data = open(self.location+self.fileName, 'r')
        except Exception as e:
            print ("Issue with test data file", e)
        json_str = json.load(test_data)
        return json_str
    

