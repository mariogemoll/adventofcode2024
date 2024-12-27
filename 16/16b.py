import sys
import math
import heapq

from sixteen import load_input, Direction


def dijkstra_with_paths(graph, start_node):
    distances = {}
    predecessors = {}
    pq = [(0, start_node)]
    for node in graph.keys():
        distances[node] = math.inf
        predecessors[node] = []
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
                predecessors[neighbor] = [current_node]
            elif new_total == distances[neighbor]:
                predecessors[neighbor].append(current_node)
    return distances, predecessors


def get_paths_to_start(predecessors, node):
    paths = [[node]]
    while True:
        extended_paths = []
        for path in paths:
            extended_paths += [[pred] + path.copy() for pred in predecessors[path[0]]]
        if len(extended_paths) == 0:
            return paths
        paths = extended_paths


def get_tiles_on_paths(paths):
    tiles = set()
    for path in paths:
        for i, j, dir in path:
            tiles.add((i, j))
    return tiles


def main():
    if len(sys.argv) != 2:
        print(f'Usage: python {sys.argv[0]} <input_file>')
        sys.exit(1)
    graph, start_row, start_col, end_row, end_col = load_input(sys.argv[1])

    distances, predecessors = dijkstra_with_paths(graph, (start_row, start_col, Direction.E))

    # There are four possible nodes for the end position corresponding to the four directions.
    # Find the one(s) with the lowest score
    min_distance = math.inf
    for direction in range(4):
        node = (end_row, end_col, direction)
        if node in distances:
            if distances[node] < min_distance:
                min_distance = distances[node]

    # Get all tiles on all best paths
    best_path_tiles = set()
    for direction in range(4):
        node = (end_row, end_col, direction)
        if distances[node] == min_distance:
            paths = get_paths_to_start(predecessors, node)
            best_path_tiles.update(get_tiles_on_paths(paths))

    print(len(best_path_tiles))


if __name__ == '__main__':
    main()
