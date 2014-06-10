try:
	fh = open("testfile", "w")
	fh.write("this is my test file for exception handling")
except IOError:
	print ("Error: can\'t find file or read data")
else:
	print ("Written content in the file successfully")
	fh.close()
