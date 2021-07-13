from queue import Queue

graph = {​​

    "Arad": {​​"Timisoara": 118, "Sibiu": 140,"Zerind": 75}​​,

    "Zerind": {​​"Arad": 75, "Oradea": 71}​​,

    "Oradea": {​​"Zerind": 71, "Sibiu": 151}​​,

    "Timisoara": {​​"Arad": 118, "Lugoj": 111}​​,

    "Lugoj": {​​"Timisoara": 111, "Mehadia":70}​​,

    "Mehadia": {​​"Lugoj": 70, "Dobreta": 75}​​,

    "Dobreta": {​​"Mehadia":75, "Craiova":120}​​,

    "Craiova": {​​"Dobreta": 120, "RimnicuVilcea": 146, "Pitesi": 138}​​,

    "RimnicuVilcea": {​​"Craiova": 146, "Pitesi": 97, "Sibiu":80}​​,

    "Sibiu": {​​"Arad": 140, "Oradea":151, "RimnicuVilcea": 80, "Fagaras": 99}​​,

    "Fagaras": {​​"Sibiu": 99, "Bucharest":211}​​,

    "Pitesi": {​​"Bucharest": 101, "RimnicuVilcea": 97, "Craiova": 138}​​,

    "Bucharest": {​​"Pitesi": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85}​​,

    "Giurgiu": {​​"Bucharest": 90}​​,

    "Urziceni": {​​"Bucharest": 85, "Hirsova": 98, "Vaslui": 142}​​,

    "Hirsova": {​​"Urziceni": 98, "Eforie": 86}​​,

    "Eforie": {​​"Hirsova": 86}​​,

    "Vaslui": {​​"Urziceni": 142, "Iasi": 92}​​,

    "Iasi": {​​"Vaslui": 92, "Neamt": 87}​​,

    "Neamt": {​​"Iasi": 87}​​

}​​​

def bfs(startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}

    bfs_traversal_output = []
    queue = Queue()

    for city in graph.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Arad'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)

    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    print(path)


# Starting City & Destination City
bfs('Arad', 'Bucharest')