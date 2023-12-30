class Employee:
    company='TESLA'
    ceo='elon Musk'
    def insert_member(self,name,age,sal,eid):
        self.name=name
        self.age=age
        self.sal=sal
        self.eid=eid

mohan=Employee()
jashu=Employee()



Employee.insert_member(mohan,'mohan',21,50000,300)
Employee.insert_member(jashu,'jashu',21,50000,300)
