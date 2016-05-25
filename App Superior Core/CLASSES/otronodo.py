# -*- coding: utf-8 -*-

#import networkx as nx
#import matplotlib.pyplot as plt
from PyQt4 import QtCore, QtGui
from UI_CLASSES.info_grupo import Ui_info_grupo


class Otronodo (QtGui.QDialog):

    def __init__(self,usuarios):
        super(Otronodo , self).__init__()
        self.info=Ui_info_grupo()
        self.info.setupUi(self)
        self.aux=[]
        self.usuarios=usuarios
        self.G=nx.Graph()
        self.nodos()

    def nodos(self):
        if len(self.usuarios) != 0:
            for i in self.usuarios:
                self.aux.append(i.email)

        self.G.add_edge(self.aux[0],self.aux[1],weight=0.5)

        pos=nx.spring_layout(self.G)
        # nodos a dibujar
        nx.draw_networkx_nodes(self.G,pos,node_size=700,alpha=0.3, node_color="blue")
        # enlaces o atributos
        nx.draw_networkx_edges(self.G,pos,width=3,alpha=0.5,edge_color='gray')
            # textos
        nx.draw_networkx_labels(self.G,pos,font_size=12,font_family='arial')
        nx.draw_networkx_edge_labels(self.G,pos,
    {
        (self.aux[0],self.aux[1]):"x"
    }
)
        plt.show() # display