
import json
students=[
  {
     "roll_no":"101",
     "name":"ahmad",
     "age":"18"
  },
  {
     "roll_no":"102",
     "name":"ahmad",
     "age":"19"
  }
]
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("json file created successfully")








