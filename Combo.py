#!/usr/bin/env python

#20/07/2019
#basic combolist generator
#Used for pentesting, enables a user to generate a list of emails with different passwords that 
#can be used to pentest your user accounts

import sys 

ver = "0.1.1"
print("Basic combolist generator version {}".format(ver))
print("github.com/nullsc")

if(len(sys.argv) < 3):
    print("Usage: combo.py [email_list] [password_list]")
    sys.exit(1) #error

emailList = sys.argv[1]
passList = sys.argv[2]
outputFile = "output.txt"

print("Loaded email list: {}".format(str(emailList)))
print("Loaded pass list: {} \n".format(str(passList)))

with open(emailList, 'rt') as file:
     for email in file:
         #print(email, end='')
         with open(passList, 'rt') as file2:
            for password in file2:
                print(email.strip() + ":" + password.strip())
                with open(outputFile, 'at') as z:
                    z.write(email.strip() + ":" + password.strip() + "\n")
                pass
            pass

file.close()
z.close()
file2.close()

print("List generated! in {}".format(outputFile))
print("Complete")

