# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import requests
from bs4 import BeautifulSoup
#import scraperwiki
from datetime import datetime
import pytz
req = requests.get('http://www.shunon.com.hk/pricing.php')
soup = BeautifulSoup(req.content, 'html.parser')
table = soup.find_all('table', {'class': 'Font16Boldc'})[1]
element = table.find_all('p')[0]
text = element.text.split()
titles = [text[i] for i in (0, 2, 4, 6)]
values = [int(text[i].replace('$', '').replace(',', ''))
                  for i in (1, 3, 5, 7)]
hkt = pytz.timezone('Asia/Hong_Kong')
dt = datetime.now().replace(tzinfo=hkt).date()
data = {titles[i]: values[i] for i in range(0, 4)}
data['date'] = dt
print(data)
scraperwiki.sqlite.save(unique_keys=['date'], data=data)
