### Disclaimer:
#This is not fully my logic. I had to depend ChatGPT inorder to fix some issues with the code I wrote initially.
# I have refered as well as copied some logic from the GPT

def main():
    while True:
        idate = input("Date: ").strip()
        out = date(idate)
        if out:
            print( out )
            break

def date(x):

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]
    abbr_months = {
        "Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June",
        "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}




    input_date = x.strip()
    if '/' in input_date:
        try:
            month, day, year = input_date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1<= day <= 31:
                return f'{year}-{month:02}-{day:02}'
        except ValueError:
            pass
    elif ',' in input_date:
        try:
            month_day, year = input_date.split(',')
            month_day = month_day.strip()
            month, day = month_day.split( ' ')
            day = int(day.strip())
            year = int(year.strip())

            if month in abbr_months:
                month = abbr_months[month]
                # if 1 <= day <= 31:
                #     return f'{year}-{month:02}-{day:02} \n{year} {day} {year}'

            elif month in months:
                month = months.index(month) +1
                if 1 <= day <= 31:
                    return f'{year}-{month:02}-{day:02}'
        except (ValueError, IndexError):
            pass
    pass

if __name__ == "__main__":
    main()





