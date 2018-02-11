import urllib.request as urllib2
from bs4 import BeautifulSoup

community_page = "https://community.qlik.com/thread/291003"

page = urllib2.urlopen(community_page)

soup = BeautifulSoup(page, 'html.parser')

my_content = soup.findAll('div', attrs={'class': 'jive-rendered-content'})

print(my_content)