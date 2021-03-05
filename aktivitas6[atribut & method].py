class student:
    """ A class representing a student"""
    def __init__ (self,a,b,c,d,e):
        self.full_name=a
        self.age=b
        self.gender=c
        self.height=d
        self.status=e
   
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_height(self):
        return self.height
    def get_status(self):
        return self.status
f = student ("Sadam Fauzi", 20, "male", 170, "Mahasiswa")
print (f.full_name)
print (f.get_age())
print (f.get_gender()) 
print (f.get_height())
print (f.get_status())