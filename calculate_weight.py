import scraper, json

def print_tag_confidence(link):
    # link = "http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg"
    data = scraper.get_tag_image(link)
    data = data.decode('utf-8')
    data = json.loads(data)
    for tag in data["tags"]:
        message = "This is {} with confidence {}".format(tag["name"], tag["confidence"])
        print(message)

def print_celebrity_details(link):
    # link = "https://lh5.googleusercontent.com/-UjdvkPr9KL4/AAAAAAAAAAI/AAAAAAAAACA/WLHz8N7GHQs/photo.jpg"
    # link = "http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg"
    data = scraper.get_celebrity(link)
    data = data.decode('utf-8')
    data = json.loads(data)
    if (len(data["result"]["celebrities"]) == 0):
        print("No celebrities found")
    else:
        for person in data["result"]["celebrities"]:
            name = person["name"]
            confidence = person["confidence"]
            message = "This is {} with confidence {}".format(name, confidence)
            print(message)

def is_celebrity(link):
    data = scraper.get_celebrity(link)