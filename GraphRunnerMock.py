from Vertex import Graph
import weight

MOCK_COMMENT_DATA = {
    "a": ["hello world", "this is a test", "banana apple orange"],
    "b": ["hello apple", "this is a mess", "bonono opplo arange"],
    "c": ["ello surface", "that was a triumpth", "hello world", "huge success"]
}

MOCK_SCRAPER_TAG_DATA = {
    "a": [{"name": "sky", "confidence": 0.9}, {"name": "apple", "confidence": 0.5}],
    "b": [{"name": "WHAT", "confidence": 0.0001}, {"name": "hello", "confidence": 0.75}, {"name": "sky", "confidence": 0.45}],
    "c": [{"name": "nothing", "confidence": 1}, {"name": "sunrise", "confidence": 0.01}]
}

MOCK_SCRAPER_CELEB_DATA = {
    "a": [],#{"name":"Barack Hussein Obama","faceRectangle":{"left":1277,"top":552,"width":1305,"height":1305},"confidence":0.9949071}],
    "b": [],
    "c": []
}

class MockTester:
    def __init__(self):
        pass

    def get_urls(self):
        return MOCK_COMMENT_DATA

class MockScraper:
    def __init__(self):
        pass

    def get_tag_image(self, url):
        return {"requestId": "no", "metadata": {}, "tags": MOCK_SCRAPER_TAG_DATA[url]}

    def get_celebrity(self, url):
        return {"requestId": "no", "metadata": {}, "result": {"celebrities": MOCK_SCRAPER_CELEB_DATA[url]}}

tester = MockTester()
scraper = MockScraper()

def main():
    # Fill this from Spring / Michael code - getting from Reddit
    # { "url" : [comments] }
    content = tester.get_urls()
    # To be filled with data from MS Vision API
    dataList = []
    metadata = {}
    imageGraph = Graph()
    # Add MS Vision data to dataList
    for url in content.keys():
        metadata[url] = {
            "comments": content[url],
            "tag": scraper.get_tag_image(url),
            "celeb": scraper.get_celebrity(url)
        }
        imageGraph.add_vertex(url)
    # Instantiate image graph

    # Add necessary data points from dataList to the imageGraph
    # Create edges between EVERYTHING
    for vertex in imageGraph:
        for othertex in imageGraph:
            # print(imageGraph.get_vertices())
            # If there is not already an edge, add it
            if not imageGraph.has_edge(vertex, othertex):
                vert_data = metadata[vertex]
                othertex_data = metadata[othertex]
                cost = weight.calculate_total_image_weight(
                    vert_data, othertex_data,
                    vert_data, othertex_data
                    # vert_data["tag"], othertex_data["tag"],
                    # vert_data["celeb"], othertex_data["celeb"]
                )
                # if cost > 0:
                imageGraph.add_edge(vertex, othertex, cost)

    # Create a wordGraph
    wordGraph = Graph()
    # Add comments from dataList to this graph
    for url in metadata.keys():
        wordGraph.add_vertex(url)
    # Create edges between EVERYTHING
    for vertex in wordGraph:
        for othertex in wordGraph:
            # If there is not already an edge, add it
            if not wordGraph.has_edge(vertex, othertex):
                vert_data = metadata[vertex]
                othertex_data = metadata[othertex]
                cost = weight.calculate_word_weight(
                    # vert_data, othertex_data
                    vert_data["comments"], othertex_data["comments"]
                )
                # if cost > 0:
                wordGraph.add_edge(vertex, othertex, cost)

    print("Weights for imageGraph")
    printWeights(imageGraph)
    print("\n\n===================\n\n")
    print("Weights for wordGraph")
    printWeights(wordGraph)


def printWeights(graph):
    for vertex in graph:
        vert = graph.get_vertex(vertex)
        neighbors = vert.get_connections()
        for neighbor in neighbors:
            print("{} -> {}, weight {}".format(vert.get_data(), neighbor.get_data(), vert.get_weight(neighbor)))
            #print(graph.get_vertex(vertex).get_data() + " to " + neighbor.get_data() + " weight is " + graph.get_vertex(vertex).get_weight(neighbor))

main()
