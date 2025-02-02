"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os

print(os.getcwd())
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
f = open("foo.txt", "r")#"/Users/ramsesbermudez/Documents/CS22/Intro-Python-I/src/foo.txt", "r")
print(f.read())
f.close()
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
# YOUR CODE HERE
e = open("bar.txt", "w")
e.write("hello this is hard \n almost midnight \n need sleep")
e.close()
