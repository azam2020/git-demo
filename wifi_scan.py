import subprocess
blocked_ssids = []
def scan_wifi():
	result = subprocess.check_output(['sudo','iwlist','wlan0','scan'])
	result = result.decode('utf-8')
	return result

def filter_blocked_wifi(scan_result):
	wifi_blocks = scan_result.split('Cell  ')
	filtered_blocks = [block for block in wifi_blocks if not any(blocked_ssid in block for blocked_ssid in blocked_ssids)]
	filtered_result = 'Cell '.join(filtered_blocks)
	return filtered_result

print("Result before blocking any wifi")
wifi_info = scan_wifi()
print(wifi_info)
x = input("Enter the ssid which you want to block:")
blocked_ssids.append(x)
filtered_wifi = filter_blocked_wifi(wifi_info)
print("Result after blocking a wifi")
print(filtered_wifi)
