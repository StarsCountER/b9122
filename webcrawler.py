from bs4 import BeautifulSoup
import urllib.request
#from urllib.request import Request

seed_url = "https://www8.gsb.columbia.edu"

urls = [seed_url]    #queue of urls to crawl
seen = [seed_url]  #stack of urls seen so far
opened = []


maxNumUrl = 10; #set the maximum number of urls to visit (not to "see")
print("Starting with url="+str(urls))
while len(urls) > 0 and len(opened) < maxNumUrl:    #allow the domain to have less than max pages
    # DEQUEUE A URL FROM urls AND TRY TO OPEN AND READ IT: allow for interruption of connection
    try:
        curr_url=urls.pop(0)  #pick out the first
        print("num. of URLs in stack: %d " % len(urls))
        print("Trying to access= "+curr_url)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:  #only accepts exceptions that you're meant to catch
        print("Unable to access= "+curr_url)
        print(ex)
        continue    #skip code below

    # IF URL OPENS, CHECK WHICH URLS THE PAGE CONTAINS
    # ADD THE URLS FOUND TO THE QUEUE url AND seen
    soup = BeautifulSoup(webpage)  #creates object soup
    # Put child URLs into the stack
    for tag in soup.find_all('a', href = True): #find tags with links (anchored tags)
        childUrl = tag['href'] #extract just the link
        o_childurl = childUrl #original child\
        # smart join regarding the domain. eg: may have diff url to the same address;
        # if diff domain, return the original
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        print("seed_url=" + seed_url)
        print("original childurl=" + o_childurl)
        print("childurl=" + childUrl)
        print("seed_url in childUrl=" + str(seed_url in childUrl))
        print("Have we seen this childUrl=" + str(childUrl in seen))
        # make sure the childUrl is within the domain; and append to urllist only if haven't seen it. if seen then must have been appended
        # opened: have done with the page; seen: just have "noticed"
        if seed_url in childUrl and childUrl not in seen:
            print("***urls.append and seen.append***")
            urls.append(childUrl)
            seen.append(childUrl)
        else:
            print("######")

print("num. of URLs seen = %d, and scanned = %d" % (len(seen), len(opened)))

print("List of seen URLs:")
for seen_url in seen:
    print(seen_url)