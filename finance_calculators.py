import math
# display menu options
print("""investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan""")

# assign chosen menu option to a variable
menu_option = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# string letters turned into lowercase 
menu_option = menu_option.lower()

# display message for an invalid input
if menu_option == "investment" or menu_option == "bond":
    pass 
else:
    print("Invalid menu option")

# conditional statement for if menu option selected is 'investment'
if menu_option == "investment":

    # assign input values to variables
    money_deposit = int(input("Enter amount of money you wish to deposit: "))
    interest_rate = int(input("Enter the interest rate as a percentage: "))
    investing_years = int(input("Enter the years you plan on investing: "))
    interest_type = input("Simple or Compound interest? : ")

    # convert interest_type into all lowercase string
    interest_type = interest_type.lower()

    # displays message if invalid answer
    if interest_type == "simple" or interest_type == "compound":
        pass
    else:
        print("Please enter either 'simple' or 'compound'.")
    
    # conditonal statement for simple interest option
    if interest_type == "simple":

        # calculate the interest from the user input
        simple_total = money_deposit*(1+(interest_rate/100)*investing_years)
        simple_interest = simple_total - money_deposit

        # round values by 2 decimal places
        simple_interest = round(simple_interest, 2)
        simple_total = round(simple_total, 2)

        # display the total amount of interest gained and total amount invested 
        print(f"If {money_deposit} is deposited, in {investing_years} years you would have gained {simple_interest} in interest with a total of {simple_total}")
    
    # conditional statement for compound interest option
    if interest_type == "compound": 

        # calculate the interest from the user input
        compound_total = money_deposit * math.pow((1+(interest_rate/100)), investing_years)
        compound_interest = compound_total - money_deposit

        # round values by 2 decimal places
        compound_interest = round(compound_interest, 2)
        compound_total = round(compound_total, 2)

        # display the total amount of interest gained and total amount invested 
        print(f"If {money_deposit} is deposited, in {investing_years} years you would have gained {compound_interest} in interest with a total of {compound_total}")

# conditional statement for if menu option selected is 'bond'
if menu_option == "bond":

    # assign imput to values
    present_value = int(input("Enter present home value : "))
    monthly_rate = float(input("Enter interest rate of home loan as a percentage : "))
    amount_months = int(input("Enter the amount of months to repay the loan : "))

    # use the input values to to work out the monthly repayment
    repayment = (((monthly_rate/100)/12) * present_value)/(1-(1+((monthly_rate/100)/12))**(-amount_months))

    # round the montly payment to 2 decimal places
    repayment = round(repayment, 2)

    # display the monthly repayment to to the user
    print(f"The monthly repayments of the home loan will be {repayment}")
    