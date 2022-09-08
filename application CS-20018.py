print("******")
print("Hotel Database")
print("***")
print("Welcome To The Hiba Hotel")
print("***")
print("Please Choose What You Would Like To Do")
print("Enter anything to exit out of the program")
print("1.Enter Details")
print("2.Total Money")
print("3.Enter Your Thoughts")
print("4.Write Database")
print("5.Display Database")
print("6.Load Database")
print("7.Exit The Hotel")

data=[]
def ent():
    print("\n")
    print("Hey,Enter your details please:")
    while True:
        name=input(str("Please Enter Your Full Name:"))
        ID=input(str("Please Enter Your CNIC Number:"))
        room=input(str("Please Enter How Many Rooms You Need:"))
        days=input(str("Please Enter How Long You'll Stay:"))
        age=input(str("Please Enter Your Age:"))
        print()
        list_of_records=[name,ID,room,days,age]
        data.append(list_of_records)
        x=input("Are there any more entries? Enter ""y"" if yes:")
        if x!="y":
            break
def display():
        count=0
        for i in range(len(data)):
            print("Person's Name:",data[count][0])
            print("CNIC Number:",data[count][1])
            print("Total Rooms To Be Used:",data[count][2])
            print("Days They Will Stay:",data[count][3])
            print("Their Age:",data[count][4])
            count+=1          
def save_data():
    f=open("database.txt","w")
    count=0
    for element in data:
        f.write(data[count][0]+",")
        f.write(data[count][1]+",")
        f.write(str(data[count][2])+",")
        f.write(str(data[count][3])+",")
        f.write(str(data[count][4])+"\n")
        count+=1
    f.close()
    print("The Database has been saved")

def load_data():
    f=open("database.txt")
    for element in f:
        r=element.split(",")
        print(r)
    f.close()

def exit():
    print("Hopefully you had a good time")
    print("Please leave a small review on our hotel if you can or enter any key to exit")

def thoughts():
    f=open("thoughts.txt","w")
    review=input("Enter Your Review Here =):")
    f.write(review)
    f.close()

def money():
    m1=int(input("Enter The Number Of Rooms You Used:"))
    m2=int(input("Enter The Number Of Days You Stayed:"))
    print("Your total bill is:",(m2*10*m1),'$')

info=[]
while True:
    print("Hello There!")
    choose=int(input("Choose your option please:"))
    if choose==1:
        ent()
    elif choose==2:
        money()
    elif choose==3:
        thoughts()
    elif choose==4:
        save_data()
    elif choose==5:
        display()
    elif choose==6:
        load_data()
    elif choose==7:
        exit()
    else:
        print("Thankyou For Visiting")
        break
