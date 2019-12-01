'''
LinkCollector will take in a url and will return a list of links within that URL.
    It will recursively look through any local links.
'''

from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.error import HTTPError
import re
import sys
from queue import Queue
LINK_REGEX = re.compile("<a [^>]*href=['\"]([^'\"]+)['\"][^>]*>")


class LinkCollector:
    def __init__(self, url, _max_links:int = 10):
        self.url = "http://%s" % urlparse(url).netloc
        self.collected_links = {}
        self.bad_links = set()
        self.visited_links = set()
        self.numLinks = 0
        if 1 <= int(_max_links) <= 25:
            self.maxLinks = int(_max_links)
        else:
            self.maxLinks = 10

    def collect_links(self):
        queue = Queue()
        queue.put(self.url)
        while not queue.empty():
            url = queue.get().rstrip('/')
            if url not in self.visited_links:
                self.visited_links.add(url)
                try:
                    ##print('opening link %s' % url)
                    self.numLinks += 1
                    if self.numLinks <= self.maxLinks:
                        page = str(urlopen(url).read())
                    else:
                        break
                except HTTPError:
                    self.bad_links.add(url)
                    ##print("Caught an exception. with %s" % url)
                links = LINK_REGEX.findall(page)
                links = {
                    self.normalize_url(urlparse(url).path, link)
                    for link in links
                }
                self.collected_links[url] = links
                for link in links:
                    self.collected_links.setdefault(link, set())
                unvisited_links = links.difference(self.visited_links)
                for link in unvisited_links:
                    if link.startswith(self.url):
                        queue.put(link)
            ##else:
                ##print("skipping link %s because we have seen this link before" % url)

    def normalize_url(self, path, link):
        if link.startswith("http://") or link.startswith("https://"):
            return link.rstrip('/')
        elif link.startswith("/"):
            return self.url + link.rstrip('/')
        else:
            return self.url + path.rpartition('/')[0] + '/' + link.rstrip('/')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        collector = LinkCollector(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 1:
        collector = LinkCollector(sys.argv[1])
    else:
        print("Usage: %s url max_links_to_scan" % sys.argv[0])

    print('Collecting links for %s' % collector.url)
    total_link = 0
    total_bad_link = 0
    collector.collect_links()
    for link, item in collector.collected_links.items():
        total_link += 1
        if item == set():
            print("For the link %s , There are the no links found:" % link)
        else:
            print("For the link %s , here are the links we found:" % link)
            for innerLink in item:
                total_link += 1
                print("..........%s" % innerLink)
    for link in collector.bad_links:
        total_bad_link += 1
        print("This link seems bad .. %s" % link)
    print("Total good links found for %s is %s " % (sys.argv[1], total_link) )
    print("Total bad links found for %s is %s " % (sys.argv[1], total_bad_link) )
    print("Total links scanned: %s" % collector.numLinks)
    print("Max links to scan: %s" % collector.maxLinks)