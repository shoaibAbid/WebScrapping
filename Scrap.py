import csv
from bs4 import BeautifulSoup 
from urllib.request import Request, urlopen




 
rank_page = 'https://socialblade.com/youtube/top/50/mostviewed'
request = Request(rank_page, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})
page = urlopen(request)
soup = BeautifulSoup(page, 'html.parser')
 
channels = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]
 
file = open('youtubers.csv', 'w')
writer = csv.writer(file)
 
# write title row
writer.writerow(['Username', 'Uploads', 'Views'])
 
for channel in channels:
    username = channel.find('div', attrs={'style': 'float: left; width: 350px; line-height: 25px;'}).a.text.strip()
    uploads = channel.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
    views = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()
 
    
    print (username + ' ' + uploads + ' ' + views)
    writer.writerow([username.encode('utf-8'), uploads.encode('utf-8'), views.encode('utf-8')])
 
file.close()