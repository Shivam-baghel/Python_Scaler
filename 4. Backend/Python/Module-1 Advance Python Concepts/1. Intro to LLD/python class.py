


from numpy import roll


class student():
    
    school = "APS"
    name="hello"
    className: str
    
    def __init__(self) -> None:
        self.rollno = None
        
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getRoll(self):
        return self.rollno
    
    def setRoll(self,roll):
        self.rollno = roll
        
    @classmethod
    def check(cls):
        print(cls.name)
    

stu = student()
stu.setName("Shivam")
print(stu.getName())

stud = student()
stud.setName("sachin")
stud.setRoll(32)
print(stud.getName())
print(stud.getRoll())