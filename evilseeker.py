#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: ss4tan
"""

# Import all libraries
from googlesearch import search
import time
from colorama import Fore
import argparse 


# Make parameters
parser = argparse.ArgumentParser(description="Search URLs with google dorking in a faster and specific way")
parser.add_argument("-d","--dork", help="The google dork.              Example: inurl:\"index.php\"", type=str)
parser.add_argument("-n", "--numberesult", help="Number of results.        Example: 5", type=int)
parser.add_argument("-l", "--language",help="Language of pages.        Example: 'en'", default="en", type=str)
parser.add_argument("-r", "--region", help="Region of pages.     Example: us (Check: https://developers.google.com/custom-search/docs/json_api_reference#countryCodes),", default="us" )
parser.add_argument("-s", "--sleep", help="Time interval in seconds.   Example: 10", default=0,  type=float)
parser.add_argument("-p", "--proxy", help='Proxy to use.               Example: "127.0.0.1:9050"', default=None,type=str)


args = parser.parse_args()


# function to show logo
def logo():
    
    # logo
    banner = """


d88888b db    db d888888b db      .d8888. d88888b d88888b db   dD d88888b d8888b. 
88'     88    88   `88'   88      88'  YP 88'     88'     88 ,8P' 88'     88  `8D 
88ooooo Y8    8P    88    88      `8bo.   88ooooo 88ooooo 88,8P   88ooooo 88oobY' 
88~~~~~ `8b  d8'    88    88        `Y8b. 88~~~~~ 88~~~~~ 88`8b   88~~~~~ 88`8b   
88.      `8bd8'    .88.   88booo. db   8D 88.     88.     88 `88. 88.     88 `88. 
Y88888P    YP    Y888888P Y88888P `8888Y' Y88888P Y88888P YP   YD Y88888P 88   YD 
                                                                                  
                                                                                  
    """
    
    # author
    who = "By: ss4tan"
    print(Fore.MAGENTA)
   
    # show proxy 
    if args.proxy:
        is_proxy = "f{args.proxy}"

    # show animation of logo
    for i in range(len(banner)):

        print(banner[i], end="")
        time.sleep(0.000001)

    # change colour to CYAN
    print(Fore.CYAN)

    # show proxy
    print(f" Proxy: {args.proxy}                                                                                      ", end="")


    # animation of author
    for i in range(len(who)):
        time.sleep(0.01)
        print(who[i], end='')
    
    # reset colours
    print(Fore.RESET)
    print("\n\n\n")


# Function to search without proxy
def searching_no_proxy(query, num, language, my_region, sleep):
    
    # search urls without proxy
    urls = list(search(query, num, lang=language, region=my_region, sleep_interval=sleep))
    
    # animation of urls
    for i in range(len(urls)):
        print(f"{Fore.YELLOW}[{Fore.GREEN}!{Fore.YELLOW}]{Fore.CYAN}\t{urls[i]}{Fore.RESET}\n")
        time.sleep(0.000001)


# function to search with proxy
def searching_proxy(query, num, language, my_region, sleep, my_proxy):
    
    # search urls with proxy
    urls = list(search(query, num, proxy=my_proxy, lang=language, region=my_region, sleep_interval=sleep))
    
    # animation of urls
    for i in range(len(urls)):
        print(f"{Fore.YELLOW}[{Fore.GREEN}!{Fore.YELLOW}]{Fore.CYAN}\t{urls[i]}{Fore.RESET}\n")
        time.sleep(0.000001)




if __name__ == "__main__":
    
    # hide barline
    print("\033[?25l", end="")
    
    # show logo
    logo()
    
    # validation of proxy
    if args.proxy == None:
        # search without proxy
        searching_no_proxy(query=args.dork, num=args.numberesult, language=args.language, sleep=args.sleep, my_region=args.region);
    else:
        # search with proxy
        searching_proxy(query=args.dork, num=args.numberesult, language=args.language, sleep=args.sleep, my_proxy=args.proxy, my_region=args.region);

    # spawn barline
    print("\033[?25h", end="")
