import subprocess
blocked_ssids = []
def scan_wifi():
	result = subprocess.check_output(['sudo','iwlist','wlan0','scan'])
	result = result.decode('utf-8')
	filter_blocked_wifi(result)

def filter_blocked_wifi(scan_result):
	wifi_blocks = scan_result.split('Cell ')
	filtered_blocks = [block for block in wifi_blocks if not any(blocked_ssid in block for blocked_ssid in blocked_ssids)]
	for block in filtered_blocks:
		ssid = find_value(block,'ESSID:')
		signal_strength = find_value(block,'Signal level=')
		frequency = find_value(block,'Frequency:')
		print("-----------------------------------------------------------------")
		print(f"SSID: {ssid}, Signal Strength: {signal_strength}, Frequency: {frequency}")

def find_value(block,key):
	start_index = block.find(key)
	if start_index != -1:
		start_index += len(key)
		end_index = block.find('\n',start_index)
		if end_index != -1:
			return block[start_index:end_index].strip()


while(True):
	print("Do you want to block any wifi: yes/no ")
	option = input()
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

