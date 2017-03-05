from Vertex import Graph
import scraper, weight

def main():
    # Fill this from Springs code - getting from Reddit
    imageURLs = []
    # To be filled with data from MS Vision API
    dataList = []
    # Add MS Vision data to dataList
    for url in imageURLs:
        dataList.append({
            "url" : url,
            "tag" : scraper.get_tag_image(url),
            "celeb" : scraper.get_celebrity(url)
        })
    # Instantiate graph
    imageGraph = Graph()
    # Add all data points from dataList to the imageGraph
    for data in dataList:
        imageGraph.add_vertex(data)
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

main()