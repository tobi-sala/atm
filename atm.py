import string, random, time
#making account balance be any number at random
bal = float(random.randint(1,10000000))

#selecting language and entering pin
lang = int(input("Select Language: \n1. French\t\t\t\t4. Igbo\n2. Spanish\t\t\t\t5. Hausa\n3. English\t\t\t\t6. Yoruba\n: "))
if lang == 1:
    pin = str(int(input("Entrez votre epingle: ")))
    time.sleep(2)
    if len(pin) > 4:
        print("Entree non valide")
        quit()
    elif len(pin) < 4:
        print("Entree non valide")
        quit()
elif lang == 2:
    time.sleep(1)
    pin = str(int(input("Entrez votre epingle: ")))
    if len(pin) > 4:
        print("Entrada no valida")
        quit()
    elif len(pin) < 4:
        print("Entrada no valida")
        quit()
elif lang == 3:
    time.sleep(1)
    pin = str(int(input("Enter Your Pin: ")))
    if len(pin) > 4:
        print("Invalid input")
        quit()
    elif len(pin) < 4:
        print("Invalid input")
        quit()
elif lang == 4:
    time.sleep(1)
    pin = str(int(input("Tinye ntutu nkeji: ")))
    if len(pin) > 4:
        print("Ntutu na-ezighi ezi")
        quit()
    elif len(pin) < 4:
        print("Ntutu na-ezighi ezi")
        quit()
elif lang == 5:
    time.sleep(1)
    pin = str(int(input("Shigar da fil din ku: ")))
    if len(pin) > 4:
        print("Fil Mara Inganci")
        quit()
    elif len(pin) < 4:
        print("Fil Mara Inganci")
        quit()
elif lang == 6:
    time.sleep(1)
    pin = str(int(input("Te Pin re sii: ")))
    if len(pin) > 4:
        print("Pin Ti ko To")
        quit()
    elif len(pin) < 4:
        print("Pin Ti ko To")
        quit()

#selecting transaction
trans = int(input("Select Transaction: \n\t\t\t\t1. Withdrawal\n\t\t\t\t2. Deposit\n\t\t\t\t3. Check Account Balance\n: "))
if trans == 1:
    print("How much would you like to withdraw? \n1. $1000\t\t\t\t4. $5000\n2. #2000\t\t\t\t5. $10000\n3. #3000\t\t\t\t6. Others")
    wthdl = int(input(": "))
    time.sleep(1)
    if wthdl == 1:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savings\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed"))
        print("loading...")
        time.sleep(1)
        quit()
    elif wthdl == 2:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savings\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed"))
        print("loading...")
        time.sleep(1)
        quit()
    elif wthdl == 3:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savings\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed"))
        print("loading...")
        time.sleep(1)
        quit()
    elif wthdl == 4:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savings\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed"))
        print("loading...")
        time.sleep(1)
        quit()
    elif wthdl == 5:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savigs\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed\n:"))
        print("loading...")
        time.sleep(1)
        quit()
    elif wthdl == 6:
        acct = int(input("Enter you Account Type\n\t\t\t\t1. Savigs\n\t\t\t\t2. Current\n\t\t\t\t3. Fixed"))
        print("Enter how much you want in denominations of $500")
        wthdl = int(input(": "))
        print("Loading...")
        time.sleep(1)
    else:
        print("Invalid Selection")
elif trans == 2:
    print("How much would you like to Deposit? \n1. $1000\t\t\t\t4. $5000\n2. #2000\t\t\t\t5. $10000\n3. #3000\t\t\t\t6. $20000")
    time.sleep(1)
    dpst = int(input(": "))
    if dpst == 1:
        print("loading...")
        time.sleep(1)
        quit()
    elif dpst == 2:
        print("loading...")
        time.sleep(1)
        quit()
    elif dpst == 3:
        print("loading...")
        time.sleep(1)
        quit()
    elif dpst == 4:
        print("loading...")
        time.sleep(1)
        quit()
    elif dpst == 5:
        print("loading...")
        time.sleep(1)
        quit()
    elif dpst == 6:
        print("Enter how much you want in denominations of $500")
        dpst = int(input(": "))
        time.sleep(1)
        print("Loading...")
    else:
        print("Invalid Selection")
elif trans == 3:
    print("Your Account Balance is $ {}".format(bal))
else:
    print("Invalid Selection")
while trans != 1 or 2 or 3:
    trans = int(input("Select Transaction: \n\t\t\t\t1. Withdrawal\n\t\t\t\t2. Deposit\n\t\t\t\t3. Check Account Balance\n: "))
    if trans == 1:
        time.sleep(1)
        print("How much would you like to withdraw? \n1. $1000\t\t\t\t4. $5000\n2. #2000\t\t\t\t5. $10000\n3. #3000\t\t\t\t6. $20000")
    elif trans == 1:
        time.sleep(1)
        print("How much would you like to Deposit? \n1. $1000\t\t\t\t4. $5000\n2. #2000\t\t\t\t5. $10000\n3. #3000\t\t\t\t6. $20000")
    elif trans == 3:
        time.sleep(1)
        print("Your Account Balance is $ {}".format(bal))
    


ano_trans = input("Would you like to perform another transaction?\n type Y for yes and N for no")
if ano_trans == "Y" or "y":
    trans = int(input("Select Transaction: \n\t\t\t\t1. Withdrawal\n\t\t\t\t2. Deposit\n\t\t\t\t3. Check Account Balance\n: "))
