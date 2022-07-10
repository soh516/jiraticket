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

core_nsid = ["mod697", "jdc210"]
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

if len(core_nsid) == 1:
    general = getString(core_nsid[0], start_date, end_date)
    print(general.getGeneralSearchString() + "\n")
else:
    for x in core_nsid:
        general = getString(x, start_date, end_date)
        print(general.getGeneralSearchString() + "\n")

if len(hpc_nsid) == 1:
    hpc = getString(hpc_nsid[0], start_date, end_date)
    print(hpc.getHPCSearchString() + "\n")
else:
    for x in hpc_nsid:
        hpc = getString(x, start_date, end_date)
        print(hpc.getHPCSearchString() + "\n")
