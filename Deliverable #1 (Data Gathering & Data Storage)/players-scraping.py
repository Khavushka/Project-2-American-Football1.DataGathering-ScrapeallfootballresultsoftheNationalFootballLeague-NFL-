# Web Scrabing of Project 2 (American Football)

# These are the modules we are working with 
import urllib
import time

# This is what hides our iddentity when we are webscrabing, to avvoid getting banned from the site.
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "utf-8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0"
} 

# We use a for loop, to go through the pages we need to "download" and save them as html files.
# We use try to make the scipt countinue in case there is an error, and except to accept the error, therefore continuing.
for link in range(1,52):
    try:
        url = 'https://www.pro-football-reference.com/years/'+str(1970+link)+'/games.htm'
        request = urllib.request.Request( url, None, headers )
        response = urllib.request.urlopen( request )
        with open('data/'+'page'+str(link+1)+'.html', 'w') as f:
            f.write(str(response.read().decode('utf-8')))
        time.sleep(10)
    except urllib.error.HTTPError:
        print("No page with start "+" found")