from datetime import date
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

now = date.today()
url = 'https://www.tef.or.jp/tmg/pool_top.jsp?tabNumber=2&doSearch=true'
url += '&start_year='
url += str(now.year)
url += '&start_month='
url += str(now.month)
url += '&start_day='
url += str(now.day)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', class_='shisetsu_schedule')
table = div.find('table', class_='base_table01')
for trs in table.findAll('tr'):
    schedule_string = '';
    for i, td in enumerate(trs.findAll('td')):
        if i != 4:
            schedule_string += td.text.strip()
            if i != 3:
                schedule_string += '/'
    print(schedule_string)
