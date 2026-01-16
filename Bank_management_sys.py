import random
import string
balance = 0
acc_fn = ""
def ch():
    print(" 1) Show Account Balance \n 2) deposit \n 3)withdraw \n 4)show Account Number \n 5)exit ")

def show_balance():
    global balance,acc_fn
    load_balance()
    print(f"current Balance : {balance}")
    print()

def deposit():
    global acc_fn
    global balance
    load_balance()
    dep = int(input("Enter Deposit Amount : "))
    balance += dep
    print(f"Your current Balance : {balance}")
    print()

    with open(f"{acc_fn}.txt",'a+') as f:
       f.write(f"Deposit : {dep}\n")
       f.write(f"balance : {balance}\n {'-'*80}\n")
    load_balance()

def load_balance():
    global acc_fn, balance
    with open(f"{acc_fn}.txt", "r") as f:
        lines = f.readlines()
    
    second_last_line = lines[-2].strip() 
    
    parts = second_last_line.split(":")
    if len(parts) == 2:
        balance = int(parts[1].strip())  
    else:
        balance = 0  
        
def withdraw():
    global acc_fn
    global balance
    load_balance()
    wd = int(input("Enter Withdraw Amount : "))
    if wd > balance:
     print("❌ Insufficient Balance")
     return
    balance -= wd
    print(f"Your current Balance : {balance}")
    print()
    
    with open(f"{acc_fn}.txt",'a+') as f:
       f.write(f"withdraw : {wd}\n")
       f.write(f"balance : {balance}\n {'-'*80}\n")
    load_balance()

def see_acc_num():
    e = input("Enter Email ID : ")
    with open("admin.txt", "r") as f:
        read = f.readlines()

        for i in range(len(read)):
            if read[i].strip() == f"Email ID : {e}":
                print("Account Found!")
                pa = input("Enter Password : ")
                if i + 2 < len(read) and read[i + 2].strip() == f"Password : {pa}":
                    print(read[i + 3].strip())  
                else:
                    print("❌ Incorrect Password")
                return
        print("❌ Email Not Found")


def user_login():
    global acc_fn
    e = input("Enter Email ID: ")
    with open("admin.txt", "r") as f:
        read = f.readlines()

        if len(read) == 0:
            print("⚠️ No accounts found.")
            return

        for i in range(len(read)):
            if read[i].strip() == f"Email ID : {e}":
                print("✅ Account Found!")
                pa = input("Enter Password: ")
                if i + 2 < len(read) and read[i + 2].strip() == f"Password : {pa}":
                    acc_fn = read[i - 2].strip().split(":")[1].strip()

                    print("✅ Login Successful")
                    while True:
                     print()
                     ch()
                     cho = int(input("Enter Your Choice: "))
                     if cho == 1:
                         show_balance()
                     elif cho == 2:
                         deposit()
                     elif cho == 3:
                         withdraw()
                     elif cho == 4:
                         see_acc_num()
                     elif cho == 5:
                         exit()
                     else:
                         print("❌ Invalid choice.")
                         break
                else:
                    print("❌ Incorrect Password")
                return
        print("❌ Email Not Found")


def create_acc():
    global acc_fn
    l = list(string.digits*3)
    random.shuffle(l)
    num = ''.join(random.sample(l,12))
    acc_fn = input("First Name : ")
    acc_ln = input("last Name : ")
    acc_em = input("Email ID : ")
    acc_mn = input("Contact No : ")
    p = input("Password : ")
    with open("admin.txt","a+") as f:
        f.write(F"First Name : {acc_fn}\n")
        f.write(F"last Name : {acc_ln}\n")
        f.write(F"Email ID : {acc_em}\n")
        f.write(F"Contact No : {acc_mn}\n")
        f.write(f"Password : {p} \n")
        f.write(f"Account Number : {num} \n {'-'*80} \n")
    print("Your Account Create Successfully....")
    print(f"Account Number : {num}")
    print()
    
    with open(f"{acc_fn}.txt","w") as f:
        f.write(f"balance : 0\n {'-'*80}\n\n")
    user_login()

print(" Welcome to Bank System ".center(100,'='))
print()
print(" 1) Create a acount..\n 2) login \n 3) exit")
c = int(input("Enter The Choice : "))
match c:
    case 1:
      create_acc()
    case 2:
     user_login()
    case 3:
         exit()
    case _:
        print("Inlaid Choice")
    

