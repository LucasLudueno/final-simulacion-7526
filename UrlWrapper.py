import numpy as np
import requests
import copy
from numpy.linalg import matrix_power
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

class UrlWrapper:
    """ """

    def head_url(self, url):
        try:
            response = requests.head(url)
            if response.status_code < 400:
                return True
            return False
        except:
            return False

    def get_url_content(self, url_map):
        print "URL" + url_map["url"]
        try:
            response = requests.get(url_map["url"])
            if response.status_code < 400:
                url_map["content"] = response.text
            else:
                print "error"
                url_map["content"] = ""
        except:
            print "error"
            url_map["content"] = ""
        
        return url_map

    def get_urls_content(self, urls):
        # pool = ThreadPoolExecutor(10)
        # futures = [pool.submit(self.get_url_content, url) for url in urls]
        # results = [r.result() for r in as_completed(futures)]

        results = []
        with ThreadPoolExecutor(max_workers=25) as executor:
            results = executor.map(self.get_url_content, urls)

        # valid_urls = list(filter(lambda x: x["content"] != "", results))

        return results
