import scraper
import json

# getTagImage(), getCelebrity(), getOCR()

def format_json(js):
    return json.dumps((json.loads(js.decode('utf-8'))), indent = 4, sort_keys = True)

def main():
    links = ["http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg", "https://blogs-images.forbes.com/brianrashid/files/2015/09/NYC-FORBES-1940x970.jpg"]
    for link in links:
        print("This is the tag image data")
        print("===========================")
        #print(scraper.getTagImage(link))
        #print(json.dumps((json.loads(scraper.getTagImage(link).decode('utf-8'))), indent = 4, sort_keys = True))
        print(format_json(scraper.getTagImage(link)))

        print("\n\n\n\n")

        print("This is the celebrity data")
        print("===========================")
        print(format_json(scraper.getCelebrity(link)))
        print("\n\n\n\n")

        print("This is the OCR data")
        print("===========================")
        print(format_json(scraper.getOCR(link)))

main()