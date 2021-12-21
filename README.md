
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

- import `beautifulsoup` `pandas` and `requests` - `requests` library will request the `URL`, `BeautifulSoup` will parse the `response` object to `HTML` format
and store it on variable/object.

- `find_all()` function will search the combination on *soup* object. It is used to find more than one data object.

- `find()` function will search only single combination on *soup* object.

- All the result are stored in variable after using the `find_all()` and `find()` function.

- `pandas` library is used to organize the data in easy way, and also help to import/export on different files like `CSV`,`JSON` and more.

----------------------
**Output of this project**
```
[{'country': 'Spain', 'total_cumulative': '5,422,169'},
{'country': 'Iran (Islamic Republic of)', 'total_cumulative': '6,170,979'},
{'country': 'Germany', 'total_cumulative': '6,809,622'},
{'country': 'France', 'total_cumulative': '8,382,498'}, 
{'country': 'Turkey', 'total_cumulative': '9,171,119'},
{'country': 'Russian Federation', 'total_cumulative': '10,241,812'},
{'country': 'The United Kingdom', 'total_cumulative': '11,361,391'}, 
{'country': 'Brazil', 'total_cumulative': '22,204,941'}, 
{'country': 'India', 'total_cumulative': '34,746,838'}, 
{'country': 'United States of America', 'total_cumulative': '50,415,400'}]
```
