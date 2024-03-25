from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *
from pyspark.sql.functions import collect_list

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_connected_components(graphframe):
    # Method to get connected components using the graphframe
    connected_components = graphframe.connectedComponents()
    # Extracting the connected components and converting them to a list of lists of ids
    components = connected_components.groupby('component').agg(collect_list('id').alias('ids')).select('ids').collect()
    return [row.ids for row in components]


if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:  # Do not modify
        for line in f:
            data = line.split()
            src = int(data[0])
            dst_list = [int(x) for x in data[1:]]
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ['id'])  # Create vertices dataframe
    edges = spark.createDataFrame(edge_list, ['src', 'dst'])  # Create edges dataframe

    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/connected-components")

    result = get_connected_components(g)
    for line in result:
        print(' '.join(map(str, line)))
