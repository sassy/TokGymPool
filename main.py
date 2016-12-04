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
    datas = []
    for i, td in enumerate(trs.findAll('td')):
        if i != 4:
            schedule_string += td.text.strip()
            datas.append(td.text.strip())
            schedule_string += ' / '
        else:
            schedule_string += '\n'
            schedule_string += 'https://www.tef.or.jp/tmg/opening_popup.jsp?doSearch=true&start_year='
            schedule_string += str(now.year)
            schedule_string += '&start_month='
            schedule_string += datas[0]
            schedule_string += '&start_day='
            schedule_string += datas[1]
    if len(schedule_string) > 0:
        print(schedule_string)
