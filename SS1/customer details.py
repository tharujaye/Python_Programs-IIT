# Get 5 customer details to a list (user will insert the values)
customers = []
for i in range(5):
    customer = input("Enter customer name: ")
    customers.append(tuple(customer.split()))

# Update the 4th customer name to “Seth”
customers[3] = ("Seth",) + customers[3][1:]

# Display the length of the name of the last customer
last_customer_name_length = len(customers[-1][0])
print(f"The length of the name of the last customer is {last_customer_name_length}.")

# Convert the customer list to a tuple
#customer_tuple = tuple(customers)

# Display the length of the tuple
customer_list_length = len(customers)
print(f"The length of the customer list is {customer_list_length}.")

# Display all the customer names using the tuple (use a loop)
for customer in customers:
    print(customer[0])

print(customers)

# Delete the newly created tuple
del customers
