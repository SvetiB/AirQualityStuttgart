import pandas as pd  # u.a. verwendet um DataFrames zu generieren und zu bearbeiten
import numpy as np
import json  # Bearbeitung von json-Files
import seaborn as sns # Visualisierungen
from matplotlib import pyplot as plt


def heatMap(df):
    corr = df.corr() #Create Correlation df
    fig, ax = plt.subplots(figsize=(10, 10)) #Plot figsize
    colormap = sns.diverging_palette(220, 10, as_cmap=True) #Generate Color Map
    sns.heatmap(corr, cmap=colormap, annot=False, fmt=".2f") #Generate Heat Map, allow annotations and place floats in map
    plt.show()

def heatMapSmall(df):
    corr = df.corr() #Create Correlation df
    fig, ax = plt.subplots(figsize=(7, 7)) #Plot figsize
    colormap = sns.diverging_palette(220, 10, as_cmap=True) #Generate Color Map
    sns.heatmap(corr, cmap=colormap, annot=False, fmt=".2f") #Generate Heat Map
    plt.show() #show plot

def heatMapBig(df):
    corr = df.corr() #Create Correlation df
    fig, ax = plt.subplots(figsize=(12, 12)) #Plot figsize
    colormap = sns.diverging_palette(220, 10, as_cmap=True) #Generate Color Map
    sns.heatmap(corr, cmap=colormap, annot=False, fmt=".2f") #Generate Heat Map
    plt.show() #show plot
