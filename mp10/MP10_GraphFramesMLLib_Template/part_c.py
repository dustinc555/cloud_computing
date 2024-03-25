from pyspark import SparkContext
from pyspark.sql import SparkSession
from graphframes import *

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    # Find shortest distances in the given graphframe to the vertex with id `dst_id`
    shortest_paths = graphframe.shortestPaths(landmarks=[dst_id])
    shortest_distances = {}

    for row in shortest_paths.select("id", "distances").collect():
        vertex_id = row["id"]
        distances = row["distances"]
        shortest_distance = distances.get(dst_id, -1)  # Use -1 if no path exists
        shortest_distances[vertex_id] = shortest_distance

    return shortest_distances


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            parts = line.strip().split(' ')
            src = int(parts[0])
            dst_list = [int(x) for x in parts[1:]]
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ["id"])
    edges = spark.createDataFrame(edge_list, ["src", "dst"])

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")

    # Find vertex id of the destination vertex (with id '1')
    dst_vertex_id = g.vertices.filter(g.vertices.id == '1').select('id').collect()[0][0]

    # We want the shortest distance from every vertex to the destination vertex
    shortest_distances = get_shortest_distances(g, dst_vertex_id)
    for k, v in shortest_distances.items():
        print(k, v)
