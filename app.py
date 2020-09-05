# This is my app, it will help calculate your moving cost
distance = input ("Please input the distance in km: ")
distance = int (distance)
layout = input ( 'Input 1 if your layout is 1LDK and input 2 if your layour is 2LDK: ')
layout = int(layout)
if (layout == 1):
    base_cost = 8000
elif (layout == 2): 
    base_cost = 12000

# where x is total amount 
total_items = input ("How many items do you have in your house?  ")
total_items = int(total_items)

cost = base_cost + distance + 10000 + total_items * 1000
print ("The total cost of your move is {}". format (cost))