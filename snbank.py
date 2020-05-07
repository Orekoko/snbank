import json


while True:
	print('Welcome to Start.ng-Python-Task4 Bank')
	print('Please enter 1 or 2 as shown below:')
	login_choice = input("\t1 - Staff Login\n\t2 - Close App\n\t")
	while (login_choice != '1') and (login_choice != '2'):
		login_choice = input('Enter the correct input (1 or 2): ')
		
	if (login_choice == '2'):
		break
		
	while (login_choice == '1'):
		print('Welcome back! Login by entering your username and password below')
		username = input("Enter your username and press 'enter' key to proceed: ")
		password = input("Enter your password and press 'enter' key to proceed: ")
		
		with open('staff.txt', 'r') as file_obj:
			staff_details = json.load(file_obj)
		while (username != (staff_details['Staff 1']['Username']) or password != (staff_details['Staff 1']['Password'])) and (username != (staff_details['Staff 2']['Username']) or password != (staff_details['Staff 2']['Password'])) :
			username = input("Wrong username or password, Enter your username again: ")
			password = input("Enter your password : ")
		else:
			print('xxxxxxxcccccxxxx')
			
		
	