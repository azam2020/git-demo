import subprocess
blocked_ssids = []
grouped_blocks = {}
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
		encryption = find_value(block,'Encryption key:')
		key = ssid
		if ssid!=None:
			key = ssid.strip('"')
		if key not in grouped_networks:
			grouped_networks[key] = {'Signal Strength': [], 'Frequency': [],'Encryption key':[]}
		grouped_networks[key]['Signal Strength'].append(signal_strength)
		grouped_networks[key]['Frequency'].append(frequency)
		grouped_networks[key]['Encryption key'].append(encryption)

		if key not in grouped_blocks:
			grouped_blocks[key] = {'blocks': []}
		grouped_blocks[key]['blocks'].append(block)
	print("Available Wi-Fi Signals are: \n") 
	print("-----------------------------------------------------------------------------------------")
	valid_keys = [key for key in grouped_networks if key is not None]
	for key in valid_keys:
		for i in range(len(grouped_networks[key]['Signal Strength'])):
			print("SSID: ",key)
			print("Signal Strength: ",grouped_networks[key]['Signal Strength'][i])
			print("Frequency: ",grouped_networks[key]['Frequency'][i])
			print("Encryption key: ",grouped_networks[key]['Encryption key'][i])
			print('\n')
		print("-----------------------------------------------------------------------------------------")

def find_value(block,key):
	start_index = block.find(key)
	if start_index != -1:
		start_index += len(key)
		end_index = block.find('\n',start_index)
		if end_index != -1:
			return block[start_index:end_index].strip()


while(True):
	s = input("Enter 'scan' if you want to scan available wifi signals or else 'stop' to stop the scanning: ")
	if s=="scan":
		scan_wifi()
		option = input("Do you want to block a WiFi? (yes/no or write 'more' if you want to see more details of a WiFI): "  )
		if option=="yes":
			print("Enter SSID which you want to block: ")
			x = input()
			blocked_ssids.append(x)
			del grouped_blocks[x]
			print(f"Wi-Fi signal {x} is  blocked, scan again to see the updated wifi signals")
		elif option=="no":
			pass
		elif option=="more":
			ssid_detail = input("Enter ssid whose details you want: ")
			if ssid_detail in grouped_blocks:
				block = grouped_blocks[ssid_detail]['blocks']
				for x in block:
					print(x)
			else:
				print(f"{ssid_detail} not found")
	elif s=="stop":
		break
	else :
		print("Invalid input")

