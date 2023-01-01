#!/usr/bin/python3

import subprocess

def ping_sweep(start_ip, end_ip):
  results = []
  for ip in range(start_ip, end_ip+1):
    ret = subprocess.call(['ping', '-c', '1', '-W', '1', str(ip)], stdout=subprocess.DEVNULL)
    if ret == 0:
      results.append(f"{ip_to_str(ip)} is reachable")
    else:
      results.append(f"{ip_to_str(ip)} is not reachable")
  return results

def ip_to_str(ip):
  return '.'.join([str((ip >> (8 * (3 - i))) & 0xff) for i in range(4)])

# IP Range scan
print("------Made by Cr7pt0nic aka NullSEC------")
start_ip_str = input("Enter the starting IP address: ")
end_ip_str = input("Enter the ending IP address: ")

# Convert the IP addresses to numerical values
start_ip = sum([int(part) << (8 * (3 - i)) for i, part in enumerate(start_ip_str.split('.'))])
end_ip = sum([int(part) << (8 * (3 - i)) for i, part in enumerate(end_ip_str.split('.'))])

results = ping_sweep(start_ip, end_ip)

file_name = input("Enter the file name: ")
with open(file_name, 'w') as f:
  for result in results:
    f.write(result + '\n')
