import json
import boto3
import base64

from collections import deque

dynamodb = boto3.resource("dynamodb")
table_name = "mp2_table"
table = dynamodb.Table(table_name)


def delete_all_items():
    # Scan and delete all items in the DynamoDB table
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan["Items"]:
            batch.delete_item(
                Key={"source": each["source"], "destination": each["destination"]}
            )


def store_distances_in_dynamodb(distances):
    # Store distances in DynamoDB table
    with table.batch_writer() as batch:
        for source, destinations in distances.items():
            for destination, distance in destinations.items():
                batch.put_item(
                    Item={
                        "source": source,
                        "destination": destination,
                        "distance": distance,
                    }
                )


def parse_graph(graph):
    # Parse the input graph and create an adjacency list
    adjacency_list = {}
    edges = graph.split(",")

    for edge in edges:
        source, destination = edge.split("->")
        if source not in adjacency_list:
            adjacency_list[source] = []
        if destination not in adjacency_list:
            adjacency_list[destination] = []
        adjacency_list[source].append(
            (destination, 1)
        )  # Assuming unit weight for simplicity

    return adjacency_list


def compute_shortest_distances(graph):
    # Parse the graph to create an adjacency list
    adjacency_list = parse_graph(graph)

    # Dictionary to store distances
    distances = {}

    # Iterate over each vertex
    for source in adjacency_list:
        distances[source] = {}
        visited = set()
        queue = deque([(source, 0)])  # (vertex, distance)

        while queue:
            current_vertex, current_distance = queue.popleft()

            # Skip if already visited
            if current_vertex in visited:
                continue

            # Mark current vertex as visited
            visited.add(current_vertex)

            # Update distance for the current vertex
            distances[source][current_vertex] = current_distance

            # Enqueue neighbors with increased distance
            for neighbor, edge_weight in adjacency_list[current_vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, current_distance + edge_weight))

    return distances


def lambda_handler(event, context):
    print("running with event")
    print(event)  # ease of seeing

    # Check if 'graph' is present in the request body
    if "body" in event and "graph" in json.loads(
        base64.b64decode(event["body"]).decode("utf-8")
    ):
        body = base64.b64decode(event["body"]).decode("utf-8")

        print("decoded body as")
        print(body)

        graph = json.loads(body)["graph"]

        # Delete all items in the DynamoDB table
        delete_all_items()

        # Parse the graph and compute shortest distances using BFS
        distances = compute_shortest_distances(graph)

        # Store distances in DynamoDB
        store_distances_in_dynamodb(distances)

        return {
            "statusCode": 200,
            "body": json.dumps("Graph processed and distances stored successfully."),
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps(
                "Bad Request: Missing or incorrect graph in the request body."
            ),
        }
