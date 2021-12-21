from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

URL = 'https://covid19.who.int/region/searo/country/np'
r = requests.get(URL)
soup = bs(r.text, 'html.parser')

confirmed_cases=soup.find_all('span',{'data-id':'metric'})[0].text
total_death =soup.find_all('span',{'data-id':'metric'})[1].text
print(f'Total confirmed cases: {confirmed_cases}')
print(f'Total death cases: {total_death}')

URL = 'https://covid19.who.int/table'
r = requests.get(URL)
soup = bs(r.text, 'html.parser')

country_div = soup.find('div',{'class':'tbody'}).find_all('div',{'role':'row'})
country_div = country_div[2:12][::-1]


master_list = []
for div in country_div:
    country_name = div.find('div',{'role':'cell'}).text
    total_cumulative = div.find_all('div',{'role':'cell'})[1].text
    data = {
        'country':country_name,
        'total_cumulative':total_cumulative
    }
    master_list.append(data)

print(master_list)