# Measure clock
#http://www.nielsmayer.com/bin/view/Raspberry+Pi/measure+overclock+frequency+with+vcgencmd+measure_clock
stats = [
	'/opt/vc/bin/vcgencmd measure_temp',
	'/opt/vc/bin/vcgencmd measure_clock core'
]

for stat in stats:
	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	getStat = os.popen(stat).readline().strip()

	if "error" in line:
		print "Error reading getStat"
	else:
		temp = line.split('=')[1].split("'")[0]
		print temp