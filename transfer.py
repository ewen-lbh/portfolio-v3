import os
import re
p = r'D:\#\Coding\projects\mx3creations\static\download\music'
for f in os.listdir(p):
    if f.endswith('-wide-cover-art.jpeg'):
        d = f.replace('-wide-cover-art.jpeg', '')
        os.makedirs(os.path.join(p, d), exist_ok=True)
        os.rename(os.path.join(p, f), os.path.join(p, d,'wide-cover-art.jpeg'))