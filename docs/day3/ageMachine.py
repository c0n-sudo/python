#start ageMachine with function

#function
def ageMachine(age: int):
    age = int(input("Enter your age: "))
    if age >= 50:
        print("User is old enough to enter")
    elif age < 50:
        print("User is not old enough to enter")

#call function
ageMachine(50)

#end