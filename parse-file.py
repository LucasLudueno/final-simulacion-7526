import json
import requests
from time import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

def divide_chunks(l, n):      
    for i in range(0, len(l), n):  
        yield l[i:i + n] 


def get_url(url):
    print url
    try:
        response = requests.get(url)
        print response.status_code
        if response.status_code < 400:
            return url
    except:
        print "error"
        return 0

def valid_url(url):
    if url != 0:
        return True
    else:
        return False


start = time()

# Iterate url files and extract urls
urls = []
file = open("little-file-with-urls.txt", "r")
for line in file:
    url = line.split()[2]
    urls.append(url)

# Try to access to each url and save only the ones than are accessibles
# pool = ThreadPoolExecutor(10)
# futures = [pool.submit(get_url, url) for url in urls]
# results = [r.result() for r in as_completed(futures)]


# results = []
# for array in list(divide_chunks(urls, 50)):
#     with ThreadPoolExecutor(max_workers=50) as executor:
#         result = executor.map(get_url, array)
#         results.extend(result)

results = []
with ThreadPoolExecutor(max_workers=50) as executor:
    results = executor.map(get_url, urls)



# Save results in a file
valid_urls = list(filter(lambda x: x != 0 and x != None, results))
urls_map = {}
for x in range(len(valid_urls)):
    urls_map[x] = { "url": valid_urls[x] }

with open("urls_maps.json", "w") as file:
    file.write(json.dumps(urls_map))

end = time()
# 6.02554711501 min cada 10000. result 320

print "Total time: %s min" % ((end - start) / 60.0)
