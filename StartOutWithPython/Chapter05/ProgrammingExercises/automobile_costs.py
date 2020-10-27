# This program asks the user to enter the expenses cost
# of operating his or her automobile
# loan payment: insurance: gas: oil: tires: and maintenance
# Then display the total monthly costs and the total annual costs

YEAR_FACTOR = 12


def main():

    monthly_costs = total_monthly_costs()

    print(f'The Total Monthly Costs Is: ${monthly_costs:,.2f}')
    print('The Total Annual Costs Is $', format(total_annual_costs(monthly_costs),' ,.2f'), sep='')


def total_monthly_costs():
    loan = float(input('Enter the amount of total loan payed: '))
    insurance = float(input('Enter the amount of insurance incurred: '))
    gas = float(input('Enter the amount spent on gas: '))
    oil = float(input('Enter the amount spent on oil: '))
    tires = float(input('Enter the amount spent on tires: '))
    maintenance = float(input('Enter the amount of total maintenance: '))
    total_cost = loan + insurance + gas + oil + tires + maintenance
    return total_cost


def total_annual_costs(costs):
    return costs * YEAR_FACTOR


main()





