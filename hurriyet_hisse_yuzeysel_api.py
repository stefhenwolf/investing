import urllib.request,json
import ast
import pandas as pd
from urllib.error import HTTPError
import datetime
import shutil 


today = datetime.date.today().strftime("%d/%m/%Y")
today2 = datetime.date.today().strftime('%d-%m-%Y')


dataframe = []

url3 = "https://bigpara.hurriyet.com.tr/api/v1/borsa/hisseyuzeysel/AEFES"
k = urllib.request.urlopen(url3).read().decode("UTF-8")
m = json.loads(k)["data"]["hisseYuzeysel"]

dataframe = pd.DataFrame([m], columns=m.keys())

with urllib.request.urlopen("https://bigpara.hurriyet.com.tr/api/v1/hisse/list") as url:
    a = url.read().decode("UTF-8")
    b = ast.literal_eval(a)["data"]
    
    for i in b:

        try:
            print("{} {}".format(i["id"],i["kod"]))
            str1 = i["kod"]
            url2 = "https://bigpara.hurriyet.com.tr/api/v1/borsa/hisseyuzeysel/{}".format(str1)
    
            c = urllib.request.urlopen(url2).read().decode("UTF-8")
            d = json.loads(c)["data"]["hisseYuzeysel"] 

            dataframe = dataframe.append(pd.DataFrame([d],columns=d.keys()))

        except AttributeError:
            pass

        except urllib.error.HTTPError as err:
            print(err.code)
            

    print(dataframe)

dataframe.to_excel(today2+"hurriyet-hisse-yuzeysel-api.xlsx", sheet_name="genel")

path = 'C:/Users/sedat/OneDrive/Masaüstü/bist'

source = 'C:/Users/sedat/OneDrive/Masaüstü/bist/'+today2 +'hurriyet-hisse-yuzeysel-api'+'.xlsx'

destination = 'C:/Users/sedat/OneDrive/Masaüstü/bist/hurriyet_hisse_yuzeysel_api'

dest = shutil.move(source, destination) 



    

    







 