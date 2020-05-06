while True:
	print('Welcome to Start.ng-Python-Task4 Bank')
	print('Please enter 1 or 2 as shown below:')
	login_choice = input("\t1 - Staff Login\n\t2 - Close App\n\t")
	while (login_choice != '1') and (login_choice != '2'):
		login_choice = input('Enter the correct input (1 or 2): ')
	if (login_choice == '1') or (login_choice == '2'):
		break