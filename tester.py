import scraper
import json
import requests
from urllib import urlparse

# getTagImage(), getCelebrity(), getOCR()

def main():
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

    r = requests.get("http://www.reddit.com/.json")
    r.text
    data = r.json()

    for value in data['data']['children']:
        print("Title: ", value['data']['title'])
        #if urlparse(value['data']['url'])[5]
        print("\t", "url: ", value['data']['url'])

main()