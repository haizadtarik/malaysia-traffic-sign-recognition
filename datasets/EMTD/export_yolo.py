import pandas as pd
import cv2
import os

pd.set_option('mode.chained_assignment', None)

df = pd.read_csv('GT.csv')

for filename in os.listdir('images'):
    temp_df = df[df['filename'] == filename]
    del temp_df['filename']

    h, w, c = cv2.imread('images/'+filename).shape
    temp_df['xmax'] = temp_df['xmax'].div(w)
    temp_df['ymax'] = temp_df['ymax'].div(h)
    temp_df['xmin'] = temp_df['xmin'].div(w)
    temp_df['ymin'] = temp_df['ymin'].div(h)
    temp_df['Class ID'] = temp_df['Class ID'] - 1
    temp_df['xcenter'] = temp_df['xmin'] + ((temp_df['xmax'] - temp_df['xmin'])/2) 
    temp_df['ycenter'] = temp_df['ymin'] + ((temp_df['ymax'] - temp_df['ymin'])/2)
    temp_df['width'] = temp_df['xmax'] - temp_df['xmin'] 
    temp_df['height'] = temp_df['ymax'] - temp_df['ymin']
    del temp_df['xmax']
    del temp_df['ymax']
    del temp_df['xmin']
    del temp_df['ymin']
    temp_df.to_csv('labels/{}.txt'.format(filename.split('.')[0]), header=None, index=None, sep=' ')
