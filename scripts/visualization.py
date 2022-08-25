#!/usr/bin/env python3
import logging

logging.basicConfig(format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

from matplotlib import pyplot
import pandas as pd
import numpy

class Visualization:
    """Class for data understanding through visualization"""
    def __init__(self, df):
        logging.info("Visualization object created")
        self.df = df

    def draw_hist(self):
        """Draw histograms"""
        logging.info("Draw Histogram")
        self.df.hist()
        pyplot.show()

    def draw_density_plot(self, l):
        """Density plots
            Attributes:
                l: Layout
        """
        t = True
        f = False
        logging.info("Draw density plot")
        self.df.plot(kind= 'density', subplots=t, layout=l, sharex=f)
        pyplot.show()

    def draw_box_plots(self, l):
        """Draw Box Plots
            Attributes:
                l: Layout
        """
        t = True
        f = False
        logging.info("Draw box plots")
        self.df.plot(kind= 'box', subplots=t, layout=l, sharex=f, sharey=f)
        pyplot.show()
    def draw_bar(self, title, x, y):
        self.df.plot(kind="bar", title="test")
        pyplot.title(title)
        pyplot.xlabel(x)
        pyplot.ylabel(y)
        pyplot.show()

    #Multivariant Plots
    def draw_correlation_matrix(self):
        """Draw Correlation matrixgraph"""
        logging.info("Draw correlation matrix")
        corr = self.df.corr()
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(corr, vmin=-1, vmax=1)
        fig.colorbar(cax)
        pyplot.show()

    def draw_scatter(self):
        """Scatter graph"""
        logging.info("Draw Scatter")
        pd.plotting.scatter_matrix(self.df)
        pyplot.show()
