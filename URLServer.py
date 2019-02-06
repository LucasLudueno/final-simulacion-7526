import re
import json
import numpy as np

from numpy.linalg import matrix_power
from UrlWrapper import UrlWrapper

class URLServer:
    """ Module to manage url content """

    """ Given a map of urls like: { "0": { "url": "http://www.google.com/" }, ...  }
        this function try to get each url content and save this content in the given map.

        Example response: { "0": {"url": "http://www.google.com/", content: "html content" }, ...  }
    """
    def load_content(self, urls_map, urls_map_file):
        urls = [{ "number": number, "url": url["url"] } for number, url in urls_map.iteritems()]

        # Get urls that exist
        valid_urls = UrlWrapper().get_urls_content(urls)

        # Add the content field to the urls_map
        for url in valid_urls:
            current = urls_map[url["number"]]
            current["content"] = url["content"]

        # Save the calculated map into a file
        with open(str(urls_map_file) + ".content", "w") as file:
            file.write(json.dumps(urls_map))

        return urls_map
