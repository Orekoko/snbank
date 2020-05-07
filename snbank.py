import json
import random
from datetime import datetime


while True:
	print('Welcome to Start.ng-Python-Task4 Bank')
	print('Please enter 1 or 2 as shown below:')
	login_choice = input("\t1 - Staff Login\n\t2 - Close App\n\t\t")
	while (login_choice != '1') and (login_choice != '2'):
		login_choice = input('Enter the correct input (1 or 2): ')
		
	if (login_choice == '2'):
		break
		
	else:
		print('Welcome back! Login by entering your username and password below')
		username = input("Enter your username and press 'enter' key to proceed: ")
		password = input("Enter your password and press 'enter' key to proceed: ")
		
		with open('staff.txt', 'r') as file_obj:
			staff_details = json.load(file_obj)
		while (username != (staff_details['Staff 1']['Username']) or password != (staff_details['Staff 1']['Password'])) and (username != (staff_details['Staff 2']['Username']) or password != (staff_details['Staff 2']['Password'])) :
			username = input("Wrong username or password, Enter your username again: ")
			password = input("Enter your password : ")
	
	login = datetime.now()
	login = login.strftime("%d:%m:%Y %H:%M:%S")
	session_data = {
	    'Present User': username,
	    'Login Time': login,
	}
	with open('user_session.txt', 'w') as file_object:
		json.dump(session_data, file_object)
	
	print('Hello ' + username + '! what do you want to do? Enter 1, 2 or 3 to choose (see options below)')
		
	while True:
		banking_choice = input("\t1 - Create new bank account\n\t2 - Check Account Details\n\t3 - Logout\n\t\t")
		
		while (banking_choice != '1') and (banking_choice != '2') and (banking_choice != '3'):
			banking_choice = input('Wrong input enter 1, 2, or 3: ')
		if banking_choice == '3':
			break
			
		if banking_choice == '1':
			print('I will be needing some data from you, so as to create an account for you')
			numbers = '0123456789'
			customer_banking_data = {}
			customer_banking_data[username] = {}
			customer_banking_data[username]['Account name'] = input("Enter an account name of your choice (Its best to use your firstname and lastname): ")
			while True:
				try:
					customer_banking_data[username]['Opening Balance'] = float(input("\nEnter your opening amount. Just enter numbers only dont worry about putting the currency symbol, You'll get the type of account next: "))
				except ValueError:
					print('Wrong input!')
					continue
				else:
					break
			customer_banking_data[username]['Account Type'] = input("\nEnter the account type, enter like eg: 'Naira Savings Account', eg: 'Dollar Current Account': ")
			customer_banking_data[username]['Account email'] = input("\nEnter the email address you want to associated with your account: ")
			customer_banking_data[username]['Account Number'] = ''.join(random.choices(numbers, k=10))
			with open ('customer.txt', 'a') as file_object:
				json.dump(customer_banking_data, file_object)
			print(customer_banking_data[username]['Account name'].title() + ', this is your account number: ' + customer_banking_data[username]['Account Number'])
			print('So ' + username + ' what do you want to do next? enter 1, 2 or 3 to choose')
			continue
		if banking_choice == '2':
			account_number = input('Enter your account number: ')
			
			
		
	