import json


ACCOUNT=1000000
SPLIT=5
MORTGAGE_INTEREST=0.04
OCCUPANCY_RATE=0.75 #Off the internet
NIGHTLY_RATE=0.0015 #GPT gave me this as its anywhere from 0.1% to 0.2%

PROPERTIES=SPLIT
EQUITY=ACCOUNT
DOWN_PAYMENT=ACCOUNT/SPLIT
MORTGAGE=(ACCOUNT/SPLIT)*4
YEARLY_MORTGAGE_PAYMENT= 12 * (MORTGAGE * (MORTGAGE_INTEREST / 12) * (1 + (MORTGAGE_INTEREST / 12)) ** (30 * 12) / ((1 + (MORTGAGE_INTEREST / 12)) ** (30 * 12) - 1))
HOUSE_VALUE=((ACCOUNT/SPLIT)*5)
DAILY_RENT=NIGHTLY_RATE*HOUSE_VALUE #This was obtained by assuming that 
TAXES=(HOUSE_VALUE * 0.27)*(80/1000) #Boulder Colorado Taxing Structure
SQUARE_FEET=((ACCOUNT/SPLIT)*5)/200 #House Cost / $200 per square foot 
MAINTENANCE=5*SQUARE_FEET #5 dollars per square foot per year
CLEANING=((SQUARE_FEET*0.075)*84.88) #84 days per year because average trip is 4.3 nights
UTILS=1.2*SQUARE_FEET #$1.20 per square foot per year 
ACCOUNT-=ACCOUNT
INSURANCE_COST=(DAILY_RENT*(365*OCCUPANCY_RATE))*0.03
MANAGEMENT_COST=5000
CASH_DEDUCTION=0.05
details={
    "Account":ACCOUNT,
    "Properties":PROPERTIES,
    "Equity":EQUITY,
    "YearlyIncome":0,
    "Cash":0
}
new_house={
    "Downpayment":DOWN_PAYMENT,
    'YearlyMortgagePayment':YEARLY_MORTGAGE_PAYMENT,
    'YearsPaid':0,
    'HouseValue':HOUSE_VALUE,
    "DailyRent": DAILY_RENT,
    "Occupancy":OCCUPANCY_RATE,
    "Taxes":TAXES,
    "SquareFeet":SQUARE_FEET,
    "MaintenanceCost":MAINTENANCE,
    "CleaningCost":CLEANING,
    "UtilityCost":UTILS,
    "InsuranceCost":INSURANCE_COST,
    "ManagementCost":MANAGEMENT_COST,
}

houses = [new_house.copy() for _ in range(SPLIT)]

year=1
for i in range(0,10):
    print("Account", json.dumps(details, indent=4))
    print("Example House", json.dumps(houses[0], indent=4))
    print()

    startingBalance=details['Account']
    for house in houses:
        house['YearsPaid']+=1
        details['Equity']+=MORTGAGE/30
        details['Account']+=(house['DailyRent']*(house['Occupancy']*365))-house['Taxes']-house['MaintenanceCost']-house['UtilityCost']-house['CleaningCost']-house['InsuranceCost']-house['ManagementCost']-house['YearlyMortgagePayment']

    details['YearlyIncome']=details['Account']-startingBalance
    
    details['Cash']+=(CASH_DEDUCTION*details['Account'])
    details['Account']=details['Account']-(CASH_DEDUCTION*details['Account'])

    new_houses=int((details['Account'])/(HOUSE_VALUE/5))

    for i in range(0, new_houses):
        houses.append(new_house)
        details['Account']-=(HOUSE_VALUE/5)
        details['Properties']+=1







