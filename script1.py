import pandas as pd 
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt

states = pd.read_csv("states_daily_4pm_et.csv")

for value in states['date']:

  datetimeobject = datetime.strptime(str(value),'%Y%m%d')
  new_value = datetimeobject.strftime('%m-%d-%Y')
  states.loc['date']= new_value
  states.replace(to_replace = value, value = new_value, inplace = True)

states['date'] =  pd.to_datetime(states['date'], infer_datetime_format=True)

def get_state_info(name):
   select_indices = list(np.where(states["state"] == name)[0])
   state = states.iloc[select_indices]
   statepos = state['positive']
   statedate = state['date']
   stateneg = state['negative']
   return statedate, statepos, stateneg

date, pos, _ = get_state_info('NY')           #input any state name
plt.plot(date, pos)


fig,ax = plt.subplots(1)
manhat = pd.read_csv("NY_36061_mob.csv")
manhat['date'] =  pd.to_datetime(manhat['date'], infer_datetime_format=True)

manhat['Rolling_Mean'] = manhat['mobility_driving'].rolling(window = 15).mean()
fig,ax = plt.subplots(1)
manhat['Rolling_Mean'] = manhat['mobility_driving'].rolling(window = 15).mean()
ax.plot('date','Rolling_Mean', data = manhat)
ax.plot('date', 'mobility_driving', data = manhat, color = 'r')