#parse month should take in the text of the month and return the number 
#as a string
#January -> 1 (as a string)
#YOU MAY USE THIS FUNCTION IF YOU WANT TO OR YOU MAY REMOVE IT
def parse_month(month):
    months = {
        "January": "01", "Febuary": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"
    }
    return months.get(month, "")

#REMOVE PASS AND FIX THIS FUNCTION
#parse_date function should return the date formated as MM/DD/YYYY
#DO NOT REMOVE THIS FUNCTION
def parse_date(user_string):
    month, day, year = user_string.split()
    day = day.rstrip(",")
    month_num = parse_month(month)
    return f"{month_num}/{day}/{year}"

#REMOVE PASS AND YOUR CODE GOES HERE
if __name__ == '__main__':
    while True:
        user_input = input()
        if user_input == "-1":
            break
        else:
            x = parse_date(user_input)
            print(x)