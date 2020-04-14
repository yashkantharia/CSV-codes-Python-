import pandas as pd
import regex as re

file_up = raw_input("Enter path of CSV uploaded")
file_down = raw_input("Enter path of CSV downloaded from the CT dashboard")

df1 = pd.read_csv(file_up)
df2 = pd.read_csv(file_down, skiprows=1)

uploaded_id = df1.identity
uploaded_id = uploaded_id.values.tolist()

df2_identity = df2.Identity

identities_ct =[]

for i in range (0,len(df2_identity)):
  x = re.split(",",df2_identity[i])
  for j in range(0,len(x)):
    identities_ct.append(x[j])
    
diff = []
found = 0 

for i in range(0,len(uploaded_id)):
  if uploaded_id in identities_ct:
    found = found + 1
  else:
    diff.append(uploaded_id[i])
    
print("Number of records not found "+str(found))

option = raw_input("Do you want to save the difference CSV in the pwd? y/n")

if option=="y":
  df3 = pd.DataFrame(diff)
  df3.columns=["Identity"]

  df3.to_csv("diff_list.csv")


    




