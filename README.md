
**packages/library used**
```
1. Requests
2. BeautifulSoup
3. Pandas
```
------------------------------
Process to run this project.

**step 1**: git clone `https://github.com/Pox420/growbydata.git`

**step 2**: `cd growbydata` and type `pip install -r requirements.txt`

**step 3**: type `python grow.py`


---------------------------------------


**Project explaination**
```
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
```
- import `beautifulsoup` `pandas` and `requests` - `requests` library will request the `URL`, `BeautifulSoup` will parse the `response` object to `HTML` format
and store it on variable/object.

- `find_all()` function will search the combination on *soup* object. It is used to find more than one data object.

- `find()` function will search only single combination on *soup* object.

- All the result are stored in variable after using the `find_all()` and `find()` function.

- `pandas` library is used to organize the data in easy way, and also help to import/export on different files like `CSV`,`JSON` and more.
