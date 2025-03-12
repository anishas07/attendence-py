number = int(input("Enter the your overal grade to join the exam!:"))

if number>85:
    print("Number is very high, you can join")
    if number%2==0:
        print("thats great")
    
    else:
        print("We need your attendence as well to determine if you can join the exam")

else: 
    print("Number is lower than 85")