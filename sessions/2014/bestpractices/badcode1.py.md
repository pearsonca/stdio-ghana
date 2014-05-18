
class MyObject():

    def __init__(self, value):
        self.value = value

    def PrintValue(self):
        print(str(self.value))

class theObject():

    def __init__(self, V):
        self.worth = V

    def state_worth(self):
        print(str(self.worth))

def calculateWorth(the_list):
    sum = 0
    for item in the_list:
        value = item.value
        sum = sum + value
    return sum

my_list_of_objects = dict()

object1 = MyObject(10)
object2 = MyObject(25)
object3 = MyObject("-10")
object4 = theObject("$25,000")
object5 = MyObject(100)
object6 = theObject("25")
object7 = theObject("millions")
object8 = theObject("precious")

my_list_of_objects[10] = object1
my_list_of_objects[25] = object2
my_list_of_objects["-10"] = object3
my_list_of_objects["$25,000"] = object4
my_list_of_objects[100] = object5
my_list_of_objects["25"] = object6
my_list_of_objects["millions"] = object7
my_list_of_objects["precious"] = object8

for thekey in my_list_of_objects:
    obj = my_list_of_objects[thekey]
    if type(obj) is MyObject:
        obj.PrintValue()
    elif type(obj) is theObject:
        obj.state_worth()

