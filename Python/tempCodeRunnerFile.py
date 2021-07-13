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
    # For keeping track of what we have visited
    visited = {}
    # keep track of distance
    distance = {}
    # parent node of specific graph
    parent = {}

    bfs_traversal_output = []
    queue = Queue()

    # travelling the cities in map
    for city in graph.keys():
        # since intially no city is visited so there will be nothing in visited list
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    # starting from 'Arad'
    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()     # first element of the queue, here it will be 'arad'
        bfs_traversal_output.append(u)

        # explore the adjust cities adj to 'arad'
        for v in romaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + 1
                queue.put(v)

        # reaching our destination city i.e 'bucharest'
    g = destinationNode
    path = []
    while g is not None:
        path.append(g)
        g = parent[g]

    path.reverse()
    # printing the path to our destination city
    print(path)


# Starting City & Destination City
bfs('Arad', 'Bucharest')