from datetime import *

today = date.today()
first = today.replace(day=1)
lastMonth = first - timedelta(days=1)

start_year = lastMonth.strftime('%Y')
start_month = lastMonth.strftime('%m')
start_day = input('Enter the start day:')

while True:
    try:
        int(start_day)
    except ValueError: 
        print('Must be interger!!')
        exit(1)
    else:
        if (1 <= int(start_day) <= 31):
            break
        else:
            print('Out of range!!')
            exit(1)

print("")

current_year = datetime.now().strftime('%Y')
current_month = datetime.now().strftime('%m')
current_day = datetime.now().strftime('%d')

start_date = start_year + '-' + start_month + '-' + start_day
end_date = current_year + '-' + current_month + '-' + current_day

general_nsid = ["mod697", "jdc210"]
hpc_nsid = ["olf067", "ses863", "bmb760", "bob521"]


class getString:
    def __init__(self, nsid, start_date, end_date):
        self.nsid = nsid
        self.start_date = start_date
        self.end_date = end_date
    def getLinuxSearchString(self):
        return "assignee = " \
                + self.nsid \
                + " AND createdDate >= '" \
                + self.start_date \
                + "' AND createdDate <= '" \
                + self.end_date \
                + "'" \
                + " AND \"ISD Queue\" = \"Research Computing\""
    def getRedcapSearchString(self):
        return "createdDate >= '" \
                + self.start_date \
                + "' AND createdDate <= '" \
                + self.end_date + "'" \
                + " AND text ~ redcap AND \"ISD Queue\" = \"Research Computing\""
    def getGeneralSearchString(self):
        return "createdDate >= '" \
                + self.start_date \
                + "' AND createdDate <= '" \
                + self.end_date + "'" \
                + " AND assignee = " \
                + self.nsid \
                + " AND text !~ redcap AND \"ISD Queue\" = \"Research Computing\""
    def getHPCSearchString(self):
        return "createdDate >= '" \
                + self.start_date \
                + "' AND createdDate <= '" \
                + self.end_date + "'" \
                + " AND assignee = " \
                + self.nsid


linux = getString("soh516", start_date, end_date)
print("linux search string:\n" + linux.getLinuxSearchString() + "\n")

redcap = getString("", start_date, end_date)
print("redcap search string:\n" + redcap.getRedcapSearchString() + "\n")

if len(general_nsid) == 1:
    general = getString(general_nsid[0], start_date, end_date)
    general_string = general.getGeneralSearchString()
else:
    for i in range(len(general_nsid)):
        if i == 0:
            general = getString(general_nsid[i], start_date, end_date)
            general_string = "(" + general.getGeneralSearchString() + ")"
        else:
            general = getString(general_nsid[i], start_date, end_date)
            general_string = general_string + " OR " + "(" + general.getGeneralSearchString() + ")"

print("general search string:\n" + general_string + "\n")


if len(hpc_nsid) == 1:
    hpc = getString(hpc_nsid[0], start_date, end_date)
    print(hpc.getHPCSearchString() + "\n")
else:
    for i in range(len(hpc_nsid)):
        if i == 0:
            hpc = getString(hpc_nsid[i], start_date, end_date)
            hpc_string = "(" + hpc.getHPCSearchString() + ")"
        else:
            hpc = getString(hpc_nsid[i], start_date, end_date)
            hpc_string = hpc_string + " OR " + "(" + hpc.getHPCSearchString() + ")"

print("hpc string:\n" + hpc_string + "\n")
