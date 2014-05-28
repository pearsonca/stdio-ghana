class IntegerObject():

    def __init__(self, value):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        v = int(value)
        if v >= 10:
            print("Too big, setting to 9.")
            v = int(9)
        self.value = v

    def print_value(self):
        print(str(self.value))


class StringObject():

    def __init__(self, s):
        self.value = str(s)

    def get_value(self):
        return self.value

    def set_value(self, s):
        s = str(s)
        if len(s) >= 10:
            s = s[0:9]
            print("Too big, truncating to " + s)
        self.value = str(s)

    def print_value(self):
        print(str(self.value))


def total_value(list_of_integer_objects):
    sum = 0
    for int_obj in list_of_integer_objects:
        value = int_obj.get_value()
        sum = sum + value
    return sum


def print_sorted_list(list_of_integer_objects):
#    the line below actually sorts the list, rather than just print it sorted
#    list_of_integer_objects.sort(key=lambda x: x.value, reverse=True)
    new_list = sorted(list_of_integer_objects, key=lambda x: x.value, reverse=True)
    for int_obj in new_list: #list_of_integer_objects:
        int_obj.print_value()

#replaces all loops to print lists
def print_object_list(object_list):
    for obj in object_list:
        obj.print_value()

int_object_list = list()
str_object_list = list()
cheese_list = ["Tilsit", "Stilton", "Emmental", "Cheshire"]

for i in range(1,5):
    int_object_list.append(IntegerObject(i))

for cheese in cheese_list:
    str_object_list.append(StringObject(cheese))

#for int_object in int_object_list:
#    int_object.print_value()

#for str_object in str_object_list:
#    str_object.print_value()

#replace with this!
print_object_list(int_object_list)
print_object_list(str_object_list)


print(total_value(int_object_list))
print_sorted_list(int_object_list)

#for int_object in int_object_list:
#    int_object.print_value()

#and this
print_object_list(int_object_list)


int_object_list[0].set_value(10)
#directly assigning value in object bypasses validity check
int_object_list[1].value = 1000
#directly assigning value in object bypasses validity check
int_object_list[2].value = "Cheddar"

str_object_list[0].set_value("Wensleydale")
#directly assigning value in object bypasses validity check
str_object_list[1].value = "Norwegian Jarlsberg"
#directly assigning value in object bypasses validity check
str_object_list[2].value = 5


#for int_object in int_object_list:
#    int_object.print_value()

#for str_object in str_object_list:
#    str_object.print_value()

print_object_list(int_object_list)
print_object_list(str_object_list)
