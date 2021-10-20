from bs4 import BeautifulSoup
import urllib.request

seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"
domain = "https://www.federalreserve.gov/newsevents/pressreleases"

test= "https://www.federalreserve.gov/newsevents/pressreleases/monetary20211013a.htm"

req = urllib.request.Request(test, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urllib.request.urlopen(req).read()
soup = BeautifulSoup(webpage)  # creates object soup
pdf_urls=[]

content = soup.get_text().lower()
print(content)

for tag in soup.find_all('a', href=True):  # find tags with links (anchored tags)
    childUrl = tag['href']  # extract just the link
    print(childUrl)
    if childUrl[-4:] == ".pdf":
        if childUrl not in pdf_urls:
            pdf_urls.append(childUrl)