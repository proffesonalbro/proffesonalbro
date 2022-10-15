#packages - 
from ast import Return, While


#def -
def loggedin():
    print("logged in")

#l or s - 
print("Select an option (l) for login  or  (s) for sign in ")
answer = input("").lower()

#signing in - 
if answer == "s":
    global u
    global p
    u = input("create a username: ")
    p = input("create a complex password: ")
    
    print("Account created successfully!")
    print("\nSelect an option (l) for login  or  (s) for sign in ")
    answer = input("")

#logging in - 
if answer == "l":
    global ul
    global lp
    ul = input("Enter the username: ")
    lp = input("Enter the user password: ")

    loggedin()
    
#welcome message - 
print('welcome' + "|" + ul)
    
#while true statement -
while True:
    print('what do you want to access? (current bank balance, your password, glod loan, home loan.)')
    dollar = 300,000,000,000 

    A1 = input("")
    
    #bank balance - 
    if A1 == 'current bank balance':
        print("you have only " + str(dollar) + "$")
        
    # password show - 
    if A1 == 'your password':
        print(lp)

    #glod loan - 
    if A1 == 'glod loan':
        A2 = input('how much money you need for buy glod? ')
        print('\nokay we will send ' + str(A2) + ' money to your bank account.')
        A3 = input('in which form you need the money please enter(in dollar / in rupee)? ')
        print('\nokay we will send the money in ' + A3)
        A9 = input('now, please enter your ATM Card Number. ')
        A10 = input('enter your adhar card number. ')
        A11 = input('enter your voter card number. ')
        a2 = input('enter your PAN card number. ')
        print('here is your detail - ' )
        print('PAN card number - ' + str(a2))
        print('ATM card number - ' + str(A9))
        print('athar card number - ' + str(A10))
        print('voter card number - ' + str(A11))

    #home loan - 
    if A1 == 'home loan':
        A4 = input('how much money you need for buy a house? ')
        print('\nokay we will send ' + str(A4) + ' money to your bank account.')
        A5 = input('in which form you need the money please enter(in dollar / in rupee)? ')
        print('\nokay we will send the money in ' + A5)
        A6 = input('now, please enter your ATM Card Number. ')
        A7 = input('enter your adhar card number. ')
        A8 = input('enter your voter card number. ')
        a1 = input('enter your PAN card number. ')
        print('here is your detail - ' )
        print('PAN card number - ' + str(a1))
        print('ATM card number - ' + str(A6))
        print('athar card number - ' + str(A7))
        print('voter card number - ' + str(A8))
        
    #you can add furder you want. By following this steps.
    #its second part wil be soon.....
