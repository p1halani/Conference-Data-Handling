import requests
import pprint
from conference import Conference

url = "https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences"
try: 
    response = requests.get(url, timeout=(5, 14)) 
    response.raise_for_status()                 # Raise error in case of failure 
except requests.exceptions.HTTPError as httpErr: 
    print ("Http Error:",httpErr) 
except requests.exceptions.ConnectionError as connErr: 
    print ("Error Connecting:",connErr) 
except requests.exceptions.Timeout as timeOutErr: 
    print ("Timeout Error:",timeOutErr) 
except requests.exceptions.RequestException as reqErr: 
    print ("Something Else:",reqErr)
else:
    print("\n\n================================================================")
    print("Successfully Fetched Data!!!!!!")
    pprint.pprint(response.json())