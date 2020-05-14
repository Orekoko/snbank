# snbank  

_______________________________________

###### This repo is an assignment for start.ng python 4th task.

## Overview
This task simulates a **Basic Banking System**

We are required to initially create two files 'customer.txt' and 'staff.txt'.

The ***customer.txt*** file will be empty prior to program run.

The ***staff.txt*** file will contain two staff details as show below:  
- *Username*  
- *Password* 
- *Email*
- *Fullname*

### On program run
	
The staff is provided with two options: 'Log in' or 'Close App'.  
So the staff has to log in with the correct staffname and password (which is in the staff.txt file).

### If the staff logs in sucessfully
	
A session file will be created to store the staff session (NB: this session file will be deleted when the staff logs out)

The staff is then presented with three options:  
- Create new bank Account  
- Check Account Details  
- Log out

#### If the staff selects 'create account'

The staff will be required to supply the following:  
- *Account name* 
- *Opening balance* 
- *Account type*  
- *Account Email*

Then the program will generate an account number for the staff.

After succesfully completing the creation of the account, the program will show the staff the generated account number

All the details above will then be saved in the customer.txt file

#### If the staff selects 'check account details'

The program will ask the staff to enter the account number 

Then the program will check the entered account number with the contents of the customer.txt file.  
+ If found, the program will fetch the details of the account and display it to the staff.  
+ If not found, the program will inform the staff and show him the options above to choose from.

#### Instead if the staff selects 'log out'

The program will delete the session file and return the staff to the initial program-run options (sign in and close app)

### Finally if the staff selects 'close app''

The program terminates


## The various files in the snbank repository

*The main python program file:* [snbank.py](https://github.com/Orekoko/snbank/blob/master/snbank.py)

*The staff.txt file:* [staff.txt](https://github.com/Orekoko/snbank/blob/master/staff.txt)

*The customer.txt file:* [customer.txt](https://github.com/Orekoko/snbank/blob/master/customer.txt)

*The README.md file:* [README.md](https://github.com/Orekoko/snbank/blob/master/README.md)

*The session file is always deleted when the staff logs out*

***PS: I uploaded an empty customer.txt file as per assignment instructions. When program is run, the appropriate data will be written to it***