#!/usr/bin/env/python3
"""Scrapes an arbitrary Wikipedia page, recursively follows first link.

Ceases execution upon reaching the "Philosophy" entry."""
import argparse

import requests
from bs4 import BeautifulSoup


def find_links(page_soup):
    """Locates anchor tags that are direct descendants of p tags."""
    return page_soup.select(".mw-parser-output > p > a")


def find_first_link(a_list):
    """Find first link to a Wiki page."""
    return [link['href'] for link in a_list
            if 'href' in link.attrs and link['href'].startswith('/')][0]


def is_philosophy(page_soup):
    """Checks for base case (the Philosophy wikipedia entry)."""
    return page_soup.title.string == 'Philosophy - Wikipedia'


def build_url(wiki_link):
    """Build URL given an internal Wikipedia link."""
    return 'https://en.wikipedia.org' + wiki_link


def philospider(url, title_list=None, url_list=None, steps=0):
    """Scan a URL for relevant data."""
    if title_list is None:
        title_list = []

    if url_list is None:
        url_list = []

    if url in url_list:
        return (url,
                title_list,
                url_list,
                steps)

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        return (url,
                title_list,
                url_list,
                steps)
    
    if is_philosophy(soup):
        # Base case
        return (url,
                title_list + [soup.title.string],
                url_list + [url],
                steps)
    else:
        first_link = find_first_link(find_links(soup))
        return philospider(build_url(first_link),
                           title_list + [soup.title.string],
                           url_list + [url],
                           steps + 1)


def main(argv=None):
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u',
                       '--url',
                       type=str,
                       nargs=1,
                       help="Wikipedia page to begin the process",
                       required=False)
    group.add_argument('-n',
                       '--num_queries',
                       type=int,
                       nargs=1,
                       help="Number of random pages to process",
                       required=False)

    args = parser.parse_args()

    if args.num_queries:
        successes = []
        steps = []

        for i in range(args.num_queries[0]):
            (last_url,
             titles,
             urls,
             num_steps) = philospider('https://en.wikipedia.org/'
                                      'wiki/Special:Randompage')

            if titles[-1] == 'Philosophy - Wikipedia':
                successes = successes + [True]
            else:
                successes = successes + [False]

            steps = steps + [num_steps]

        print(successes)
        print(steps)
        return (successes, steps)

    elif args.url:
        successful = False

        last_url, titles, urls, num_steps = philospider(args.url[0])

        if titles[-1] == 'Philosophy - Wikipedia':
            successful = True

        print("\nThe process took",
              str(num_steps),
              "steps to terminate.\n\n")

        titles_urls = zip(titles, urls)

        for title, url in titles_urls:
            print(title.split('-')[0].strip() + " (" + url + ")")

    else:
        print("url: " + str(args.url))
        successful = False

        (last_url,
         titles,
         urls,
         num_steps) = philospider('https://en.wikipedia.org/'
                                  'wiki/Special:Randompage')

        if titles[-1] == 'Philosophy - Wikipedia':
            successful = True

        print("\nThe process took",
              str(num_steps),
              "steps to terminate.\n\n")

        titles_urls = zip(titles, urls)

        for title, url in titles_urls:
            print(title.split('-')[0].strip() + " (" + url + ")")


if __name__ == '__main__':
    main()

