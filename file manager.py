import json
import os
class filemanager:
    file_name = 'students.json'
    @staticmethod
    def load_data(self):
        with open(self.file_name,'r') as file:
            data = json.load(file)
        return data
os.path.exists(filemanager.file_name)
with open(filemanager.file_name,'r') as file:
 json.load(file)
def save_data(data):
  with open(filemanager.file_name,'w') as file:
   json.dump(data,file,indent=4)