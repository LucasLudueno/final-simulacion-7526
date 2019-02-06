import re
import sys
import json
import BeautifulSoup
import numpy as np

from PageRank import PageRank
from Searcher import Searcher
from URLServer import URLServer
from URLResolver import URLResolver
from UrlWrapper import UrlWrapper


""" This module represents the engine of a Google search.
    It allows you to search into a web pages and retrieves the pages that matches with
    the searches using the PageRank algorithm of Google.

    The two parameters that receives is the search_type and a file path of a maps urls that
    should have a content like this:
    { "0": { "url": "http://www.google.com/", "content": "html content", page_rank: 0.9 }, ...  }

    where the only required field if "url". If the content or the page rank is not added, this module
    will populate this fields.

    After all fields are populated, you can search into this pages like Google does. Enjoy!
"""
def main(urls_map_file, search_type = "content"):
    urls_map = {}
    urls_content = {}
    urls_graph = []

    print "Loading Page Urls..."
    with open(urls_map_file) as json_file:  
        urls_map = json.load(json_file)

    print "Loading Page Content..."
    if not "content" in urls_map["0"]:
        urlServer = URLServer()
        urls_map = urlServer.load_content(urls_map, urls_map_file) 

    print "Loading Page Rank..."
    if not "page_rank" in urls_map["0"]:
        urlResolver = URLResolver()
        urls_map = urlResolver.load_page_rank(urls_map, urls_map_file) 

    print "Lets make google searches... \n"
    searcher = Searcher(urls_map)

    user_input = raw_input('Write some text to search (write "exit" to quit the program): ')
    while not user_input == "exit":
        print "Searching pages..."
        match_urls = searcher.search(user_input, search_type)

        if len(match_urls) == 0:
            print "No url match your search"
        else:
            print "Search result (URL - Page Rank)"
            for x in range(len(match_urls)):
                print str(x) + ". " + match_urls[x][0] + " - " + str(match_urls[x][1])

        print "\n"

        user_input = raw_input('Write some text to search (write "exit" to quit the program): ')
    
    print "Bye bye!!"


if __name__ == "__main__":
    search_type = "title"
    if len(sys.argv) == 3:
	    search_type = sys.argv[2]
    sys.exit(main(sys.argv[1], search_type))
