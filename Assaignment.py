class attendence_management():
    def __init__(self):
        self.clerks=""
        self.teachers=""
    def staff_attendence(self):
        print(self.clerks)
        print(self.teachers)


a1=attendence_management()
a1.clerks="It will take clerk attendence"    
a1.teachers="It will take teachers attendence"   
a1.staff_attendence() 

class overtime(attendence_management):
    def __init__(self):
        self.teachers_overtime=""
        self.clerks_overtime=""
    def overtime_attendence(self):
        print(self.teachers_overtime)
        print(self.clerks_overtime) 

a2=overtime()
a2.teachers_overtime="It will check Teacher's overtime"
a2.clerks_overtime="It will check Clerk's overtime"
a2.overtime_attendence()        
