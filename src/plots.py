from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

import src.plot_functions as pf

def distribution_plot(df, column,hue=False):
	"""Plot a subplot with boxplot, violinplot and histogram to show distribution of a numeric column"""
	fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8), sharex=True)

	# ax1 : boxplot
	if hue:
		sns.boxplot(x=df[column],y=df[hue], ax=ax1)
	else:
		sns.boxplot(x=df[column], ax=ax1)

	# ax2 : violinplot
	if hue:
		sns.violinplot(x=df[column],y=df[hue], ax=ax2)
	else:
		sns.violinplot(df[column], ax=ax2)

	# ax3 : histogram 
	if hue:
		sns.histplot(data=df, kde=True, x=column, hue=hue,ax=ax3)
	else:
		pass
		sns.histplot(data=df, kde=True, x=column,ax=ax3)
		ax3.axvline(df[column].median(), label="median", alpha=1, color="g", lw=2)
		ax3.axvline(df[column].mean(), label="mean", alpha=1, color="r", lw=2)
		ax3.legend()

	# plot style
	plt.yticks([])

	for ax in [ax1, ax2]:
		ax.set_xlabel("")

	if hue:
		file_name = f"{column.title()} Distribution, split by {hue}"
		ax1.set_title(file_name)
	else:
		file_name = f"{column.title()} Distribution"
		ax1.set_title(file_name)

	pf.save_figure(
		file_name=file_name,
		subfolder_name="01.1.1 Basic EDA - Distributions",
	)