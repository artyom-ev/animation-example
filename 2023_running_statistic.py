# Imports
import pandas as pd
import seaborn as sns
import glob
import os
from natsort import natsorted
import moviepy.editor as mpy

# Dataset
df = pd.read_csv('2023_running_statistic.csv', parse_dates=['Date'])
# Sorting dates in ascending order
df = (df.sort_values(by='Date', ascending=True)
        .reset_index()
        .drop(columns='index'))

# Calculating total distance and converting to kilometers
df['Total_distance'] = df['Distance'].cumsum()
df['Total_distance'] = df['Total_distance'] / 1000

length = len(df.index)
folder_name = 'plots'
os.mkdir(folder_name)
for i in range(1, length+1):
    sns.set_theme()
    ax = (df[['Date', 'Total_distance']].iloc[:i]
            .plot(x='Date', y='Total_distance', 
            figsize=(12, 8), 
            linewidth=5, 
            color=['#2CAEA3']))
    ax.set_title('Running distance covered in 2023', fontsize=20)
    ax.set_xlabel('Date', fontsize=15)
    ax.set_ylabel('Total Distance (km)', fontsize=15)
    ax.legend(loc='upper left', frameon=True)
    ax.grid(axis='x')
    fig = ax.get_figure()
    fig.savefig(f'plots/{i}.png')

# Gif 
gif_name = 'Running distance covered in 2023'
file_list = natsorted(glob.glob('plots/*'))
fps = 5
clip = mpy.ImageSequenceClip(file_list, fps=fps)
clip.write_gif(f'{gif_name}.gif', fps=fps)