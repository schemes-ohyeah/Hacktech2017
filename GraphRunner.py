from Vertex import Graph
import scraper, weight

def main():
    # Fill this from Spring / Michael code - getting from Reddit
    # { "url" : [comments] }
    content = {}
    # To be filled with data from MS Vision API
    dataList = []
    # Add MS Vision data to dataList
    for url in content.keys():
        dataList.append({
            "url" : url,
            "comments" : content[url],
            "tag" : scraper.get_tag_image(url),
            "celeb" : scraper.get_celebrity(url)
        })
    # Instantiate image graph
    imageGraph = Graph()
    # Add necessary data points from dataList to the imageGraph
    for data in dataList:
        imageGraph.add_vertex({
            "url" : data["url"],
            "tag" : data["tag"],
            "celeb" : data["celeb"]
        })
    # Create edges between EVERYTHING
    for vertex in imageGraph:
        for othertex in imageGraph:
            # If there is not already an edge, add it
            if othertex not in vertex:
                cost = weight.calculate_total_image_weight(
                    vertex.data["tag"], othertex.data["tag"],
                    vertex.data["celeb"], othertex.data["celeb"]
                )
                imageGraph.add_edge(vertex, othertex, cost)

    # Create a wordGraph
    wordGraph = Graph()
    # Add comments from dataList to this graph
    for data in dataList:
        wordGraph.add_vertex({
            data["url"],
            data["comments"]
        })
    # Create edges between EVERYTHING
    for vertex in wordGraph:
        for othertex in wordGraph:
            # If there is not already an edge, add it
            if othertex not in vertex:
                cost = weight.calculate_word_weight(vertex.data, othertex.data)
                wordGraph.add_edge(vertex, othertex, cost)

    print("Weights for imageGraph")
    printWeights(imageGraph)
    print("\n\n===================\n\n")
    printWeights(wordGraph)

def printWeights(graph):
    for vertex in graph:
        neighbors = vertex.get_connections()
        for neighbor in neighbors:
            print(vertex["url"] + " to " + neighbor["url"] + " weight is " + vertex.get_weight(neighbor))

main()