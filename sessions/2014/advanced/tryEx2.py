# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as err:
      print ("The argument does not contain numbers\n", err)

# Call above function here.
temp_convert("xyz");
