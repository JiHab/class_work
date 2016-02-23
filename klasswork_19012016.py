
muld_name = 'Fox Mulder'
scull_name = 'Dana Scully'
import random

class User (object):
    def __init__(self, *args):

        self.name = args[0]
        try:
            self.age = args[1]
        except:
            a=1
            #print('no age')
    def __str__(self):
        return str(self.name)

    def money(self):
        return None

class Employee(User):
    def __init__(self, name, sallary):
        User.__init__(self,name)
        self._money = sallary

    def __str__(self):
        return str(self.name) + ' ' + str(self._money)

    def money(self):
        return self._money

class Freelanser(User):
    def __init__(self, name, hours, rate):
        User.__init__(self, name)
        self.hours = hours
        self.rate = rate

        #Employee.__init__(self,name)
        #Employee.money = self.hours * self.rate
    def __str__(self):
        return str(self.name) + ' h' + str(self.hours) + ' r' + str(self.rate)# + ' '+str(Employee.money)

    def money(self):
        return self.rate * self.hours


muld = User(muld_name)

scull = Employee(scull_name, 10000)

scull2 = Freelanser(scull_name, 10, 100)

print(muld.money())
print(scull.money())
print(scull2.money())
import string
#def r_name():
  #  return string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase))] + string.ascii_lowercase[random.randint(0, len(string.ascii_uppercase))] for)

print(str(string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase))] for _ in range (10)))