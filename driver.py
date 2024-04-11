import threading
from test_BECU import get_balance
import sheets
# Use threads to update all bank accounts simultaneously
threads = []
#BECU 
becu = threading.Thread(target=get_balance) #make it a class... 
becu.start()
threads.append(becu)
#CHASE

#SUNCOAST


for t in threads: t.join()
#SHEETS
sheets.update_google_sheet(becu, 'A2')