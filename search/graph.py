import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if self.graph.number_of_nodes() == 0:
                raise(ValueError('No nodes present in graph.'))
        elif start not in self.graph:
            raise(KeyError(start + ' node not present in graph.'))
        else:
            if end == None:
                Q = []
                visited = [ ]
                Q.append(start)
                visited.append(start)
                while len(Q) > 0:
                    v = Q.pop(0)
                    N = self.graph.neighbors(v)
                    for w in N:
                        if w not in visited:
                            visited.append(w)
                            Q.append(w)
                if len(visited) < self.graph.number_of_nodes():
                    raise(ValueError('Graph is unconnected, all nodes could not be reached from ' + start + '.'))
                return visited
        
            else:
                if end not in self.graph:
                    raise(KeyError(end + ' node not present in graph.'))
                Q = []
                visited = [ ]
                prev = {}
                prev[start] = None
                shortest_path = []
                Q.append(start)
                visited.append(start)
                while len(Q) > 0:
                    v = Q.pop(0)
                    N = self.graph.neighbors(v)
                    for w in N:
                        if w not in visited:
                            prev[w] = v
                            visited.append(w)
                            if w == end:
                                shortest_path.append(w)
                                while prev[w] != None:
                                    w = prev[w]
                                    shortest_path.append(w)
                                return shortest_path[::-1]
                            Q.append(w)
                return



