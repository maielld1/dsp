# Hint:  use Google to find python function
from datetime import datetime

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'

start_a = datetime.strptime(date_start, '%m-%d-%Y')
stop_a = datetime.strptime(date_stop, '%m-%d-%Y')

print(stop_a - start_a)

####b)  
date_start = '12312013'  
date_stop = '05282015'

start_b = datetime.strptime(date_start, '%m%d%Y')
stop_b  = datetime.strptime(date_stop, '%m%d%Y')

print(stop_b - start_b)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

start_c = datetime.strptime(date_start, '%d-%b-%Y')
stop_c = datetime.strptime(date_stop, '%d-%b-%Y')

print(stop_c - start_c)
