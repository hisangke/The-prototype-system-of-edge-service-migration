import networkx as nx
from Graph_Matrix import Graph_Matrix
class MaximumFlow:
    def __init__(self,adjacencyMatrixData,nodesNumber=10):
        self.adjacencyMatrixData=adjacencyMatrixData
        self.nodesNumber=nodesNumber
        self.my_graph=Graph_Matrix(vertices=list(range(len(adjacencyMatrixData[0]))),matrix=adjacencyMatrixData) #vertices=[], matrix=[]
        self.created_graph=self.__create_undirected_matrix()
        self.G=self.__draw_undircted_graph()
    def __create_undirected_matrix(self):
        nodes=list(range(len(self.adjacencyMatrixData[0])))
        return Graph_Matrix(nodes,self.adjacencyMatrixData)

    def __draw_undircted_graph(self):
        graph=nx.Graph()
        for node in self.created_graph.vertices:
            graph.add_node(node)
        for edge in self.created_graph.edges:
            graph.add_edge(edge[0],edge[1],cost=6)
        return graph

    def value(self,source,target):
        graph=nx.Graph()
        for edge in self.G.edges():
            new_edge=(edge[0],edge[1],self.adjacencyMatrixData[edge[0]][edge[1]])
            graph.add_edge(new_edge[0],new_edge[1],capacity=new_edge[2])
        flow_value, flow_dict = nx.maximum_flow(graph, source, target)
        return flow_value
