def living_cost(days):
    return 4000*days

def plane_cost(city):
    if  city=="Delhi":
        return 10000
    elif city=="Chennai":
        return 15000
    
def trip_expendature(city, days, shopping_money):
    return living_cost(days) + plane_cost(city) + shopping_money

print("Total trip expendature: $", trip_expendature("Delhi",5,5000))