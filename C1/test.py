from datetime import datetime

now = datetime.now()

now = str(now)

print(now[5:7]+ now[8:10] + now[11:13] + now[14:16] + now[0:4] + '.' + now[17:19])

print("now =", now)

import os

os.popen('sh st.sh')
