# monica and megan climbing class

#How to make default variable in class
class climbing:
    def __init__(self, location='yosemite', rock='hard', height=100, grade=5.7):
# makes it a module because the attributes are defined as
# set values, modules already build the object and you can't change it
# *args and **kargs to 'turn off and turn on' different variables
        self.location = location
        self.rock = rock
        self.height = height
        self.grade = grade

#Only runs modules if it is called, i.e. when you call site1.pitches()
#to make pitches an atrribute, you would
    def pitches(self):
        pitches = self.height/170 #170 m rope length
        return pitches

    def hours(self):
        hours = self.pitches() * (self.grade-5)*2
        return hours



site1 = climbing("yosemite","granite", 3000, 5.11)
print('location',site1.location)
print('number of pitches',site1.pitches())
print('hours to climb', site1.hours())

site2 = climbing("red river gorge","sandstone", 100, 5.14)
print('location',site2.location)
print('number of pitches',site2.pitches())
print('hours to climb', site2.hours())

site3 = climbing("black cliffs","basalt", 50, 5.6)
print('location',site3.location)
print('number of pitches',site3.pitches())
print('hours to climb', site3.hours())
