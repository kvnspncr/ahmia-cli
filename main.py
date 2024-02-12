import requests
from bs4 import BeautifulSoup
import time
import os
from art import * 
import argparse 
def main(query: str):
    parser = argparse.ArgumentParser() 
    parser.add_argument('-limit', type=int, help=None)
    args = parser.parse_args() 
    limit = args.limit
    url = f"https://ahmia.fi/search/?q={query}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    urls = soup.find_all("cite")
    titles = soup.find_all("p")
    noshow = ["Did you mean", "Unfortunately", "Omitted"]
    if res.status_code == 200:
        index = 0
        if limit is not None: 
            print(f"Limiting to {limit} results")
        for title, url in zip(titles, urls):
            if not any(entry in title.text for entry in noshow):
                print(f"\nTitle: {title.text}\nUrl: {url.text}\n")
                index += 1
                if index == limit: 
                    break
                elif limit is None:
                    continue 
    else:
        print(f"Exception: {res.status_code}")

if __name__ == "__main__":
    try:
        os.system("clear")
        tprint("ahmia.fi")
        query = input("Enter query: ")
        if query:
            main(query)
        else:
            print("Exception: invalid query")
    except KeyboardInterrupt:
        print("\n")
        exit(0)

