# Your code below:

#Q1
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

#Q2
prices = [2, 6, 1, 3, 2, 7, 2]

#Q3
num_two_dollar_slices = prices.count(2)

#Q4
num_pizzas = len(toppings)

#Q5
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#Q6
pizza_and_prices = [[2,	"pepperoni"], [6,	"pineapple"], [1,	"cheese"], [3,	"sausage"], [2,	"olives"], [7,	"anchovies"], [2,	"mushrooms"]]

#Q7
#print(pizza_and_prices)

#Q8
pizza_and_prices.sort()
#print(pizza_and_prices)

#Q9
cheapest_pizza = pizza_and_prices[0]

#Q10
priciest_pizza = pizza_and_prices[-1]

#Q11
pizza_and_prices.pop(-1)
print(pizza_and_prices)

#Q12
pizza_and_prices.insert([2.5, "peppers"])
print(pizza_and_prices)
