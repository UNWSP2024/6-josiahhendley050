# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
#Josiah Hendley
#2/27/26
#Tax Rate
#PSEUDOCODE
# Function calcTaxes(totalSales)
#     Set STATE_RATE = 0.05
#     Set COUNTY_RATE = 0.025
#
#     Set stateTax = totalSales * STATE_RATE
#     Set countyTax = totalSales * COUNTY_RATE
#     Set totalTax = stateTax + countyTax
#
#     Return stateTax, countyTax, totalTax
# End Function
#
# Main Module
#     Display "Enter total sales for the month:"
#     Input monthlySales
#
#     Call calcTaxes(monthlySales)
#         Return stateTax, countyTax, totalTax
#
#     Display "County Sales Tax: ", countyTax
#     Display "State Sales Tax: ", stateTax
#     Display "Total Sales Tax: ", totalTax
# End Main


#Program 3: Tax Rate
def calcTaxes(totalSales):
    STATE_RATE = 0.05
    COUNTY_RATE = 0.025

    stateTax = totalSales * STATE_RATE
    countyTax = totalSales * COUNTY_RATE
    totalTax = stateTax + countyTax

    return stateTax, countyTax, totalTax


def main():
    monthlySales = float(input("Enter total sales for the month: "))

    stateTax, countyTax, totalTax = calcTaxes(monthlySales)

    print("County Sales Tax:", round(countyTax, 2))
    print("State Sales Tax:", round(stateTax, 2))
    print("Total Sales Tax:", round(totalTax, 2))


main()

