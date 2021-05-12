import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt

def save_figure(file_name,subfolder_name=False):
    """ Function to save the figure in folder 'plots' and optional subfolder"""
    if subfolder_name:
    	directory = f'plots/{subfolder_name}'
    else:
    	directory = 'plots'

    # Make folder if doesn't exist
    Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Save file
    filepath_full = f'{directory}/{file_name}.png'
    plt.savefig(fname=filepath_full,format='png')