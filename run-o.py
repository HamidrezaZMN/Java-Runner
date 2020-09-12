#########################################################################
# This program uses the given argument so it only runs one java file.   #
# But it means that the running java file is gonna use another java     #
# in th package                                                         #
# Note: Don't put ".java" at the end                                    #
#########################################################################

# imports
import os, sys

# full path of the current py file
rpath = os.path.realpath(__file__)
rpath = rpath.split('\\')

# declaring package and the main java file
package = rpath[-2]
main_class = sys.argv[1]

# going up one directory
parent = os.path.dirname(os.getcwd())
os.chdir(parent)

# compile and running the package
os.system(f'javac -cp . {package}/{main_class}.java')
os.system(f'java -cp . {package}/{main_class}.java')

# going back to the package
os.chdir(package)

# deleting all the class files
for file in os.listdir():
	if file.endswith('.class'):
		os.system(f'del {file}')
		
