import time

import requests

token = "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"
url = "https://api.github.com/search/code?q=addClass+in:file"

url2 = "https://api.github.com/search/code?q=endsWith+in:file"

headers = {
  'Authorization': ('Token ' + token)
}

response = requests.request("GET", url, headers=headers).json()

print(response)
print(response['total_count'])
print()

print('start sleep')
time.sleep(10)
print('wake up')

response2 = requests.request("GET", url2, headers=headers).json()

print(response2)
print(response2['total_count'])
print()