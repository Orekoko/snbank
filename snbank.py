import json
import os
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
			os.remove('user_session.txt')
			break
			
		if banking_choice == '1':
			print('I will be needing some data from you, so as to create an account for you')
			numbers = '0123456789'
			account_name = input("Enter an account name of your choice (Its best to use your firstname and lastname): ")
			while True:
				try:
					opening_balance = float(input("\nEnter your opening amount. Just enter numbers only dont worry about putting the currency symbol, You'll get the type of account next: "))
				except ValueError:
					print('Wrong Input!')
					continue
				else:
					break
			account_type = input("\nEnter the account type, enter like eg: 'Naira Savings Account', eg: 'Dollar Current Account': ")
			account_email = input("\nEnter the email address you want to associated with your account: ")
			account_number = ''.join(random.choices(numbers, k=10))
			
			customer_file_data = []
			customer_banking_data = {
			    username: [
			        {
			            'Account Name': account_name,
			            'Opening Balance': opening_balance,
			            'Account Type': account_type,
			            'Account email': account_email,
			            'Account Number': account_number,
			        }
			    ],
			}
			if os.stat('customer.txt').st_size == 0:
				customer_file_data.append(customer_banking_data)
				with open('customer.txt', 'w') as file_obj:
					json.dump(customer_file_data, file_obj)
				print(customer_banking_data[username][0]['Account Name'] + ' this is your account number: ' + customer_banking_data[username][0]['Account Number'])
				print('So what do you want to do next? Enter 1, 2 or 3 to choose: ')
			else:
				with open('customer.txt') as file_obj:
					data = json.load(file_obj)
				data.append(customer_banking_data)
				with open('customer.txt', 'w') as file_obj:
					json.dump(data, file_obj)
				print(customer_banking_data[username][0]['Account Name'] + ' this is your account number: ' + customer_banking_data[username][0]['Account Number'])
				print('So what do you want to do next? Enter 1, 2 or 3 to choose: ')
			continue
		
		if banking_choice == '2':
			collect_acct_no = input('Enter your account number so as to fetch your account details (please ensure you enter correctly: ')
			check_account = {'Account Number': collect_acct_no,}
			
			with open('customer.txt') as file_obj:
				data = json.load(file_obj)
				found_flag = False
			for user_data in data:
				for user_data_key in user_data.keys():
					for user_details in user_data[user_data_key]:
						if check_account['Account Number'] in user_details.values():
							found_flag = True
							print('\nAccount Found ! See details below:')
							for key, value in user_details.items():
								print('\n' + key + ' : ' + str(value))
								
			if found_flag == False:
				print('Account Not Found! You can register a new one if you wish')
				continue
	