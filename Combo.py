#!/usr/bin/env python

#20/07/2019
#basic combolist generator
#Used for pentesting, enables a user to generate a list of emails with different passwords that 
#can be used to pentest your networks user accounts
#to do - add arg parse, split first/last name

import sys 

ver = "0.1.2"
print("Basic combolist generator version {}".format(ver))
print("Created by github.com/nullsc \n")

VERBOSE = False #print out info
SEPARATOR = ":" #the part between username & password

if(len(sys.argv) < 3):
    print("Usage: combo.py [email_list] [password_list] [-v for verbose (optional)]")
    sys.exit(1) #error

if(len(sys.argv) == 4):
    if(sys.argv[3] == "-v"):
        print("Verbose mode on")
        VERBOSE = True
    else:
        print("Verbose mode off")
        #VERBOSE = False

emailList = sys.argv[1]
passList = sys.argv[2]
outputFile = "output.txt" #where the data will be written to


print("Loaded email list: {}".format(str(emailList)))
print("Loaded pass list: {} \n".format(str(passList)))

with open(emailList, 'rt') as file:
     for email in file:
         with open(passList, 'rt') as file2:
            for password in file2:
                if(VERBOSE): print(email.strip() + SEPARATOR + password.strip()) #print out to cmd
                with open(outputFile, 'at') as z:
                    z.write(email.strip() + SEPARATOR + password.strip() + "\n")


#with closes files automatically

print("List generated! in {}".format(outputFile))
