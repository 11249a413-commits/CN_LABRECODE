"""
Experiment 8: Distance Vector (Bellman-Ford) and Link State (Dijkstra) routing.
Edit GRAPH below to experiment with other network topologies.
"""
import math

GRAPH = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "C": 1, "D": 4},
    "C": {"A": 5, "B": 1, "D": 2, "E": 3},
    "D": {"B": 4, "C": 2, "E": 1},
    "E": {"C": 3, "D": 1},
}

def distance_vector(graph):
    nodes = list(graph)
    dist = {u: {v: (0 if u == v else graph[u].get(v, math.inf)) for v in nodes} for u in nodes}
    next_hop = {u: {v: (v if v in graph[u] else None) for v in nodes} for u in nodes}
    changed = True
    rounds = 0
    while changed:
        changed = False
        rounds += 1
        for u in nodes:
            for neighbor, cost in graph[u].items():
                for destination in nodes:
                    candidate = cost + dist[neighbor][destination]
                    if candidate < dist[u][destination]:
                        dist[u][destination] = candidate
                        next_hop[u][destination] = neighbor
                        changed = True
        if rounds > len(nodes) * len(nodes):
            break
    return dist, next_hop, rounds

def dijkstra(graph, source):
    dist = {v: math.inf for v in graph}
    previous = {v: None for v in graph}
    dist[source] = 0
    unseen = set(graph)
    while unseen:
        u = min(unseen, key=lambda x: dist[x])
        unseen.remove(u)
        if dist[u] == math.inf:
            break
        for v, weight in graph[u].items():
            candidate = dist[u] + weight
            if candidate < dist[v]:
                dist[v], previous[v] = candidate, u
    return dist, previous

def path_from_previous(previous, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous[target]
    return " -> ".join(reversed(path))

def main():
    print("Network links (undirected costs):")
    for u, links in GRAPH.items():
        print(f"  {u}: {links}")
    dv, hops, rounds = distance_vector(GRAPH)
    print(f"\nDISTANCE VECTOR converged after {rounds} update round(s):")
    for src in GRAPH:
        print(f"From {src}:")
        for dst in GRAPH:
            print(f"  to {dst}: cost={dv[src][dst]}, next hop={hops[src][dst]}")
    print("\nLINK STATE (Dijkstra):")
    for src in GRAPH:
        dist, prev = dijkstra(GRAPH, src)
        print(f"From {src}:")
        for dst in GRAPH:
            print(f"  to {dst}: cost={dist[dst]}, path={path_from_previous(prev, dst)}")

if __name__ == "__main__":
    main()
