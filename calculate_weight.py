import scraper, math, Vertex

def print_tag_confidence(link):
    # link = "http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg"
    data = scraper.get_tag_image(link)
    for tag in data["tags"]:
        message = "This is {} with confidence {}".format(tag["name"], tag["confidence"])
        print(message)

def print_celebrity_details(link):
    # link = "https://lh5.googleusercontent.com/-UjdvkPr9KL4/AAAAAAAAAAI/AAAAAAAAACA/WLHz8N7GHQs/photo.jpg"
    # link = "http://img.wennermedia.com/social/trumpfamily-0a0680e3-ea21-45c5-a9ad-c51fec63dffa.jpg"
    data = scraper.get_celebrity(link)
    if not is_celebrity(link):
        print("No celebrities found")
    else:
        for person in data["result"]["celebrities"]:
            name = person["name"]
            confidence = person["confidence"]
            message = "This is {} with confidence {}".format(name, confidence)
            print(message)

def is_celebrity(link):
    data = scraper.get_celebrity(link)
    return len(data["result"]["celebrities"]) != 0

def calculateWeight(dataA, dataB):
    """

    :param dataA: Raw json data for one image
    :param dataB: Raw json data for another image
    :return: returns a float weight between 0 and 1
    """
    # Get the tags for both vertexes
    # dataA = VertexA.get_data()["tags"]
    # dataB = VertexB.get_data()["tags"]
    # We will work with the larger one compared to the smaller one to make sure we hit
    # each item
    if len(dataA) > len(dataB):
        dataLarger = dataA
        dataSmaller = dataB
    else:
        dataLarger = dataB
        dataSmaller = dataA
    subweights = []
    for name in dataLarger["name"]:
        if name in dataSmaller["name"]:
            difference = math.fabs(dataLarger["confidence"] - dataSmaller["confidence"])
            subweights.append(1 - difference)
        else:
            subweights.append(0)
    total_tag_weight = sum(subweights) / float(len(subweights))
    return total_tag_weight
