ACCOUNT=1000000
SPLIT=5
INTEREST=0.04
OCCUPANCY=0.84
PROPERTIES=SPLIT
EQUITY=ACCOUNT
DOWN_PAYMENT=ACCOUNT/SPLIT
MORTGAGE=(ACCOUNT/SPLIT)*4
YEARLY_MORTGAGE= 12 * (MORTGAGE * (INTEREST / 12) * (1 + (INTEREST / 12)) ** (30 * 12) / ((1 + (INTEREST / 12)) ** (30 * 12) - 1))
YEARS_PAID=0
HOUSE_VALUE=DOWN_PAYMENT*SPLIT
RENT=0.0016*HOUSE_VALUE
TAXES=(HOUSE_VALUE * 0.27)*(80/1000)
SQUARE_FEET=((ACCOUNT/SPLIT)*5)/200
MAINTENANCE=5*SQUARE_FEET
UTILS=1.2*SQUARE_FEET
ACCOUNT-=ACCOUNT

details={
    "Account":ACCOUNT,
    "Properties":PROPERTIES,
    "Equity":EQUITY,
}
new_house={
        "Downpayment":DOWN_PAYMENT,
        'YearlyPayment':YEARLY_MORTGAGE,
        'YearsPaid':YEARS_PAID,
        'HouseValue':HOUSE_VALUE,
        "Rent": RENT,
        "Occupancy":OCCUPANCY,
        "Taxes":
    },
houses=[]
year=1
for i in range(0,25):
    print("Year:", i)
    print("account:", account)
    print("properties:", len(houses))
    print("yearly income:", len(houses)*annual_return)
    print("Equity:", equity)
    print()

    account+=(annual_return*len(houses))

    for house in houses:
        house['YearsPaid']+=1
        equity+=house['YearlyPayment']
        if house['YearsPaid']<=30:
            account-=house['YearlyPayment']

    new_houses=int(account/house_cost)

    for j in range(0, new_houses):
        houses.append({
            'YearsPaid':0,
            'Principal':house_cost,
            'YearlyPayment':61980
        })
        equity+=house_cost
        account-=house_cost


