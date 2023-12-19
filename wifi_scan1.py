import subprocess

grouped_blocks = {}

def read_file() :
	with open("blocked_signal.txt", 'r') as file:
		return [line.strip() for line in file.readlines()]
def write_file(ssid):
	with open("blocked_signal.txt", 'w') as file:
		file.write('\n'.join(ssid))

def block_function(ssid):
	grouped_networks = filter_blocked_wifi(scan_wifi())
	if ssid in grouped_networks:
		total_blocked_ssid = read_file() 
		total_blocked_ssid.append(ssid) 
		write_file(total_blocked_ssid)
		del grouped_blocks[ssid]
		print(f"Wifi signal {ssid} has been blocked successfully.")
	else:
		print(f"Wifi signal {ssid} is not found")
	print("-------------------------------------------------------------------")

def unblock_function(ssid):
	total_blocked_ssid = read_file()
	if ssid in total_blocked_ssid:
		total_blocked_ssid.remove(ssid)
		write_file(total_blocked_ssid) 
		filter_blocked_wifi(scan_wifi())
		print(f"Wifi signal {ssid} has been unblocked successfully.")
	else:
		print(f"Wifi signal {ssid} is not found in the blocked wifi list")
	print("-----------------------------------------------------------------------") 

def display_blocked_wifi():
	total_blocked_wifi = read_file()
	if len(total_blocked_wifi)==0:
		print("Nothing to display -> Blocked wifi list is empty")
	else:
		print("Blocked wifi list: ") 
		for i in total_blocked_wifi:
			print(i) 
	print("-----------------------------------------------------------------------")

def reset():
	subprocess.check_output(['rm', 'blocked_signal.txt'])
	subprocess.check_output(['touch','blocked_signal.txt'])
	print("All blocked wifi signals have been successfully unblocked.")
	print("------------------------------------------------------------------------")

def scan_wifi():
	scan_result = subprocess.check_output(['sudo', 'iwlist', 'wlan0', 'scan']) 
	scan_result = scan_result.decode('utf-8') 
	return scan_result

def filter_blocked_wifi(scan_result):
	wifi_blocks = scan_result.split('Cell') 
	total_blocked_ssid = read_file() 
	filtered_blocks = [] 
	for block in wifi_blocks: 
		if not any(ssid in block for ssid in total_blocked_ssid):
			filtered_blocks.append(block)

	grouped_networks = {}
 
	for block in filtered_blocks:
		ssid = extract_data(block, 'ESSID:') 
		signal_strength = extract_data(block, 'Signal level=') 
		frequency = extract_data(block, 'Frequency:') 
		encryption = extract_data(block, 'Encryption key:') 
		key = ssid
 
		if key not in grouped_networks:
			grouped_networks[key] = {'Signal Strength' : [], 'Frequency' : [], 'Encryption key' : [] } 
		grouped_networks[key]['Signal Strength'].append(signal_strength) 
		grouped_networks[key]['Frequency'].append(frequency) 
		grouped_networks[key]['Encryption key'].append(encryption)

		if key not in grouped_blocks:
        		grouped_blocks[key] = {'blocks' : []}
		grouped_blocks[key]['blocks'].append(block)

	return grouped_networks

def display_result(grouped_networks):
	print("Available Wi-Fi Signals are: ") 
	print("-----------------------------------------------------------------------------------------") 
	valid_keys = [key for key in grouped_networks if key is not None] 
	for key in valid_keys:
		for i in range(len(grouped_networks[key]['Signal Strength'])):
			print("SSID: ", key)
			print("Signal Strength: ", grouped_networks[key]['Signal Strength'][i])
			print("Frequency: ", grouped_networks[key]['Frequency'][i])
			print("Encryption key: ", grouped_networks[key]['Encryption key'][i],"\n")
		print("-----------------------------------------------------------------------------------------")

def extract_data(block, var):
	start_index = block.find(var)
	if start_index != - 1:
		start_index += len(var)
		end_index = block.find('\n', start_index)
		if end_index != - 1:
			return block[start_index:end_index].strip('"')

while (True):
	option = input('''
                    Enter 's' to scan all the available wifi signals: 
                    Enter 'b' to block a wifi signal:
                    Enter 'u' to unblock a wifi signal:
                    Enter 'l' to list down all the blocked wifi signals:
                    Enter 'm' to know more about a wifi signal:
		    Enter 'r' to remove all blocked wifi signals:
                    Enter 'q' to stop the program:\n		''')
	print("-------------------------------------------------------------------------------------------------------")

	if option == "s":
		print("scanning available wifi signals.....")
		scan_result = scan_wifi()
		filter_result = filter_blocked_wifi(scan_result)
		display_result(filter_result)

	elif option == "b":
		x = input("Enter ssid which you want to block: ") 
		block_function(x)

	elif option == 'u':
		ssid = input("Enter ssid which you want to unblock: ") 
		unblock_function(ssid)

	elif option == 'l':
		display_blocked_wifi()

	elif option == "m":
		ssid = input("Enter ssid whose details you want: ") 
		if ssid in grouped_blocks:
			block = grouped_blocks[ssid]['blocks'] 
			for x in block:
				print(x)
		else:
			print(f"Wifi signal {ssid} is not found, please check if it is present in the available wifi list or not") 
		print("--------------------------------------------------------------------------------------------------")

	elif option=='r':
		reset()

	elif option == "q":
		break

	else:
		print("Invalid input, choose from the given options.") 
		print("-----------------------------------------------------------------------------------------------------------")
