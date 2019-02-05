import re
import numpy as np
import BeautifulSoup

from numpy.linalg import matrix_power

class Searcher:
    """ Module to search phrases into pages and sorting them by its page rank """

    def __init__(self, urls_map):
       self.urls_map = urls_map

    """ Given a text to search and a map of urls like:
        { "0": { "url": "http://www.google.com/", "content": "html content", page_rank: 0.9 }, ...  }
        this function search the text into the content (or the title) of the urls and return only the pages
        that matches with the text. The pages are sorted by its page rank

        Example response: [(url1, 0.88999), (url2, 0.888222)
    """
    def search(self, text_to_search, search_type = "title"):
        match_urls = []
        for url in self.urls_map.values():
            # Extract url content
            content = url["content"]
            soup = BeautifulSoup.BeautifulSoup(content.lower()) # TODO: MAKE IT OUT

            # Search by title or content
            if search_type == "title":  
                has_title = soup.html and soup.html.head and soup.html.head.title and soup.html.head.title.string
                if has_title and text_to_search in soup.html.head.title.string:
                    match_urls.append((url["url"], url["page_rank"]))

            else:
                if soup.find(text=re.compile(text_to_search)) != None:
                    match_urls.append((url["url"], url["page_rank"]))

        # Sort urls that have matched with the text_to_search
        match_urls.sort(key=lambda url: url[1], reverse=True)
        return [url for url in match_urls]
