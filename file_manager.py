import json
class Manager:
    def __init__(self,filename="data.json"):
        self.filename = filename
def load_data(self):
    try:
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return[]
    except Exception as e:
        print("Error: ", e)
        return []
def save_data(self,data):
    try:
        with open(self.filename, "w") as file:
             json.dump(data, file, indent=4)
        print("Data saved successfully")
     except Exception as e:
         print("Error saving data:",e)

