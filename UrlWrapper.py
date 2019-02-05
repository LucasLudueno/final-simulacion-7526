import numpy as np
import requests
import copy

from numpy.linalg import matrix_power
from concurrent.futures import ThreadPoolExecutor, wait, as_completed


class UrlWrapper:
    """ Module to fetch urls and get its content """

    """ Head urls to check it exists or not
    """
    def head_url(self, url):
        try:
            response = requests.get(url, timeout = 3)
            if response.status_code < 400:
                return url
            return False
        except:
            return False


    """ Head urls to check it exists or not and return only the valid ones
    """
    def head_urls_content(self, urls, workers = 25):
        results = []
        with ThreadPoolExecutor(max_workers = workers) as executor:
            results = executor.map(self.head_url, urls)

        valid_urls = list(filter(lambda x: x != False, results))
        return valid_urls


    """ Given a map of urls like: { "url": "http://google.com" }
        this function try to get each url content and save this content in the given map.
        Urls that takes more than 3 seconds in retrieve their content, will be discarded.
        (That is to not deteriorate the proyect performance)

        Example response: { "url": "http://google.com", content: "html content" }
    """
    def get_url_content(self, url_map):
        try:
            response = requests.get(url_map["url"], timeout = 3)
            if response.status_code < 400:
                url_map["content"] = response.text
            else:
                url_map["content"] = ""
        except:
            url_map["content"] = ""
        
        return url_map


    """ Given an array of urls like: [{ "number": 2, "url": "http://google.com" }]
        this function try to get each url content and save this content in the given array.

        Example response: [{ "number": 2, "url": "http://google.com", content: "html content" }]
    """
    def get_urls_content(self, urls, workers = 25):
        results = []
        with ThreadPoolExecutor(max_workers = workers) as executor:
            results = executor.map(self.get_url_content, urls)

        return results
