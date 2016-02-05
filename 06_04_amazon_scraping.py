#06_04_amazon_scraping
#Doesn't work with current Amazon website

import urllib.request

u = 'http://www.amazon.com/s/ref=nb_sb_noss?field-keywords=raspberry+pi'
f = urllib.request.urlopen(u)
contents = str(f.read())
f.close()
i = 0
while True:
    i = contents.find('productTitle', i)
    if i == -1:
        break
    #Find the next two '>' after productTitle', i)
    i = contents.find ('>', i+1)
    i = contents.find ('>', i+1)
    #Find the first '<' after the two '>'s
    j = contents.find ('<', i+1)
    title = contents[i+2:j]
    print(title)
