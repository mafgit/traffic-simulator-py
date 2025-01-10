def create_graph(graph):
    # LEFT

    # adding vertices
    graph.add_vertex('LA', (100, 100))
    graph.add_vertex('LB', (300, 100))
    graph.add_vertex('LC', (500, 100))
    graph.add_vertex('LD', (700, 100))
    graph.add_vertex('LE', (900, 100))
    graph.add_vertex('LF', (100, 200))
    graph.add_vertex('LG', (900, 200))
    graph.add_vertex('LH', (100, 300))
    graph.add_vertex('LI', (900, 300))
    graph.add_vertex('LJ', (100, 400))
    graph.add_vertex('LK', (300, 400))
    graph.add_vertex('LL', (500, 400))
    graph.add_vertex('LM', (700, 400))
    graph.add_vertex('LN', (900, 400))
    graph.add_vertex('LO', (500, 200))
    graph.add_vertex('LP', (500, 300))

    # adding bidirectional edges
    graph.add_edge('LA', 'LB',dist=1, bi=True)
    graph.add_edge('LB', 'LC',dist=1, bi=True)
    graph.add_edge('LC', 'LD',dist=1, bi=True)
    graph.add_edge('LD', 'LE',dist=1, bi=True)
    graph.add_edge('LJ', 'LK',dist=1, bi=True)
    graph.add_edge('LK', 'LL',dist=1, bi=True)
    graph.add_edge('LL', 'LM',dist=1, bi=True)
    graph.add_edge('LM', 'LN',dist=1, bi=True)
    graph.add_edge('LA', 'LF',dist=1, bi=True)
    graph.add_edge('LF', 'LA',dist=1, bi=True)
    graph.add_edge('LG', 'LE',dist=1, bi=True)
    graph.add_edge('LE', 'LG',dist=1, bi=True)
    graph.add_edge('LH', 'LJ',dist=1, bi=True)
    graph.add_edge('LJ', 'LH',dist=1, bi=True)
    graph.add_edge('LI', 'LN',dist=1, bi=True)
    graph.add_edge('LN', 'LI',dist=1, bi=True)
    graph.add_edge('LO', 'LP',dist=1, bi=True)

    # adding single direction edges
    graph.add_edge('LF', 'LO',dist=1, bi=False)
    graph.add_edge('LO', 'LG',dist=1, bi=False)
    graph.add_edge('LI', 'LP',dist=1, bi=False)
    graph.add_edge('LP', 'LH',dist=1, bi=False)

    # RIGHT
    
    # adding vertices
    graph.add_vertex('RA', (1100 + 100, 100))
    graph.add_vertex('RB', (1100 + 300, 100))
    graph.add_vertex('RC', (1100 + 500, 100))
    graph.add_vertex('RD', (1100 + 700, 100))
    graph.add_vertex('RE', (1100 + 900, 100))
    graph.add_vertex('RF', (1100 + 100, 200))
    graph.add_vertex('RG', (1100 + 900, 200))
    graph.add_vertex('RH', (1100 + 100, 300))
    graph.add_vertex('RI', (1100 + 900, 300))
    graph.add_vertex('RJ', (1100 + 100, 400))
    graph.add_vertex('RK', (1100 + 300, 400))
    graph.add_vertex('RL', (1100 + 500, 400))
    graph.add_vertex('RM', (1100 + 700, 400))
    graph.add_vertex('RN', (1100 + 900, 400))
    graph.add_vertex('RO', (1100 + 500, 200))
    graph.add_vertex('RP', (1100 + 500, 300))

    # adding bidirectional edges
    graph.add_edge('RA', 'RB',dist=1, bi=True)
    graph.add_edge('RB', 'RC',dist=1, bi=True)
    graph.add_edge('RC', 'RD',dist=1, bi=True)
    graph.add_edge('RD', 'RE',dist=1, bi=True)
    graph.add_edge('RJ', 'RK',dist=1, bi=True)
    graph.add_edge('RK', 'RL',dist=1, bi=True)
    graph.add_edge('RL', 'RM',dist=1, bi=True)
    graph.add_edge('RM', 'RN',dist=1, bi=True)
    graph.add_edge('RA', 'RF',dist=1, bi=True)
    graph.add_edge('RF', 'RA',dist=1, bi=True)
    graph.add_edge('RG', 'RE',dist=1, bi=True)
    graph.add_edge('RE', 'RG',dist=1, bi=True)
    graph.add_edge('RH', 'RJ',dist=1, bi=True)
    graph.add_edge('RJ', 'RH',dist=1, bi=True)
    graph.add_edge('RI', 'RN',dist=1, bi=True)
    graph.add_edge('RN', 'RI',dist=1, bi=True)
    graph.add_edge('RO', 'RP',dist=1, bi=True)

    # adding single direction edges
    graph.add_edge('RF', 'RO',dist=1, bi=False)
    graph.add_edge('RO', 'RG',dist=1, bi=False)
    graph.add_edge('RI', 'RP',dist=1, bi=False)
    graph.add_edge('RP', 'RH',dist=1, bi=False)

    # TOP

    # adding vertices
    graph.add_vertex('TA', (800 + 100, 200 - 100))
    graph.add_vertex('TB', (800 + 100, 200 - 300))
    graph.add_vertex('TC', (800 + 100, 200 - 500))
    graph.add_vertex('TD', (800 + 100, 200 - 700))
    graph.add_vertex('TE', (800 + 100, 200 - 900))
    graph.add_vertex('TF', (800 + 200, 200 - 100))
    graph.add_vertex('TG', (800 + 200, 200 - 900))
    graph.add_vertex('TH', (800 + 300, 200 - 100))
    graph.add_vertex('TI', (800 + 300, 200 - 900))
    graph.add_vertex('TJ', (800 + 400, 200 - 100))
    graph.add_vertex('TK', (800 + 400, 200 - 300))
    graph.add_vertex('TL', (800 + 400, 200 - 500))
    graph.add_vertex('TM', (800 + 400, 200 - 700))
    graph.add_vertex('TN', (800 + 400, 200 - 900))
    graph.add_vertex('TO', (800 + 200, 200 - 500))
    graph.add_vertex('TP', (800 + 300, 200 - 500))

    # adding bidirectional edges
    graph.add_edge('TA', 'TB',dist=1, bi=True)
    graph.add_edge('TB', 'TC',dist=1, bi=True)
    graph.add_edge('TC', 'TD',dist=1, bi=True)
    graph.add_edge('TD', 'TE',dist=1, bi=True)
    graph.add_edge('TJ', 'TK',dist=1, bi=True)
    graph.add_edge('TK', 'TL',dist=1, bi=True)
    graph.add_edge('TL', 'TM',dist=1, bi=True)
    graph.add_edge('TM', 'TN',dist=1, bi=True)
    graph.add_edge('TA', 'TF',dist=1, bi=True)
    graph.add_edge('TF', 'TA',dist=1, bi=True)
    graph.add_edge('TG', 'TE',dist=1, bi=True)
    graph.add_edge('TE', 'TG',dist=1, bi=True)
    graph.add_edge('TH', 'TJ',dist=1, bi=True)
    graph.add_edge('TJ', 'TH',dist=1, bi=True)
    graph.add_edge('TI', 'TN',dist=1, bi=True)
    graph.add_edge('TN', 'TI',dist=1, bi=True)
    graph.add_edge('TO', 'TP',dist=1, bi=True)

    # adding single direction edges
    graph.add_edge('TF', 'TO',dist=1, bi=False)
    graph.add_edge('TO', 'TG',dist=1, bi=False)
    graph.add_edge('TI', 'TP',dist=1, bi=False)
    graph.add_edge('TP', 'TH',dist=1, bi=False)

    
    # BOTTOM

    # adding vertices
    graph.add_vertex('BA', (800 + 100, 200 - 100 + 1100))
    graph.add_vertex('BB', (800 + 100, 200 - 300 + 1100))
    graph.add_vertex('BC', (800 + 100, 200 - 500 + 1100))
    graph.add_vertex('BD', (800 + 100, 200 - 700 + 1100))
    graph.add_vertex('BE', (800 + 100, 200 - 900 + 1100))
    graph.add_vertex('BF', (800 + 200, 200 - 100 + 1100))
    graph.add_vertex('BG', (800 + 200, 200 - 900 + 1100))
    graph.add_vertex('BH', (800 + 300, 200 - 100 + 1100))
    graph.add_vertex('BI', (800 + 300, 200 - 900 + 1100))
    graph.add_vertex('BJ', (800 + 400, 200 - 100 + 1100))
    graph.add_vertex('BK', (800 + 400, 200 - 300 + 1100))
    graph.add_vertex('BL', (800 + 400, 200 - 500 + 1100))
    graph.add_vertex('BM', (800 + 400, 200 - 700 + 1100))
    graph.add_vertex('BN', (800 + 400, 200 - 900 + 1100))
    graph.add_vertex('BO', (800 + 200, 200 - 500 + 1100))
    graph.add_vertex('BP', (800 + 300, 200 - 500 + 1100))

    # adding bidirectional edges
    graph.add_edge('BA', 'BB',dist=1, bi=True)
    graph.add_edge('BB', 'BC',dist=1, bi=True)
    graph.add_edge('BC', 'BD',dist=1, bi=True)
    graph.add_edge('BD', 'BE',dist=1, bi=True)
    graph.add_edge('BJ', 'BK',dist=1, bi=True)
    graph.add_edge('BK', 'BL',dist=1, bi=True)
    graph.add_edge('BL', 'BM',dist=1, bi=True)
    graph.add_edge('BM', 'BN',dist=1, bi=True)
    graph.add_edge('BA', 'BF',dist=1, bi=True)
    graph.add_edge('BF', 'BA',dist=1, bi=True)
    graph.add_edge('BG', 'BE',dist=1, bi=True)
    graph.add_edge('BE', 'BG',dist=1, bi=True)
    graph.add_edge('BH', 'BJ',dist=1, bi=True)
    graph.add_edge('BJ', 'BH',dist=1, bi=True)
    graph.add_edge('BI', 'BN',dist=1, bi=True)
    graph.add_edge('BN', 'BI',dist=1, bi=True)
    graph.add_edge('BO', 'BP',dist=1, bi=True)

    # adding single direction edges
    graph.add_edge('BF', 'BO',dist=1, bi=False)
    graph.add_edge('BO', 'BG',dist=1, bi=False)
    graph.add_edge('BI', 'BP',dist=1, bi=False)
    graph.add_edge('BP', 'BH',dist=1, bi=False)

    # adding intersections
    graph.add_vertex('ITL', (1000, 200), type="intersection")
    graph.add_vertex('ITR', (1100, 200), type="intersection")
    graph.add_vertex('IBL', (1000, 300), type="intersection")
    graph.add_vertex('IBR', (1100, 300), type="intersection")
    graph.add_edge('LG', 'ITL')
    graph.add_edge('ITL', 'ITR')
    graph.add_edge('ITR', 'IBR')
    graph.add_edge('IBR', 'IBL')
    graph.add_edge('IBL', 'LI')
    graph.add_edge('IBL', 'ITL')
    graph.add_edge('ITR', 'RF')
    graph.add_edge('RH', 'IBR')
    graph.add_edge('ITL', 'TF')
    graph.add_edge('TH', 'ITR')
    graph.add_edge('BG', 'IBL')
    graph.add_edge('IBR', 'BI')
