actual_cost=float(input("What is the original cost of the product?"))
sales_cost=float(input("What is the price you are selling your product at?"))

if actual_cost<sales_cost:
    amount= sales_cost-actual_cost
    print("Profit={0}".format(amount))

else:
    print("No Profit.")