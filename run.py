#########################################################################
# This program runs a simple java file. It doesn't need to be in        #
# package.                                                              #
# Note: Don't put ".java" at the end                                    #
#########################################################################

# imports
import os, sys

# name of the java file
name = sys.argv[1]

# runs the file
os.system(f'java {name}.java')