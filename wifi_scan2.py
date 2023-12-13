import subprocess
blocked_ssids = []
def scan_wifi():
	result = subprocess.check_output(['sudo','iwlist','wlan0','scan'])
	result = result.decode('utf-8')
	filter_blocked_wifi(result)

def filter_blocked_wifi(scan_result):
	wifi_blocks = scan_result.split('Cell ')
	filtered_blocks = [block for block in wifi_blocks if not any(blocked_ssid in block for blocked_ssid in blocked_ssids)]
	grouped_networks = {}
	for block in filtered_blocks:
		ssid = find_value(block,'ESSID:')
		signal_strength = find_value(block,'Signal level=')
		frequency = find_value(block,'Frequency:')
		key = ssid
		if key not in grouped_networks:
			grouped_networks[key] = {'Signal Strength': [], 'Frequency': []}
		grouped_networks[key]['Signal Strength'].append(signal_strength)
		grouped_networks[key]['Frequency'].append(frequency)

	print("Available Wi-Fi Signals: ") 
	for key in grouped_networks:
		if key!=None:
			print("SSID: ",key)
			print("Signal Strength: ",grouped_networks[key]['Signal Strength'])
			print("Frequency: ",grouped_networks[key]['Frequency'])
			print("-----------------------------------------------------------------------------------------")

def find_value(block,key):
	start_index = block.find(key)
	if start_index != -1:
		start_index += len(key)
		end_index = block.find('\n',start_index)
		if end_index != -1:
			return block[start_index:end_index].strip()


while(True):
	option = input("Do you want to block a WiFi? (yes/no or write 'more' if you want to see more details of a WiFI): "  )
	if option=="yes":
		print("Enter SSID which you want to block: ")
		x = input()
		blocked_ssids.append(x)
		scan_wifi()
	elif option=="no":
		scan_wifi()
	else :
		print("Run the program again to get the output")
		break


