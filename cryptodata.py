import csv
import requests

url='http://api.coincap.io/v2/assets'

headers={
    'Accept':'application/json',
    'Content-Type':'application/json'
}
response=requests.request("GET",url,headers=headers,data={})
jsonfile=response.json()

actualdata=[]
csvheading=['ID','Rank','Symbol','Name','Price(USD)','Max Supply']



for x in jsonfile['data']:
    listing=[x['id'],x['rank'],x['symbol'],x['name'],x['priceUsd'],x['maxSupply']]
    actualdata.append(listing)

with open('cryptodata.csv','w',encoding='UTF8',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(csvheading)
    writer.writerows(actualdata)

print("Conversion Completed")