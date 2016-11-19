from ds18b20_CLASS import DS18B20   

import time
   
# test temperature sensors
x = DS18B20()
count=x.device_count()

while True:
	i = 0
	while i < count:
		print(x.tempC(i))
		i += 1
	
	time.sleep(1)
