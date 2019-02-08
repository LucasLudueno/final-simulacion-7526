import re
import json
import numpy as np
import BeautifulSoup

from urlparse import urlparse
from PageRank import PageRank

class URLResolver:
    """ Module to resolve urls into a html content and link them with other into a url graph"""

    """ Given a map of urls like: { "0": { "url": "http://www.google.com/", "content": "html content" }, ...  }
        this function explores all the urls content and computes a page rank for each one.

        Example response: { "0": {"url": "http://www.google.com/", content: "html content", page_rank: 0.9 }, ...  }
    """
    def load_page_rank(self, urls_map, urls_map_file):
        # Build a graph of urls
        urls_graph = self.make_urls_graph(urls_map)

        # Calculate the page rank for each page
        pageRank = PageRank()
        link_matrix = pageRank.build_matrix(urls_graph)
        page_rank_values = pageRank.calculate_page_rank(link_matrix)
        
        # Add the page rank field to urls_map object
        for x in range(len(page_rank_values)):
            if str(x) in urls_map:
                urls_map[str(x)]["page_rank"] = page_rank_values[x]
        
        # Save the calculated map into a file
        with open(str(urls_map_file) + ".page_rank", "w") as file:
            file.write(json.dumps(urls_map))
        
        return urls_map


    """ Given a map of urls like: { "0": { "url": "http://www.google.com/", "content": "html content" }, ...  }
        this function explores all the urls content and makes a graph where each node represents an url and 
        each edge represents a link between two pages.

        Response: a matrix that represents a graph
            - Each value is 1 when exists a link between two nodes (urls)
            - Each value is 0 when no exists a link between two nodes (urls)
    """
    def make_urls_graph(self, urls_map):
        links_cont = 0
        nodes_count = len(urls_map)
        graph = np.zeros([nodes_count, nodes_count])

        # Iterate each page url
        for number, url in urls_map.iteritems():
            main_base_url = self.get_base_url(url["url"])
            html = url["content"]
            links = self.get_url_links(html)

            # Iterate liks found into each page urls
            for link in links:
                if link != None:
                    base_url = self.get_base_url(link)

                    # Check if some link points to another page url
                    for ady_number, ady_url in urls_map.iteritems():
                        base_ady_url = self.get_base_url(ady_url["url"])

                        if base_url != "" and base_url == base_ady_url and base_url != main_base_url:
                            links_cont += 1
                            graph[int(number)][int(ady_number)] = 1
        
        print "Total links between pages: " + str(links_cont)
        return graph


    def get_base_url(self, url):
        return urlparse(url)[1].replace("www.", "")

    def get_url_links(self, html):
        soup = BeautifulSoup.BeautifulSoup(html)
        links = [link.get("href") for link in soup.findAll("a")]
        return links
