import time

import requests

token = "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"

# search_final_url = 'https://api.github.com/search/code?q=something+in:file+language:java'
#
# url2 = 'https://api.github.com/search/code?q=endsWith'
#
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# response = requests.get(url2, verify='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')
# # print("Status code: ", response.status_code)
# response_dict = response.json()
# # print(response_dict.keys())
# # print(response_dict['total_count'])
# print(response_dict)

url = "https://api.github.com/search/code?q=addClass+in:file"

url2 = "https://api.github.com/search/code?q=endsWith+in:file"

headers = {
  'Authorization': 'Token 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'
}

response = requests.request("GET", url, headers=headers).json()

print(response)
print(response['total_count'])
print()

time.sleep(10)

response2 = requests.request("GET", url2, headers=headers).json()

print(response2)
print(response2['total_count'])
print()