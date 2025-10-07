#it is a callback example, customer in restaurant put order and waiter deliver food

def checkFoodExistance(food_name:str):
    #             0        1         2          .........n
    arr_foods=["Pizza", "Pasta", "Döner"]
    arr_length = len(arr_foods)
    print(f"we have {arr_length} foods in our menu")

def orderFood(food_name:str, checkFoodExistance):
    print(f"your {food_name} deliver soon!")
    checkFoodExistance(food_name)


    #--actual program use upper defined methods --#
order_string = input("what is your order?")
orderFood(order_string,checkFoodExistance)