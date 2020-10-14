#Eugene Washington lab assn 2
meal_cost = float( input( 'enter meal_cost:') )
tax = meal_cost * .07
tip = 0.20 * meal_cost
total_cost = meal_cost + tax + tip
print("meal_cost: $" + format( meal_cost, ",.2f"), "tip: $" + \
    format( tip, ",.2f" ), "tax: $" + format( tax, ",.2f"), \
       "total_cost: $" + format( total_cost, ",.2f"), sep = "\n" )
    