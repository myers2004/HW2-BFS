# write tests for bfs
import pytest
from search import Graph
import networkx as nx

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    #Test if bfs reaches all nodes
    tiny_network_graph = Graph('data/tiny_network.adjlist')
    traversal = tiny_network_graph.bfs('Luke Gilbert')
    assert len(traversal) == 30

    #Test if KeyError is raised if start node is not in graph.
    with pytest.raises(KeyError):
        tiny_network_graph.bfs('George')

    #Check bfs node traversal order against netwrokx built in bfs traversal order
    graph = nx.read_adjlist('data/tiny_network.adjlist', create_using=nx.DiGraph, delimiter=";")
    certified_bfs_order = []
    for node in nx.bfs_edges(graph, 'Atul Butte'):
        certified_bfs_order.append(node[1])
    traversal_order = tiny_network_graph.bfs('Atul Butte')
    traversal_order.pop(0)
    assert traversal_order == certified_bfs_order

    #Test if ValueError is raised by bfs if an empty graph is read in
    empty_graph = Graph('data/empty.adjlist')
    with pytest.raises(ValueError):
        empty_graph.bfs('A')
    
    #Test if ValueError is raised by bfs if an unconnected graph is read in
    unconnected_graph = Graph('data/unconnected.adjlist')
    with pytest.raises(ValueError):
        unconnected_graph.bfs('A')
    





def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    #Test if bfs retuns a list when supplied a start and end that are connected
    citation_network_graph = Graph('data/citation_network.adjlist')
    start = 'Atul Butte'
    end = 'Katie Pollard'
    bfs_search = citation_network_graph.bfs(start, end)
    assert type(bfs_search) == list

    #Test if bfs and networkx built in function find shortest paths with the same length
    nx_graph = nx.read_adjlist('data/citation_network.adjlist', create_using=nx.DiGraph, delimiter=";")
    assert len(bfs_search) == len(nx.shortest_path(nx_graph, start, end))

    #Test if bfs and networkx built in function find shortest paths with the same length, with a different start and end
    start = 'Elad Ziv'
    end = 'Hao Li'
    bfs_search = citation_network_graph.bfs(start, end)
    assert len(bfs_search) == len(nx.shortest_path(nx_graph, start, end))

    #Test if bfs returns none when start and end nodes are not connected
    assert citation_network_graph.bfs('Reza Abbasi-Asl', 'Hao Li') == None

    #Test if ValueError is raised by bfs if an empty graph is read in
    empty_graph = Graph('data/empty.adjlist')
    with pytest.raises(ValueError):
        empty_graph.bfs('A', 'B')

    #Test if KeyError is raised if start node is not in graph.
    with pytest.raises(KeyError):
        citation_network_graph.bfs('George', 'Hao Li')

    #Test if KeyError is raised if end node is not in graph
    with pytest.raises(KeyError):
        citation_network_graph.bfs('Elad Ziv', 'Lily')

    #Test if KeyError is raised if neither start nor end node is in the graph
    with pytest.raises(KeyError):
        citation_network_graph.bfs('George', 'Lily')
