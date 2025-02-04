#Import necessary libraries
import os
import time
import adafruit_dht
import board

#Set up DHT22
dht_device = adafruit_dht.DHT22(board.D18, use_pulseio=False)

#If the report file is empty, add the header
try:
	if os.path.getsize('/home/elifaulk/humidity.csv') == 0:
		with open('/home/elifaulk/humidity.csv', 'a') as f:
			f.write('Date,Time,Temperature C, Temperature F,Humidity\r\n')
except:
	pass

#Until program is ended...
while True:
	try:
		#Collect temperatures and humidity
		temperature_c = dht_device.temperature
		temperature_f = temperature_c * (9/5) + 32

		humidity = dht_device.humidity

		#Write the data in the CSV report file
		data = ('{0},{1},{2:0.1f}*C,{3:0.1f}*F,{4:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature_c, temperature_f, humidity))
		with open('/home/elifaulk/humidity.csv', 'a') as f:
			f.write(data)
		print(data)
	except RuntimeError as err:
		print(err.args[0])
	
	#Wait 5 minutes between each data collection
	time.sleep(300.0)

