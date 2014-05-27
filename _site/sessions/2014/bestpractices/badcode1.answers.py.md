
class MyObject():
    def __init__(self, value):
        self.value = value
    #object method same naming conventions as object
    def PrintValue(self):
        print(str(self.value))

#this object uses a different naming convention than MyObject
class theObject():
    #use of V here is not a flaw.  local use, never referenced again
    def __init__(self, V):
        self.worth = V
    #object method uses different naming convention than PrintValue
    def state_worth(self):
        print(str(self.worth))

#this function is NEVER called
#function has odd naming convention for Python, but acceptable as long as consistent
#might be useful to describe what kind of list it is in the variable name
def calculateWorth(the_list):
    sum = 0
    for item in the_list:
        value = item.value
        sum = sum + value
    return sum

#confusing variable name.  It isn't a list, it is a dictionary
my_list_of_objects = dict()

#variable names are vague. No way of telling whether object3 is a MyObject or theObject
object1 = MyObject(10)
object2 = MyObject(25)
object3 = MyObject(-10)
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

#thekey uses a different naming convention than the variables above
for thekey in my_list_of_objects:
    obj = my_list_of_objects[thekey]
    if type(obj) is MyObject:
        obj.PrintValue()
    elif type(obj) is theObject:
        obj.state_worth()
#code defensively.  what if a maintenance task adds new object? There should be a default "else" case

#refactor.  PrintValue() and state_worth() do the same thing.  If you rename both to print_var() no if else needed
#some MyObjects are integers and theObjects are strings.  could these objects have more descriptive names?