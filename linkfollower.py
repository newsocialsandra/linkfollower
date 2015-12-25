import urllib
from BeautifulSoup import *

url = raw_input('Enter url:')
count = raw_input('Enter count:')
count = int(count)
position = raw_input('Enter position:')
position = int(position)

while count > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    linklist = []
    for t in tags:
        linklist.append(t.get('href', None))
    url = linklist[position]
    count -= 1
    del linklist[:]

print 'The last url is', url