import sys
import json
import requests
sys.path.append('../')

from UrlWrapper import UrlWrapper
from time import time
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


start = time()

# Iterate url files and extract urls
file = open("little-original-file-california.txt", "r")
urls = [line.split()[2] for line in file]

# Get only urls that exist
valid_urls = UrlWrapper().head_urls_content(urls)

# Save results in a file
urls_map = {}
for x in range(len(valid_urls)):
    urls_map[x] = { "url": valid_urls[x] }

with open("urls_maps.pepe.json", "w") as file:
    file.write(json.dumps(urls_map))

end = time()

print "Total time: %s min" % ((end - start) / 60.0)
