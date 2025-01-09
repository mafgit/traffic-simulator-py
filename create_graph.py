def create_graph(graph):
    # adding vertices
    graph.add_vertex('A', (100, 100))
    graph.add_vertex('B', (300, 100))
    graph.add_vertex('C', (500, 100))
    graph.add_vertex('D', (700, 100))
    graph.add_vertex('E', (900, 100))
    graph.add_vertex('F', (100, 300))
    graph.add_vertex('G', (900, 300))
    graph.add_vertex('H', (100, 400))
    graph.add_vertex('I', (900, 400))
    graph.add_vertex('J', (100, 600))
    graph.add_vertex('K', (300, 600))
    graph.add_vertex('L', (500, 600))
    graph.add_vertex('M', (700, 600))
    graph.add_vertex('N', (900, 600))
    graph.add_vertex('O', (500, 300))
    graph.add_vertex('P', (500, 400))

    # adding intersections
    

    # adding bidirectional edges
    graph.add_edge('A', 'B',dist=1, bi=True)
    graph.add_edge('B', 'C',dist=1, bi=True)
    graph.add_edge('C', 'D',dist=1, bi=True)
    graph.add_edge('D', 'E',dist=1, bi=True)
    graph.add_edge('J', 'K',dist=1, bi=True)
    graph.add_edge('K', 'L',dist=1, bi=True)
    graph.add_edge('L', 'M',dist=1, bi=True)
    graph.add_edge('M', 'N',dist=1, bi=True)
    graph.add_edge('A', 'F',dist=1, bi=True)
    graph.add_edge('F', 'A',dist=1, bi=True)
    graph.add_edge('G', 'E',dist=1, bi=True)
    graph.add_edge('E', 'G',dist=1, bi=True)
    graph.add_edge('H', 'J',dist=1, bi=True)
    graph.add_edge('J', 'H',dist=1, bi=True)
    graph.add_edge('I', 'N',dist=1, bi=True)
    graph.add_edge('N', 'I',dist=1, bi=True)
    graph.add_edge('O', 'P',dist=1, bi=True)

    # adding single direction edges
    graph.add_edge('F', 'O',dist=1, bi=False)
    graph.add_edge('O', 'G',dist=1, bi=False)
    graph.add_edge('I', 'P',dist=1, bi=False)
    graph.add_edge('P', 'H',dist=1, bi=False)
