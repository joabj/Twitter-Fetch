from twitter import *
import json
import os.path
import time
import Environs

t = Twitter(
auth=OAuth(Environs.OAUTH_TOKEN, Environs.OAUTH_TOKEN_SECRET,
                       Environs.CONSUMER_KEY, Environs.CONSUMER_SECRET)
           )

DailyCollection = json.dumps(t.statuses.user_timeline())

## dd-mm-yyyy format
dated = time.strftime("%Y-%m-%d.json")

file_name = os.path.join(Environs.save_path, dated)


#print DailyCollection

f = open(file_name, 'w')
f.write(DailyCollection)
f.close()
		
