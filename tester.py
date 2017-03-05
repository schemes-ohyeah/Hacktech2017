import scraper
import json
import requests
import weight
from urllib.parse import urlparse
import time

# getTagImage(), getCelebrity(), getOCR()

def main():
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
    """

    count = 0
    subreddits = ["http://www.reddit.com/r/all/top.json?limit=50", "http://www.reddit.com/r/funny/top.json?limit=50",
                  "http://www.reddit.com/r/pics/top.json?limit=50"]
    images = set()

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
            except:
                print("Something occurred. Loading backup links...")
                images.clear();
                for url in file:
                    images.add(url)
                break;
            else:
                pass

    for url in images:
       print(url)
       count = count + 1

    print(count)

    # data_a = scraper.get_tag_image("https://portalstoragewuprod2.azureedge.net/vision/Analysis/1-1.jpg")
    # data_b = scraper.get_tag_image("https://portalstoragewuprod2.azureedge.net/vision/Analysis/7-1.jpg")
    # print(calculate_weight.calculateTagWeight(data_a, data_b))

    file.close()

def print_comments(thread):
    COMMENTS_SECTION = 1
    print("Thread:", "", thread)
    s = requests.get(thread)
    s.text
    data_2 = s.json()
    comments = []
    try:
        for value in data_2[COMMENTS_SECTION]['data']['children']:
            if value['kind'] == "t1":
                comments.append(value['data']['body'])

        for val in comments: # This is where it prints stuff
            print(val)
    except Exception as e:
        print("Reddit doesn't like us")

main()