from pyspark import SparkContext
from numpy import array
from pyspark.mllib.clustering import KMeans, KMeansModel

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()


def get_clusters(data_rdd, sample_ids, num_clusters=NUM_CLUSTERS, max_iterations=MAX_ITERATIONS,
                 initialization_mode=INITIALIZATION_MODE, seed=SEED):
    # Train a K-Means model
    model = KMeans.train(data_rdd, num_clusters, maxIterations=max_iterations,
                         initializationMode=initialization_mode, seed=seed)

    # Predict cluster for each data point
    predictions = model.predict(data_rdd).collect()

    # Group sample_ids based on the predicted clusters
    clusters = [[] for _ in range(num_clusters)]
    for i, prediction in enumerate(predictions):
        clusters[prediction].append(sample_ids[i])

    return clusters


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    # Parse data from file into an RDD
    data_rdd = f.map(lambda line: array([float(x) for x in line.split(',')[1:]]))

    # Get sample_ids from file
    sample_ids = f.map(lambda line: line.split(',')[0]).collect()

    clusters = get_clusters(data_rdd, sample_ids)

    for cluster in clusters:
        print(','.join(cluster))
