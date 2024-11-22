month_number = int(input("Enter the month number (1-12):"))

year = int(input("Please enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_february = 29
else:
    days_in_february = 28


month_days = {
    1:31,
    2:days_in_february,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

if 1<= month_number <+12:
    print(f"Month{month_number}has{month_days[month_number]}days.")
else:
    print("invalid month number!")
