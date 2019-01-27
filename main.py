import re
import re
import sys
import json
import BeautifulSoup
import numpy as np
from PageRank import PageRank
from UrlWrapper import UrlWrapper
from urlparse import urlparse
from concurrent.futures import ThreadPoolExecutor, wait, as_completed

def main(urls_map_file, urls_graph_file = None):
    urls_map = {}
    urls_content = {}
    urls_graph = []

    # Read urls map file
    print "Loading Page Urls"
    with open(urls_map_file) as json_file:  
        urls_map = json.load(json_file)

    # Get each url content
    print "Loading Page Content"
    if not "content" in urls_map["0"]:
        urls_map = get_urls_content(urls_map)

        with open(str(urls_map_file) + ".content", "w") as file:
            file.write(json.dumps(urls_map))

    # Build graph
    print "Loading Page Rank"
    if not "page_rank" in urls_map["0"]:
        urls_graph = make_urls_graph(urls_map)

        # Build Page Rank for each page
        pageRank = PageRank()
        link_matrix = pageRank.build_matrix(urls_graph)
        page_rank_values = pageRank.calculate_page_rank(link_matrix)
        
        for x in range(len(page_rank_values)):
            urls_map[str(x)]["page_rank"] = page_rank_values[x]
        
        with open(str(urls_map_file) + ".page_rank", "w") as file:
            file.write(json.dumps(urls_map))

    print "Lets make google searches"
    user_input = ""
    while not user_input == "exit program":
        user_input = raw_input('write to search!: ')
        match_urls = search(urls_map, user_input)

        print "Search pages"
        for x in range(len(match_urls)):
            print str(x) + ". " + match_urls[x]

def get_urls_content(urls_map):
    urls = [{ "number": number, "url": url["url"] } for number, url in urls_map.iteritems()]
    valid_urls = UrlWrapper().get_urls_content(urls)

    for url in valid_urls:
        current = urls_map[url["number"]]
        current["content"] = url["content"]

    return urls_map

def make_urls_graph(urls_map):
    cont = 0
    nodes_count = len(urls_map)
    graph = np.zeros([nodes_count, nodes_count])

    for number, url in urls_map.iteritems():
        html = url["content"]
        soup = BeautifulSoup.BeautifulSoup(html)
        links = [link.get("href") for link in soup.findAll("a")]

        for link in links:
            if link != None:
                base_url = urlparse(link)[1].replace("www.", "")

                for ady_number, ady_url in urls_map.iteritems():
                    base_ady_url = urlparse(ady_url["url"])[1].replace("www.", "")

                    if base_url == base_ady_url and urlparse(link)[2] != urlparse(url["url"])[2]:
                        cont += 1
                        graph[int(number)][int(ady_number)] = 1
    
    # print "TOTAL"
    # print cont
    return graph

def search(urls_map, text_to_search):
    match_urls = []
    for url in urls_map.values():
        content = url["content"]
        soup = BeautifulSoup.BeautifulSoup(content.lower()) # TODO: MAKE IT OUT

        # search by title
        has_title = soup.html and soup.html.head and soup.html.head.title and soup.html.head.title.string
        if has_title and text_to_search in soup.html.head.title.string:
            match_urls.append((url["url"], url["page_rank"]))

        # search by content
        # if soup.find(text=re.compile(phrase)) != None:
        #     match_urls.append((url["url"], url["page_rank"]))

    match_urls.sort(key=lambda url: url[1])
    return [url[0] for url in match_urls]


if __name__ == "__main__":
	if len(sys.argv) != 2:
		raise ValueError('The script only allow one parameter')
	sys.exit(main(sys.argv[1]))
