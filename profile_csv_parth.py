import requests
import pandas as pd

df = pd.DataFrame()
ids=[]
all_ids=[]

region = input("Select the index number as per your account region: \n [1] eu \n [2] in \n [3] sg \n")

if region=="1" or region =="eu": 
  url = "https://api.clevertap.com/1/profiles.json"
elif region == "2" or region =="in":
  url = "https://in.api.clevertap.com/1/profiles.json"
elif region == "3" or region =="sg":
  url ="https://sg.api.clevertap.com/1/profiles.json"


acc_id = input("Enter your CleverTap account ID: \n")
pass_code = input("Enter the pass-code: \n")


payload = "{\n    \"event_name\": \"-1\",\n    \"common_profile_properties\": {\n        \"profile_fields\": [\n            {\n                \"name\": \"bad_identities\",\n                \"operator\": \"exists\",\n                \"value\": \"-1\"\n            }\n        ]\n    }\n}"
headers = {
    'X-CleverTap-Account-Id': acc_id,
    'X-CleverTap-Passcode': pass_code,
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

cursor = response.json()['cursor']
next_cursor = cursor
while next_cursor is not None:
  params =(('cursor', next_cursor),)
  response = requests.get(url = url+"?cursor="+next_cursor,headers = headers)
  print(response, response.content)
https://github.com/yash-kantharia/CSV-codes-Python-
  record = response.json()['records']
  if len(record)==0:
    break

  df = pd.read_json(response.content)
  for i in range (0,len(df)):
    for key,value in df.records[i].items():
      if key=="identity":
        ids.append(value)
      if key =="all_identities":
        all_ids.append(str(value))

  next_cursor = response.json()['next_cursor']

df_1 = pd.DataFrame(ids)
df_1.columns=["Identity"]

df_1 = pd.DataFrame(ids)
df_1.columns=["Identity"]

result = pd.concat([df_1,df_2],axis=1)
result.head(10)

save_csv = input("Do you want to save this list as a csv in the pwd? y/n")
if save_csv="y":
  result.to_csv("result.csv")
