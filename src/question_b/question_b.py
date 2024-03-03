
weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']

def get_day_of_week(val):
    val=str(val)
    if not val or not val.isnumeric():
        return('ERROR')
    else:
        val = int(val)
        if val < 1 or val > 7:
            return('ERROR')
        else:
            return(weekdays[val-1])
