xfrom database import *
a = input("Are you new or not new: ")
if a == 'new':
    while True:
        name  = input("enter your name: ")
        if not name.isalpha():
            continue
        else:
            try:
                age = int(input("enter age: "))
            except ValueError:
                print("sorry i did'nt understand that")
            c.execute("INSERT INTO malli(name,age) VALUES(?,?)",(name,age))
            conn.commit()
            print("You are added")
            break        
            print(a)
elif a == 'not new':
    print("pls proced to check up")
    from disease import *
    print(a)
    Disease = input("which disease do you have: ")
    if Disease == 'a'or Disease == 'b' or Disease == 'malaria'or Disease == 'corona':
        c.execute ("INSERT INTO Disease VALUES('Disease')")
        print("Go to Dr adren")
    elif Disease == 'c' or Disease == 'd'or Disease == 'e'or Disease == 'stomache' or Disease=='headache'or Disease=='fever':
        print("GO to Dr Sharo")
    elif b == 'f' or b == 'g'or b == 'aneamia' or b == 'whoopingcough':
        print("GO to Dr nessy")
    from pharmacy import *
