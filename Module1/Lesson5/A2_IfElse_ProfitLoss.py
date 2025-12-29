actual_cost = float(input(" Please Enter the Actual Product Price: "))
sale_amount = float(input(" Please Enter the Sales Amount: "))
 
if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    #{0} is a placeholder for amount variable in format function 0 replace by the ammount value
    print("Total Profit = {0}".format(amount))
else:
    print("No Profit!!!")