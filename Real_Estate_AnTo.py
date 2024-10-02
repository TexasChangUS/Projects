import pandas as pd
import requests
from bs4 import BeautifulSoup

#Current portfolio (mutable)
portfolio = {
    'Property':['8125 Loma Terrace Rd', '10322 Urban Oak Trail', '9619 Blue Water Hyssop'],
    'Price':[181900, 274700, 357700],
    'Rent':[1300, 1900, 2050],
    'LoanPay':[0, 1700, 0],
    'Insurance':[1314, 2870, 1200],
    'Total_Loan':[0, 160_000, 0],
    'Property_type':['Singe Family', 'Single Family', 'Single Family']
}

perspective = {
}

perspective_df = pd.DataFrame(perspective)

#Prints current real estate portfolio.
df = pd.DataFrame(portfolio)

#Determines ROI for current portfolio (currently manual imput)
df['ROI'] = ((df["Rent"]*12) - df['Insurance'] - df['LoanPay'])/ df['Price']
print(df['ROI'])

#Gives the basic metrics
average_price = df['Price'].mean()
print("Property average price: $",average_price)
total_worth = (df['Price'].sum() - (df['Total_Loan'].sum()))
print('Total Property value: $',total_worth)
cash_flow = df['Rent'].sum() - (df['Insurance'].sum() / 12) - (df['LoanPay'].sum())
print('Monthly Cash Flow: $',cash_flow)

#User Menu
def user_menu():
    print("\n1. Add Property")
    print("2. Search Property")
    print("3. View Portfolio")
    print("4. Calculate ROI for Property")
    print("5. Exit System")

# Adding property from menu
def add_property(df):
    address = input('Enter property address: ')
    current_price = float(input('Enter property price: '))
    rent = float(input('Enter monthly rent: '))
    loan_pay = float(input('Enter monthly loan payment: '))
    insurance = float(input('Input yearly insurance rate: '))
    total_loan = float(input('Enter total remaining laon ammount: '))
    property_type = input('Enter property type: ')

    df = df.append({
        'Property': address,
        'Price': current_price,
        'Rent': rent,
        'LoanPay': loan_pay,
        'Insurance': insurance,
        "Total_Loan": total_loan,
        "Property_type": property_type
    }, ignore_index=True)
    return df

#Prints current portfolio
def peek_portfolio(df):
    print("\nCurrentPorfolio")
    print(df)

#searches for specific properties
def search_property(df):
    address = input("Enter desired property: ")
    property_row = df[df['Property'].str.contains(address, case=False)]
    if not property_row.empty:
        print(property_row)
    else:
        print("Property not found or unavailable.")

#calculates ROI for searched property
def roi_calc(df):
    address = input("Enter property address to calcualte ROI: ")
    property_row = df[df['Property'].str.contains(addres, case=False)]
    if not property_row.empty:
        current_price = property_row['Price'].values[0]
        rent = property_row['Rent'].values[0]
        annual_expenses = (property_row['Insurance'].value[0])+(property_row['LoanPay'].value[0]*12)
        roi = ((rent*12)- annual_expenses)/current_price
        print(f"ROI for {address}: {roi:.2f}")
    else:
        print("Property not found or unavailable.")

def main():
    global df
    while True:
        user_menu()
        choice = input("Please select form choices: ")

        if choice == 1:
            add_property(df)
        elif choice == 2:
            search_property(df)
        elif choice == 3:
            peek_portfolio(df)
        elif choice == 4:
            roi_calc(df)
        elif choice == 5:
            break
        else:
            print("Choice unavailable, please try again")

if __name__ == "__main__":
    main()
        
            


    







    





