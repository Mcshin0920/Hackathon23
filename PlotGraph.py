# Import libraries
import matplotlib.pyplot as plt
import numpy as np

def graph(value): 
    # Creating vectors X and Y
    x = np.linspace(-10, 10, 100)
    y = value

    fig = plt.figure(figsize = (10, 5))
    # Create the plot
    plt.plot(x, y)
    
    # Save the plot
    plt.savefig('myplot.png')