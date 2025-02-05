
#Importing datetime module 
#for generating date and time

from datetime import datetime

#Importing the random module to
#generate random numbers

import random

#Importing regex module for validation

import re

#Generating the time and date for login

date_and_time=datetime.now()
date_formatted=date_and_time.strftime("%d-%m-%Y")
time_formatted=date_and_time.strftime("%H:%M")

#Using dictionary as a makeshift database for 
#the atm mockup

User_password_database={
'0066327651' : ['Seyi', 'Taylor', 'seyi@ymail.com', 'passwordSeyi', 0]
}

trial=3

#Obtaining the currrent date
date_and_time=datetime.now()
date_formatted=date_and_time.strftime("%d-%m-%Y")
time_formatted=date_and_time.strftime("%H:%M")


#A function for invalid options
def invalid_option(func):

		print('You have not selected a valid option')
		print('These are the available options')
		func()


#Function for exiting the program
def exit_func():
		print('x'*20)
		print('Goodbye')
		exit()

	 

#The main function that sets the pace for
#the program.
def init():

	print('+'*20)
	print('Welcome to Bank Python')
	print('Press')
	print('1, To login if you have account already')
	print('2, To register,if you  do not have an account')
	print('3, To file a complaint or feedback')
	print('4, To exit')
	option= int(input('Please select an option: \n'))
	if option == 1:
		login()
	elif option == 2:
		register()
	elif option == 4:
		exit_func()
	elif option == 3:
		print()
		print()
		print('You need to have an account to give a feedback')
		print('Select register or login if you have an account already')
		init()
	else:
		invalid_option(init)

#Function for inputting first name
def first_name():

	first1=input('First name: \n')
	first=validate_name(first1)
	return first1

#Function for inputing Last name
def last_name():
	last1=input('Last name: \n')
	last=validate_name(last1)
	return last1


#Function for inputting password
def password_func():

	password=input('Password: \n')
	password1=input('Confirm password: \n')
	validate_password(password, password1)
	return password

#Function for inputting emails
def email_func():

	email=input('Email: \n')
	validate_email(email)
	return email

#Function for validating name input
def validate_name(name):

	if not re.match(r'^[A-Za-z]+$', name):
		print('Invalid name')
		first_name()

#Function for validating password
def validate_password(password, password1):

	

	if password != password1:
		print('Password does not match')
		password_func()

#Function for validating email
def validate_email(email):

	if not re.match(r'^[a-z-]+@[a-z]+.com$', email):
		print('Invalid email, small letters and underscore allowed only')
		email_func()
	else:
		for accounts in User_password_database:
			if email in User_password_database[accounts]:
				print('We have this record already')
				print('This is your account number ', accounts)
				print('1, Login')
				print('2, Register with another email')
				option=int(input('3, Exit \n'))
				if option==1:
					login()
				elif option==2:
					email_func()
				elif option==3:
					exit_func()
				else:
					invalid_option(validate_email(email))
					
		
#Function that presents option after registration
def option_after_registration():

	print('Deposit into account now')
	print('1, yes')
	print('2, Maybe later')
	option=int(input('Please select an option: \n'))
	if option ==1:
		print('-'*20)
		cash_deposit()
	elif option == 2:
		exit()
	else:
		invalid_option(option_after_registration)


#Function that generates password and adds user
#to database 
def register():

	print('o-o'*20)
	global account_number
	account_number=str(random.randint(11111111,9999999999)).zfill(10)
	User_password_database[account_number]=[first_name(), last_name(), email_func(), password_func(), 0]
	print('Thanks for choosing to bank with us,', User_password_database[account_number][1])
	print('Here is your account number,', account_number)
	option_after_registration()




	
		
#Function that presents option when email is incorrect
def incorrect_email():

				
				print('1, Input email again')
				print('2, register')
				print(3, exit)
				option_1=int(input('Please select an option:'))
				if option_1 == 1:
					input_email(message)
				elif option_1 == 2:
					register()
				elif option_1 == 3:
					exit_func()
				else:
					invalid_option(incorrect_email)
				


#Function to find email in database(dictionary)					
def input_email(message):

		
		email=input('Input email: ')
		global accounts
		for accounts in User_password_database:
			if email in User_password_database[accounts]:
								
				the_message=message
				break
		if the_message:
			print(message)
		else:
			print('We do not have this record')
			incorrect_email()
					

	
