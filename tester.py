import scraper
import json
import config
import requests
import requests.auth
import praw
import weight
from urllib.parse import urlparse
import time

# getTagImage(), getCelebrity(), getOCR()
def print_comments(thread):
    COMMENTS_SECTION = 1
    print("Thread:", "", thread)
    try:
        print("Before requests")
        req = requests.get(thread)
        req.text
        data_2 = req.json()
        comments = []
        print("after requests")
        for value in data_2[COMMENTS_SECTION]['data']['children']:
            if value['kind'] == "t1":
                comments.append(value['data']['body'])
        print("Filled array")
        for val in comments: # This is where it prints stuff
            print(val)
    except Exception as e:
        print(e)
        print("Error in print_comments")
        print("json from print_comments")
        print(json.dumps(data_2, indent=4))

def get_urls():
    """
    links = ["http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg", "https://blogs-images.forbes.com/brianrashid/files/2015/09/NYC-FORBES-1940x970.jpg"]
    for link in links:
        print("This is the tag image data")
        print("===========================")
        #print(scraper.getTagImage(link))
        #print(json.dumps((json.loads(scraper.getTagImage(link).decode('utf-8'))), indent = 4, sort_keys = True))
        print(scraper.format_json(scraper.get_tag_image(link)))

        print("\n\n\n\n")

        print("This is the celebrity data")
        print("===========================")
        print(scraper.format_json(scraper.get_celebrity(link)))
        print("\n\n\n\n")

        # print("This is the OCR data")
        # print("===========================")
        # print(format_json(scraper.get_ocr(link)))

            try:
        file = open("backup_links.txt", "r+")
    except IOError:
        print("File not found.")
    else:
        for subreddit in subreddits:
            print("Loading images...")
            try:
                req = requests.get(subreddit)
                req.text
                data = req.json()

                for child in data['data']['children']:
                    time.sleep(3)
                    if urlparse(child['data']['url'])[2][-4:] == ".jpg" or urlparse(child['data']['url'])[2][-4:] == ".png":
                        images.add(child['data']['url'] + "\n")
                        # print("Title: ", child['data']['title'])
                        # print("\t", "url: ", child['data']['url'])
                        url = "https://reddit.com" + child['data']['permalink'] + ".json?sort=top"
                        print_comments(url)
                        print("still in if")
            except:
                print("Something occurred. Loading backup links...")
                print("json from main:")
                print(json.dumps(data, indent = 4))
                images.clear()
                for url in file:
                    images.add(url)
                break

            else:
                pass

    for url in images:
       print(url)
       url_count = url_count + 1
    """

    url_count = 0
    subreddits = ["all", "funny", "pics"]
    images = {}

    reddit = praw.Reddit('bot1')

    for subreddit in subreddits:
        for thread in reddit.subreddit(subreddit).top(limit=50):
            if thread.url[-4:] == ".jpg" or thread.url[-4:] == ".png":
                images[thread.url] = ""
                url_count = url_count + 1
            elif urlparse(thread.url).netloc == "imgur.com":
                url = "{parsed_url.scheme}://i.{parsed_url.netloc}/{parsed_url.path}.png".format(parsed_url=urlparse(thread.url))
                images[url] = ""
                url_count = url_count + 1

    for keys in images:
        print(keys)

    #print(url_count)

    # file.close()

def main():
    get_urls()


main()