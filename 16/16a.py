import sys
import math
import heapq

from sixteen import load_input, Direction


def dijkstra(graph, start_node):
    distances = {}
    pq = [(0, start_node)]
    for node in graph.keys():
        distances[node] = math.inf
    distances[start_node] = 0
    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, distance in graph[current_node].items():
            new_total = current_distance + distance
            if new_total < distances[neighbor]:
                distances[neighbor] = new_total
                heapq.heappush(pq, (new_total, neighbor))
    return distances


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    graph, start_row, start_col, end_row, end_col = load_input(sys.argv[1])

    distances = dijkstra(graph, (start_row, start_col, Direction.E))

    # There are four possible nodes for the end position corresponding to the four directions.
    # Find the one with the lowest score
    min_distance = math.inf
    for direction in range(4):
        node = (end_row, end_col, direction)
        if node in distances:
            if distances[node] < min_distance:
                min_distance = distances[node]
    print(min_distance)


if __name__ == '__main__':
    main()
