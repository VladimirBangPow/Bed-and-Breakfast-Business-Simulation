import json
import uuid

ACCOUNT=1000000
SPLIT=5
MORTGAGE_INTEREST=0.04
OCCUPANCY_RATE=0.84 #Off the internet
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

N_YEARS=11

_houses=[]
_details=[]

details={
    "Account":ACCOUNT,
    "Properties":PROPERTIES,
    "Equity":EQUITY,
    "YearlyIncome":0,
    "Cash":0,
    "Year":0,
    "TotalDebt":MORTGAGE*SPLIT
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
    "Id":str(uuid.uuid4()),
    "Year":0
}
for i in range(0, SPLIT):
    _new_house=new_house.copy()
    _new_house['Id']=str(uuid.uuid4())
    _houses.append(_new_house)


year=1
for i in range(0,N_YEARS):

    details['Year']+=1
    _details.append(details.copy())

    startingBalance=details['Account']
    for house in _houses:
        house['YearsPaid']+=1
        house['Year']+=1
        details['Equity']+=MORTGAGE/30
        details['Account']+=(house['DailyRent']*(house['Occupancy']*365))-house['Taxes']-house['MaintenanceCost']-house['UtilityCost']-house['CleaningCost']-house['InsuranceCost']-house['ManagementCost']-house['YearlyMortgagePayment']
        details['TotalDebt']-=MORTGAGE/30

    details['YearlyIncome']=details['Account']-startingBalance
    
    details['Cash']+=(CASH_DEDUCTION*details['Account'])
    details['Account']=details['Account']-(CASH_DEDUCTION*details['Account'])

    new_houses=int((details['Account'])/(HOUSE_VALUE/5))

    for i in range(0, new_houses):
        _new_house=new_house.copy()
        _new_house['Id']=str(uuid.uuid4())
        _houses.append(_new_house)
        details['Account']-=(HOUSE_VALUE/5)
        details['Properties']+=1
        details['TotalDebt']+=MORTGAGE



print("Account", json.dumps(_details, indent=4))
# print("Houses", json.dumps(_houses, indent=4))



