# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import networkx as nx



class Graficos():

    def __init__(self):
        super(Graficas, self).__init__()

    def DiagramaDeBarras(lista):

        listaEnviados = []
        listaRecibidos = []
        listaNombres = []
        cont = 0

        for i in lista:
            nombre, enviados, recibidos = lista[cont]
            listaNombres.append(nombre)
            listaEnviados.append(enviados)
            listaRecibidos.append(recibidos)
            cont = cont + 1

        """se obtiene de la lista recibida los nombres, la cantidad de los correos enviados y
            la cantidad de correos recibidos del usuario"""

        cantCorreos = []
        cantCorreos.append(listaEnviados)
        cantCorreos.append(listaRecibidos)

        """En cantCorreos la posición [0] son los enviados, la posición [1] son los recibidos"""

        cantPersonas =  len(listaNombres) #Cantidad de las personas en el grupo
        X = np.arange(cantPersonas)

        espacio = 0
        colores = '0.0'
        inc = 1

        for i in range(len(cantCorreos)):
            plt.bar(X + espacio, cantCorreos[i], color = colores, width = 0.25)
            esto = float(colores) + inc
            colores = repr(esto)
            espacio = 0.25

        plt.xticks(X + 0.38, listaNombres) #etiquetas en el eje X
        enviados = mpatches.Patch(color='k', label='enviados')
        recibidos = mpatches.Patch(color='w', label='recibidos')

        plt.legend(handles=[enviados,recibidos])
        plt.show()

    def graficaEnviados(lista):

        graph_layout='circular'
        node_size=1600
        node_color='blue'
        node_alpha=0.5
        node_text_size=12
        edge_color='blue'
        edge_alpha=0.5
        edge_tickness=1
        edge_text_pos=0.5 #posicion de la etiqueta en la línea
        text_font='sans-serif'

        # creacion de gráfico de networkX
        G=nx.DiGraph()

        listaEnviados = []
        listaNombres = []
        cont = 0

        for i in lista:
            nombre, enviados, recibidos = lista[cont]
            listaNombres.append(('yo', nombre))
            listaEnviados.append(enviados)
            cont = cont + 1

        """en listaNombres las ids de las personas que conforman el grupo.
            En la posición 1 de todas las tuplas irá el usuario actual"""

        labels = range(len(listaNombres))

        # agregando los edges (las líneas entre los nodos)
        for edge in listaNombres:
            G.add_edge(edge[0], edge[1])

        if graph_layout == 'circular' :
            graph_pos=nx.circular_layout(G) #Estilo de la gráfica

        # dibujando: la gráfica
        nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
        #parámetros: la gráfica, estilo de gráfica, tamaño, opacidad y color
        nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
        #parámetros: la gráfica, estilo de la gráfica, grosor, opacidad, color
        nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)
        #parámetros: la gráfica, estilo de la gráfica, tamaño de la fuente, tipo de fuente

        edgelabels = dict(zip(listaNombres,listaEnviados)) #creación de un diccionario

        edge_labels = dict(zip(listaNombres, labels)) #creación de un diccionario
        nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edgelabels,
                                 label_pos=0.5)
        """parámetros: la gráfica, estilo de la gráfica, etiquetas de las líneas,
           posición de las etiquetas en la línea"""

        # mostrar la gráfica
        plt.show()

    def graficaRecibidos(lista):

        graph_layout='circular'
        node_size=1600
        node_color='blue'
        node_alpha=0.5
        node_text_size=12
        edge_color='blue'
        edge_alpha=0.5
        edge_tickness=1
        edge_text_pos=0.5 #posicion de la etiqueta en la línea
        text_font='sans-serif'

        # creacion de gráfico de networkX
        G=nx.DiGraph()

        listaRecibidos = []
        listaNombres = []
        cont = 0

        for i in lista:
            nombre, enviados, recibidos = lista[cont]
            listaNombres.append((nombre,'yo'))
            listaRecibidos.append(recibidos)
            cont = cont + 1

        """en listaNombres las ids de las personas que conforman el grupo.
            En la posición 1 de todas las tuplas irá el usuario actual"""

        labels = range(len(listaNombres))

        # agregando los edges (las líneas entre los nodos)
        for edge in listaNombres:
            G.add_edge(edge[0], edge[1])

        if graph_layout == 'circular' :
            graph_pos=nx.circular_layout(G) #Estilo de la gráfica

        # dibujando: la gráfica
        nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                           alpha=node_alpha, node_color=node_color)
        #parámetros: la gráfica, estilo de gráfica, tamaño, opacidad y color
        nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
        #parámetros: la gráfica, estilo de la gráfica, grosor, opacidad, color
        nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)
        #parámetros: la gráfica, estilo de la gráfica, tamaño de la fuente, tipo de fuente

        edgelabels = dict(zip(listaNombres,listaRecibidos)) #creación de un diccionario

        edge_labels = dict(zip(listaNombres, labels)) #creación de un diccionario
        nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edgelabels,
                                 label_pos=0.5)
        """parámetros: la gráfica, estilo de la gráfica, etiquetas de las líneas,
           posición de las etiquetas en la línea"""

        # mostrar la gráfica
        plt.show()