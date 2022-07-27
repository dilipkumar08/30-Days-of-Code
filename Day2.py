#operators
def solve(meal_cost, tip_percent, tax_percent):
    a=(meal_cost*tip_percent)/100
    b=(meal_cost*tax_percent)/100
    print(round(meal_cost+a+b))
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
