class Dog:
    # This is the constructor for the class. It is called whenever a Dog
    # object is created. The reference called "self" is created by Python
    # and made to point to the space for the newly created object. Python
    # does this automatically for us but we have to have "self" as the first
    # parameter to the __init__ method (i.e. the constructor).
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

     # This is an accessor method that returns the speakText stored in the
     # object. Notice that "self" is a parameter. Every method has "self" as its
     # first parameter. The "self" parameter is a reference to the current
     # object. The current object appears on the left hand side of the dot (i.e.
     # the .) when the method is called.
    def speak(self):
        return self.speakText

    # Here is an accessor method to get the name
    def getName(self):

        return self.name

    # This is another accessor method that uses the birthday information to
    # return a string representing the date.
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

    # This is a mutator method that changes the speakText of the Dog object.
    def changeBark(self,bark):
        self.speakText = bark

    def __add__(self,otherDog):
        print("Puppy name is:{0}".format(otherDog.getName()+" " +self.getName()))
newSpeakText = "WOOFY WOOFY WOOFY"
# CREATE A DOG OBJECT
dog = Dog(name="Mesa", month=9, day=30, year=2020, speakText="WOOOF")
print("Below is example of class accessor")
# JUST ACCESSING THE METHOD , IRRESPECTIVE OF MULTIPLE ACCESS
# SAME VALUE IS PRINTED
print("Birth date of Dog {0}".format(dog.birthDate()))
print("Below is example of class modifier")
print("Bark text before modifying:{0}".format(dog.speak()))
dog.changeBark(newSpeakText)
print("Modifying to {0}".format(newSpeakText))
print("Bark text after modifying:{0}".format(dog.speak()))


dog1 = Dog(name="Mesa", month=9, day=30, year=2020, speakText="WOOOF")
dog2 = Dog(name="Busa", month=9, day=30, year=2020, speakText="WOOOF")

print ("Name of Dog1 is {0} and of Dog2 is {1}".format(dog1.getName(),dog2.getName()))
dog1.__add__(dog2)