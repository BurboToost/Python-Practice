# Problem 07 - Finding largest and smallest number of three numbers using nested if_else

num01 = float(input("Enter your first number: "))
num02 = float(input("Enter your second number: "))
num03 = float(input("Enter your third number: "))

if num01>num02 and num01>num03:
    print("The First Number is the largest")
    if num02<num03:
        print("The Second Number is the smallest")
    elif num03<num02:
        print("The Third Number is the smallest")
    elif num02==num03:
        print("The Second & Third Number both are of same value")

elif num02>num03 and num02>num01:
    print("The Second Number is the largest")
    if num01<num03:
        print("The First Number is the smallest")
    elif num03<num01:
        print("The Third Number is the smallest")
    elif num03==num01:
        print("The First & Third Number both are of same value")

elif num03>num02 and num03>num01:
    print("The Third Number is the largest")
    if num02<num01:
        print("The Second Number is the smallest")
    elif num01<num02:
        print("The First Number is the smallest")
    elif num02==num01:
        print("The First & Second Number both are of same value")

elif num01==num02 and num01>num03:
    print("The First and Second Number are of same value and larger than The Third Number")
elif num03==num01 and num01>num02:
    print("The First and Third Number are of same value and larger than The Second Number")
elif num03==num02 and num02>num01:
    print("The Second and Third Number are of same value and larger than The First Number")
else:
    print("They are all of the same value")