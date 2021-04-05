from datetime import datetime
date_and_time=datetime.now()
date_formatted=date_and_time.strftime("%d-%m-%Y")
time_formatted=date_and_time.strftime("%H:%M")
name=input("What is your name? \n")
allowedUsers  =['Seyi', 'Mike', 'Love']
allowedPassword=['passwordSeyi', 'passwordMike', 'passwordLove']
if (name in allowedUsers):
    password=input("Your password? \n")
    userId=allowedUsers.index(name)
    if (password ==allowedPassword[userId]):
        print('Date: ', date_formatted)
        print('Time: ', time_formatted)
        print('Welcome %s ' %name)
        print('these are the available options:')
        print('1, Withdrawal')
        print('2, Cash Deposit')
        print('3, Complaint')
        
        selectedOption=int(input('please select an option: '))
        
        if (selectedOption == 1):
            print('you selected %s' %selectedOption)
            input('How much would you like to withdraw: ')
            print('Take your cash')
        elif (selectedOption == 2):
            print('you selected %s' %selectedOption)
            Balance=input('How much would you like to deposit? ')
            print('Current balance: ₦%s' %Balance)
           
        elif (selectedOption == 3):
            print('you selected %s' %selectedOption)
            input('What issue will you like to report? ')
            print('Thank you for contacting us' )
        else:
            print('Invalid option selected, please try again')
            
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')
