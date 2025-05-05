class Employee:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.email=self.fname+self.lname+'@gmail.com'
    def full_name(self):
        return self.fname+self.lname
    @classmethod
    def cm(cls,strr):
        fname,lname,age=strr.split(",")
        return cls(fname,lname,age)
    