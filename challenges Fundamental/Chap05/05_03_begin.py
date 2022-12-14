
def wash_car(payed):
    if(payed==12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if(payed==6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

price=int(input("choose the wash price (6 || 12) "))

wash_car(price)