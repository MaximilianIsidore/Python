from budget_app import Category, create_spend_chart

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(1000, "initial deposit")
food.withdraw(150.25, "groceries")
food.withdraw(50.75, "restaurant")

entertainment.deposit(500, "initial deposit")
entertainment.withdraw(200, "movies")

business.deposit(2000)
business.withdraw(150)

print(food)
print(create_spend_chart([business, food, entertainment]))
