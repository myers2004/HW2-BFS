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
        #Raise an error if there are no nodes in the graph
        if self.graph.number_of_nodes() == 0:
                raise(ValueError('No nodes present in graph.'))
        #Raise an error if the given start node does not exist
        elif start not in self.graph:
            raise(KeyError(start + ' node not present in graph.'))
        else:
            #If no end node is given, do a bfs traversal to visit each node, 
            #going one layer at a time, and return a lsit of each node visited, 
            #in the order they were visited.
            if end == None:
                Q = []                   #The queue that will tell which node to visit next
                visited = [ ]            #A list to be filled with nodes that have been visited
                Q.append(start)          #Add the start node to the queue
                visited.append(start)    #Add the start node the visited list

                #The bfs traversal gets the next node in line out of the queue, adds its
                #neighbors to the queue, and then adds it to the visited list, until there
                #are no more nodes present in the queue
                while len(Q) > 0:
                    v = Q.pop(0)                #Get the next node in the queue
                    N = self.graph.neighbors(v) #Get a list of that nodes neighbors

                    #For each neighbor, if it was not visited yet add it to both the visited and queue list
                    for w in N:
                        if w not in visited:
                            visited.append(w)
                            Q.append(w)
                #Raise an error if not every node was visited
                if len(visited) < self.graph.number_of_nodes():
                    raise(ValueError('Graph is unconnected, all nodes could not be reached from ' + start + '.'))
                return visited
        
            else:
                #If an end node was given, do a bredth first search to find the shortest path from the 
                #start to the end node

                #Raise an error if the given end node doesn't exist
                if end not in self.graph:
                    raise(KeyError(end + ' node not present in graph.'))
                Q = []                  #The queue that will tell which node to visit next
                visited = [ ]           #A list to be filled with nodes that have been visited
                prev = {}               #For each node, stores the node that lead to it being added to the queue
                prev[start] = None      #The start node has no previous node
                shortest_path = []      #Stores the shortest path from start to end
                Q.append(start)         #Add the start node to the path
                visited.append(start)   #Add the start node to the visited list
                
                #The bfs gets the next node in line out of the queue, adds its
                #neighbors to the queue, and then adds it to the visited list, until there
                #are no more nodes present in the queue. After the end node is found,
                #the search is ended and the shortest path is traced back from the end node
                #through the prev dictionary
                while len(Q) > 0:
                    v = Q.pop(0)                    #Get the next node in the queue
                    N = self.graph.neighbors(v)     #Get a list of that nodes neighbors

                    #For each neighbor, if it was not visited yet add it to both the visited and queue list
                    for w in N:
                        if w not in visited:
                            prev[w] = v
                            visited.append(w)

                            #If a neighbor is the end node, stop the search and trace back the path
                            if w == end:
                                shortest_path.append(w)
                                while prev[w] != None:
                                    w = prev[w]
                                    shortest_path.append(w)

                                #return the shortest path, reversing to start at the start node
                                return shortest_path[::-1]
                            Q.append(w)
                #If no shortest path is found, return None
                return



