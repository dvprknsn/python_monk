#06_04_MWIS_scraping

import urllib.request

u = 'http://www.mwis.org.uk/text/PD'
f = urllib.request.urlopen(u)
contents = str(f.read())
f.close()
i = 0
while True:
    i = contents.find('<p', i)
    if i == -1:
        break
    #Find the next two '>' after productTitle', i)
    i = contents.find ('>', i+1)
    #Find the first '<' after the two '>'s
    j = contents.find ('</p>', i+1)
    title = contents[i:j]
    print(title)
