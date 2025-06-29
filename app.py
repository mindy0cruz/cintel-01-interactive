import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Title
ui.page_opts(title="Shiny Histogram App", fillable=True)

# Sidebar slider
with ui.sidebar():
    ui.input_slider("selected_number_of_bins", "Number of Bins", 0, 100, 20)

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    
    plt.hist(
        x, 
        bins=input.selected_number_of_bins(),  
        density=True,
        color="coral", edgecolor="white"
    )

    plt.title("Histogram of Random Data")
    plt.xlabel("Value")
    plt.ylabel("Density")
