# Monthly Sales Analysis

# Create an application to input monthly sales data for a company and perform a basic annual performance analysis.

print('Welcome to the best monthly sales analysis!\nPlease enter your total sales for each month below in this format: 00.00\nExample: 1500.50')



# Add month names to monthly_sales list
month_names = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]

monthly_sales = []

for month in range(0,12):
    sales = float(input(f'Enter sales for {month_names[month]}: '))
    monthly_sales.append(sales)

print('Monthly Sales:', monthly_sales)



# Sum all monthly sales to get the annual total.
total = 0

for i in monthly_sales:
    total += i
    total = round(total, 2)
print('Total annual sales: $', total)




# Calculate the average monthly sales.

for i in monthly_sales:
    len_list = total / len(monthly_sales)
    len_list = round(len_list,2)
print('Average monthly sales: $', len_list)




# Identify the months with the highest and lowest sales.

highest_sales = monthly_sales[0]
lowest_sales = monthly_sales[0]

for number in monthly_sales:
    if number > highest_sales:
        highest_sales = number
        highest_sales = round(highest_sales,2)
    elif number < lowest_sales:
        lowest_sales = number
        lowest_sales = round(lowest_sales,2)

print('Highest Sale: $', highest_sales)
print('Lowest Sale: $', lowest_sales)



print('\nDeveloped by carloscoronatax')


