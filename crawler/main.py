import requests
import time
from bs4 import BeautifulSoup
from . import acc_csv

def imdbScraper(titleLink, wait_time=5):
    r = requests.get('http://www.imdb.com' + titleLink + '/movieconnections')
    
    start_time = time.time()
    
    print("scraper: open new title")
    if r.status_code != 404:
        print("request: no 404")
        soup = BeautifulSoup(r.text, 'lxml')
        
        title_tag = soup.head.title.contents
        title_str = stripTitle(str(title_tag))
        
        print("scraper: next title '" + title_str + "'")
        if acc_csv.titleInList(title_str) == False:
            ref_heading = soup.find('a', attrs={'name':'referenced_in'})
            
            div_list = []
            
            if ref_heading != None:
            
                ref_divs = ref_heading.find_next_siblings('div')
                ref_divsCount = len(ref_divs)

                c = False
                cntr = 0
                
                for div in ref_divs:
                    cntr += 1
                    print("loading: {:.1%}".format(cntr/ref_divsCount), end='\r')
                    if c == False:
                        div_list.append([div.a.contents, div.a['href']])
                    if div.next_sibling.next_sibling == soup.find('a', attrs={'name':'spoofed_in'}): c = True
                
                print("scraper: writing in csv")
                acc_csv.writeCsv(title_str, div_list, titleLink)
        else:
            print("scraper: known title, just parsing div_list")
            div_list = acc_csv.getDivList(title_str)
        
        elapsed_time = time.time() - start_time
        if elapsed_time < wait_time:
            sleep_time = wait_time - elapsed_time
            print("request: need to wait {:.0} seconds".format(sleep_time))
            time.sleep(sleep_time)
        
        return div_list
    else:
        print('request: 404')
        return '404'
    
def stripTitle(title):
    titleQuotPos = title.index("'") if "'" in title else None
    titleHypPos = title.index('-') if '-' in title else None
    if titleQuotPos == None and titleHypPos == None:
        return title
    elif titleQuotPos == None:
        return title[: titleHypPos - 1]
    else:
        return title[titleQuotPos + 1 : titleHypPos - 1]
    
def imdbCrawler(levelDepth=0, init_titleLink='/title/tt0133093', wait_time=5):
    if levelDepth == None: levelDepth = 0
    if init_titleLink == None: init_titleLink = '/title/tt0133093'
    if wait_time == None: wait_time = 5
    #print("level of Depth: " + str(levelDepth) + " initial title Link: " + str(init_titleLink) + " wait time: " + str(wait_time))
    print("crawler: start, level: " + str(levelDepth))
    div_list = imdbScraper(init_titleLink, wait_time)
    for _ in range(levelDepth):
        if div_list != '404':
            for div in div_list:
                next_link = div[1]
                imdbCrawler(levelDepth-1, next_link, wait_time)
    print("crawler: done, level: " + str(levelDepth))