#Logic for function after incorrect password/password help
#Using selected option from 'else_options_invalid_password' function
def incorrect_password(option):
	if option == 1:
		global message
		message='An email has been sent to you'
		input_email(message)


	elif option == 2:
		exit_func()
	elif option == 3:
		login()
	else:
		print(else_options_invalid_password)



#Logic for function after incorrect account number/account number using options
#from 'options_account_number' function
def no_record_for_account_number(option):

	if option == 1:
		global message
		message='Your account number is:'
		input_email(message)
		print(accounts)
		print()
		print('You may proceed to login, now')
		login()
		
	elif option == 2:
		register()
	elif option == 3:
		exit_func()
	elif option == 4:
		login()
		
	else:
		invalid_option(options_account_number())

#options after incorrect account number/Account number help	
def options_account_number():

			
			print('Forgot account number? to retrieve, press 1')
			print('Register, to get an account number, press 2')
			print('To exit, press 3')
			option=int(input('Go back to input email, press 4 \n'))
			no_record_for_account_number(option)

#Options after incorrect password/password help
def else_options_invalid_password():

				print('Forgotten password? press 1')
				print('To exit, press 2')
				option=int(input('Try again?,press 3 (you have {} trial(s) left ) \n'.format(trial)))
				incorrect_password(option)





#Function for login
def login():


	print()
	print("|"*20)
	global account_number
	account_number=input("What is your account number? (Unsure what to type?, press 1, for help) \n")
	for account_numbers in User_password_database:
		if account_numbers==account_number:
			account_number=account_numbers
			password=input("What is your password? (Forgotten password?, press enter,Extra options would be displayed) \n")
			if password == User_password_database[account_number][3]:
				print('='*20)
				print('Date: ', date_formatted)
				print('Time: ', time_formatted)
				print('Welcome', User_password_database[account_number][1])
				print()
				print()
				print('These are the available options:')
				bank_operation()
				exit_func()
		
			else:
				print('Incorrect password')
				global trial
				trial =trial-1
				if trial >= 0:
					else_options_invalid_password()
					exit_func()
				else:
					print ('You have exceeded your limit for this session')
					exit_func()
		elif account_number==str(1):
			options_account_number()
			exit_func()
			
	print('We do not have this record')
	options_account_number()


#Function that presents option for bank
#operation
def bank_operation():
	
	
	selected_option=int(input("""
	1, Withdrawal
        2, Cash Deposit
        3, Complaint
	4, Check balance
	5, Exit
	6, Logout
	"""
	))
	if selected_option==1:
		withdrawal()
	elif selected_option==2:
		cash_deposit()
	elif selected_option==3:
		complaint()
	elif selected_option==4:
		check_balance()	
	elif selected_option==5:
		exit_func()
	elif selected_option==6:
		login()
	else:
		print('Invalid option')

#Function that is called after esch bank operation
def next_step_after_operation():
	print('Perform another operation or exit')
	bank_operation()



#Function called when user wants to make a complaint
def complaint():
	input('What issue will you like to report? ')
	print('Thank you for contacting us' )
	next_step_after_operation()

#Function called when user wants to make a withdrawal
def withdrawal():
	amount_withdrawn=int(input('How much would you like to withdraw: '))
	if amount_withdrawn <= User_password_database[account_number][4]:
		print('Take your cash')
		User_password_database[account_number][4]=User_password_database[account_number][4]-amount_withdrawn
	else:
		print('Insufficient funds')
	
	next_step_after_operation()
#Function called when user wants to make a cash deposit
def cash_deposit():
	amount_deposited=int(input('How much would you like to deposit? '))
	User_password_database[account_number][4]=User_password_database[account_number][4]+amount_deposited
	print('You deposited ₦{}'.format(amount_deposited))
	next_step_after_operation()

#Function called when user wants to make a check balance
def check_balance():
	print('Dear ', User_password_database[account_number][0],  User_password_database[account_number][1])
	print('You have a balance of ₦',  User_password_database[account_number][4])
	next_step_after_operation()


#Calling the  init function
init()
           
        