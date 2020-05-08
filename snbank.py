''' Start.ng Python 4th Task 'A Basic Banking System'
by Oreoluwa Adetimehin slackID - orekoko '''

# the python modules used
import json
import os
import random
from datetime import datetime


# main program
while True: # main program loop
	print('*** WELCOME TO START.NG PYTHON-TASK4 BANK LTD ***')
	print('Please enter 1 or 2 as shown below:')
	login_choice = input("\t1 - Staff Login\n\t2 - Close App\n\t\t")
	# ensures user enters correct input
	while (login_choice != '1') and (login_choice != '2'):
		login_choice = input('Please enter the correct input (1 or 2): ')
	
	# if user selects close app, terminate the program	
	if (login_choice == '2'):
		break
		
	else: # if user selects 'staff login'
		print('\nWelcome back! Login by entering your username and password below')
		# collect username and password
		username = input("Enter your username and press 'enter' key to proceed: ")
		password = input("Enter your password and press 'enter' key to proceed: ")
		
		# verify the username and password is in staff.txt
		with open('staff.txt', 'r') as file_obj:
			staff_details = json.load(file_obj)
		while (username != (staff_details['Staff 1']['Username']) or password != (staff_details['Staff 1']['Password'])) and (username != (staff_details['Staff 2']['Username']) or password != (staff_details['Staff 2']['Password'])) :
			username = input("\nWrong username or password, Enter your username again: ")
			password = input("Enter your password : ")
	
	# create the session file if user logs in succesfully
	login = datetime.now()
	login = login.strftime("%d:%m:%Y %H:%M:%S")
	session_data = {
	    'Present User': username,
	    'Login Time': login,
	}
	with open('user_session.txt', 'w') as file_object:
		json.dump(session_data, file_object)
		
	# user has logged in show banking options
	print('\nHello ' + username + '! what do you want to do? Enter 1, 2 or 3 to choose (see options below):')
		
	while True:
		banking_choice = input("\t1 - Create new bank account\n\t2 - Check Account Details\n\t3 - Logout\n\t\t")
		
		# ensure proper input
		while (banking_choice != '1') and (banking_choice != '2') and (banking_choice != '3'):
			banking_choice = input('Wrong input please enter 1, 2, or 3: ')
			
		# if user selects 'log out' return the user to sign-in prompt
		if banking_choice == '3':
			os.remove('user_session.txt')
			print()
			break
		
	# for if user selects create account	
		if banking_choice == '1':
			print('\nI will be needing some data from you, so as to create an account for you!\n')
			numbers = '0123456789'
			account_name = input("Enter an account name of your choice (Its best to use your firstname and lastname): ")
			
			# endure the balance entered is a valid number input
			while True:
				try:
					opening_balance = float(input("\nEnter your opening amount. Just enter numbers only dont worry about putting the currency symbol or comma (you'll be asked for the type of account next): "))
					opening_balance = '{:.2f}'.format(opening_balance)
				except ValueError:
					print('Wrong Input!')
					continue
				else:
					break
			account_type = input("\nEnter the account type, enter like eg: 'Naira Savings Account', eg: 'Dollar Current Account': ")
			account_email = input("\nEnter the email address you want to be associated with your account: ")
			# generate a 10-digits account number randomly from the numbers variable
			account_number = ''.join(random.choices(numbers, k=10))
			
			customer_file_data = [] # to collect all the customer_banking_data 
			customer_banking_data = {
			    username: [
			        {
			            'Account name': account_name.title(),
			            'Opening Balance': opening_balance,
			            'Account Type': account_type.title(),
			            'Account email': account_email,
			            'Account Number': account_number,
			        }
			    ],
			}
			
			# check if the customer.txt is empty, if yes, append customer_banking_data to the customer_file_data list and json dump it in customer.txt
			if os.stat('customer.txt').st_size == 0:
				customer_file_data.append(customer_banking_data)
				with open('customer.txt', 'w') as file_obj:
					json.dump(customer_file_data, file_obj)
				# show the user the account number
				print('\n>>>\t'+ customer_banking_data[username][0]['Account name'] + ', this is your account number: ' + customer_banking_data[username][0]['Account Number'])
				print('\nSo what do you want to do next? Enter 1, 2 or 3 to choose: ')
			
			# if customer.txt is not empty at time of program run, json load the data from it in variable 'data', append the customer_banking_data to it and json dump it back
			else:
				with open('customer.txt') as file_obj:
					data = json.load(file_obj)
				data.append(customer_banking_data)
				with open('customer.txt', 'w') as file_obj:
					json.dump(data, file_obj)
				# show the user the account number
				print('\n' + customer_banking_data[username][0]['Account name'] + ' this is your account number: ' + customer_banking_data[username][0]['Account Number'])
				print('\nSo what do you want to do next? Enter 1, 2 or 3 to choose: ')
			continue
		
		# if user selects 'check account details'
		if banking_choice == '2':
			collect_acct_no = input('\nEnter your account number so as to fetch your account details (please ensure you enter correctly: ')
			check_account = {'Account Number': collect_acct_no,}
			
			# json load the customer.txt file and check if the account number is in it, if yes, print the specific user details
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
								print('\n\t' + key + ' : ' + str(value))
							print('\nSo what do you want to do next? Enter 1, 2 or 3 to choose:')
							continue
			
			# if the account number is not in the customer.txt, inform the user					
			if found_flag == False:
				print('\nAccount Not Found! You can register a new one if you wish. Choose by entering 1, 2 or 3 as shown below')
				continue