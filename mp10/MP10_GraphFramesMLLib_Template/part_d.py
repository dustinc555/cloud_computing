from pyspark.mllib.tree import RandomForest
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext

sc = SparkContext()


def predict(training_data, test_data):
    # Train random forest classifier from given data
    model = RandomForest.trainClassifier(training_data, numClasses=2,
                                         categoricalFeaturesInfo={},
                                         numTrees=20, featureSubsetStrategy="auto",
                                         impurity='gini', maxDepth=4, maxBins=32)
    # Predict using the trained model
    predictions = model.predict(test_data.map(lambda x: x.features))
    return predictions


if __name__ == "__main__":
    raw_training_data = sc.textFile("dataset/training.data")
    raw_test_features_data = sc.textFile("dataset/test-features.data")
    raw_test_labels_data = sc.textFile("dataset/test-labels.data")

    # Parse RDD from raw training data
    training_data = raw_training_data.map(lambda line: line.split(',')).map(
        lambda features: LabeledPoint(float(features[-1]), features[:-1]))

    # Parse RDD from raw test data
    test_data = raw_test_features_data.map(lambda line: line.split(',')).map(
        lambda features: LabeledPoint(-1, features))  # Labels are not available for test data

    predictions = predict(training_data, test_data)

    # Output the predictions
    for pred in predictions.collect():
        print(int(pred))
