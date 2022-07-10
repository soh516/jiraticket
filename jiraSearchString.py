from datetime import *

today = date.today()
first = today.replace(day=1)
lastMonth = first - timedelta(days=1)

start_year = lastMonth.strftime('%Y')
start_month = lastMonth.strftime('%m')
start_day = input('Enter the start day:')

current_year = datetime.now().strftime('%Y')
current_month = datetime.now().strftime('%m')
current_day = datetime.now().strftime('%d')

start_date = start_year + '-' + start_month + '-' + start_day
end_date = current_year + '-' + current_month + '-' + current_day

linux = "assignee = soh516 AND createdDate >= '" + start_date + "' AND createdDate <= '" + end_date + "'" + " AND \"ISD Queue\" = \"Research Computing\""
redcap = "createdDate >= '" + start_date + "' AND createdDate <= '" + end_date + "'" + " AND text ~ redcap AND \"ISD Queue\" = \"Research Computing\""

print("linux search string:\n" + linux + "\n")
print("redcap search string:\n" + redcap + "\n" )
print("general search string:\n")
print("hpc search string:\n")
