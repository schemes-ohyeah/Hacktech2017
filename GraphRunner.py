from Vertex import Graph
import scraper, weight, tester


def get_graphs():
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


    return imageGraph, wordGraph

    # print("Weights for imageGraph")
    # printWeights(imageGraph)
    # print("\n\n===================\n\n")
    # print("Weights for wordGraph")
    # printWeights(wordGraph)


def printWeights(graph):
    for vertex in graph:
        vert = graph.get_vertex(vertex)
        neighbors = vert.get_connections()
        for neighbor in neighbors:
            print("{} -> {}, weight {}".format(vert.get_data(), neighbor.get_data(), vert.get_weight(neighbor)))
            #print(graph.get_vertex(vertex).get_data() + " to " + neighbor.get_data() + " weight is " + graph.get_vertex(vertex).get_weight(neighbor))

def get_weights(graph):
    graph_data = {}
    for vertex in graph:
        vert = graph.get_vertex(vertex)
        neighbors = vert.get_connections()

        neighbor_list = []
        for neighbor in neighbors:
            neighbor_list.append("{} -> {}, weight {}".format(vert.get_data(), neighbor.get_data(), vert.get_weight(neighbor)))
        graph_data[vert] = neighbor_list

    return graph_data

