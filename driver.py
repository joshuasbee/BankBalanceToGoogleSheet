from test_BECU import BECU
import sheets
# Use threads to update all bank accounts simultaneously
threads = []
#BECU 
becu = BECU()
becu.start()
threads.append(becu)
#SUNCOAST

for t in threads: t.join()
#SHEETS
sheets.update_google_sheet(becu.result, 'A2')