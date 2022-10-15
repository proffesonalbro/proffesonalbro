master_pwd = input("what is your master password? ")

if master_pwd == "1988":
    print('correct master password')
    pass
else :
    print('incorrect mastard password')
    quit()
    
def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input('Account name: ')
    pwd = input("Password")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:    
    mode = input("would you like to add a new password or view existing ones (view, add)? if you wnat to exit press the key (q)... ")
    if mode.lower() == "q":
        break
    
    if mode.lower() == "view":
        view()
    elif mode.lower() == "add":
        add()