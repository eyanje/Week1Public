from urllib import request
from bs4 import BeautifulSoup
import pandas as pd

years = input('Year [2015-2016]: ') # 2015-2016
if (len(years) == 0):
    years = '2015-2016'
var_code = input('Code: ')

base_dir = f'https://wwwn.cdc.gov/Nchs/Nhanes/{years}/{var_code}.htm'

req = request.Request(base_dir, headers={'User-Agent': ''})

with request.urlopen(req) as documentation:
    soup = BeautifulSoup(documentation, features='html.parser')

print(soup.prettify())