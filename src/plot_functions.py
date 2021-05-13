import pandas as pd
from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np

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
    
def show_values_on_bars(axs,round_annot=True,fontsize=12,append_pct_sign=False,thousands_of_pounds=False,millions_of_pounds=False,pos_offset=100,neg_offset=10):
    """ Code I got from stackoverflow and then further modified 
    Only got it to work with plots with a single set of data, but I reckon it could be tweaked to work with more 
    Original code : https://stackoverflow.com/questions/43214978/seaborn-barplot-displaying-values
    
    Keyword arguments:
    round_annot -- if True, rounds the data labels to whole numbers. I added code to let you switch this off for % change graphs, as 84% increase would be 0.84 and would be rounded up
    """
    
    def _show_on_single_plot(ax,pos_offset=pos_offset,neg_offset=neg_offset):        
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2 # gets x position
            _y = p.get_y() + p.get_height() # gets y position
            
            # adding a buffer to the data label so it's slightly above the bar (or below if it's negative)
            if _y >= 0:
                _y = _y + (ax.get_ylim()[1])/pos_offset # adds 1% of length of ylim to add a bit of buffer to the data label so it isn't sitting directly on the bar
            elif _y < 0:
                _y = _y - (ax.get_ylim()[1])/neg_offset # adds 1% of length of ylim to add a bit of buffer to the data label so it isn't sitting directly on the bar

            # round annotation to remove decimals, or don't
            if round_annot == True:
                value = '{:.0f}'.format(p.get_height())
            elif round_annot == False:
                value = '{:.2f}'.format(p.get_height()) ### original code -> 2 decimal places 
            elif round_annot == 3:
                value = '{:.3f}'.format(p.get_height()) ### original code -> 2 decimal places
                
            # divide by something to make it easier to read if annotation is > 1 million (for sales value graph)
            #if float(value) > 1_000_000:
            #    value = float(value)/1_000_000
            #    value = round(value,2)
            #    value = str(value) + 'm'
            #else:
            #    pass

            if append_pct_sign:
                value = value + '%'
            else:
                pass
            
            if thousands_of_pounds:
                value = round(float(value)/1000,1)
                value = '£'+str(value)+'k'

            if millions_of_pounds:
                value = round(float(value)/1_000_000,1)
                value = '£'+str(value)+'m'

            ax.text(_x, _y, value, ha="center",fontfamily='monospace',fontweight='extra bold',fontsize=fontsize,color='k') 

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs,pos_offset=pos_offset,neg_offset=neg_offset):
            _show_on_single_plot(ax,pos_offset=pos_offset,neg_offset=neg_offset)
    else:
        _show_on_single_plot(axs)