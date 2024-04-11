from test_BECU import BECU
from test_CHASE import CHASE
import sheets
# Use threads to update all bank accounts simultaneously
threads = []
#BECU 
# becu = BECU()
# becu.start()
# threads.append(becu)
#CHASE
chase = CHASE()
chase.start()
threads.append(chase)
#SUNCOAST


for t in threads: t.join()
#SHEETS
# sheets.update_google_sheet(becu.result, 'A2')
print(f'{chase.result=}')