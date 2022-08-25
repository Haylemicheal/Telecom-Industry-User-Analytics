#!/usr/bin/env python3
import logging

logging.basicConfig(format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

from matplotlib import pyplot
import pandas as pd
import numpy
import seaborn as sns

class Visualization:
    """Class for data understanding through visualization"""
    def __init__(self, df):
        logging.info("Visualization object created")
        self.df = df

    def draw_hist(self):
        """Draw histograms"""
        logging.info("Draw Histogram")
        sns.set(style="darkgrid")
        sns.histplot(data=self.df)
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

    def draw_box_plots(self):
        """Draw Box Plots
            Attributes:
                l: Layout
        """
        t = True
        f = False
        logging.info("Draw box plots")
        pyplot.figure(figsize=(12, 7))
        sns.boxplot(data=self.df)
        pyplot.show()

    def draw_bar(self, title, x, y):
        pyplot.figure(figsize=(12, 7))
        self.df.plot(kind="bar")
        pyplot.title(title)
        pyplot.xlabel(x)
        pyplot.ylabel(y)
        pyplot.show()

    #Multivariant Plots
    def draw_correlation_matrix(self):
        """Draw Correlation matrixgraph"""
        logging.info("Draw correlation matrix")
        pyplot.figure(figsize=(12, 7))
        corr = self.df.corr()
        fig = pyplot.figure()
        ax = fig.add_subplot(111)
        cax = ax.matshow(corr, vmin=-1, vmax=1)
        fig.colorbar(cax)
        pyplot.show()

    def draw_scatter(self):
        """Scatter graph"""
        logging.info("Draw Scatter")
        pyplot.figure(figsize=(12, 7))
        sns.scatterplot(data=self.df)
        pyplot.show()
