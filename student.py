class student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,'roll_no': self.roll_no
        }