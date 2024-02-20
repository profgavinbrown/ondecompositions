from IPython.display import display, HTML
display(HTML(""" <style> div.output_scroll {height: 35em; } </style> """))


import matplotlib.pyplot as plt
plt.rcParams.update({
    'font.size': 8,
    'font.family': 'sans-serif',
    'font.sans-serif': 'Helvetica',
    #'text.usetex': True,
    'text.latex.preamble': r'\usepackage{amsfonts}'
})

#mpl.rcParams.update(mpl.rcParamsDefault)


import numpy as np

from copy import deepcopy

from numpy.linalg import pinv

from sklearn.metrics import mean_squared_error, log_loss
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, RidgeCV
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_regression

