import json
from numpyEncoder import NpEncoder
class ResultLog:
    def __init__(self, path):
        self.path = path
        pass

    def add(self, dict_result):
        dict_result = json.dumps(dict_result, cls=NpEncoder)
        self.write(path = self.path,text =  dict_result)
        print("log done!!!")
        return None

    def write(self, path, text):
        f = open(path, 'a')
        f.write(text + "\n")
        f.close()
        return None