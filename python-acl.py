import os

from posix import aclexec

def main():

#Get the absololute path to the script.

script_path = os.patha.abspath(__file__)

# Set the owner to read, write, and execute the script 

os.chmod(script_path, 0755)

# Set the group to read and execute the script 

os.chmod(Script_path, 0550)
