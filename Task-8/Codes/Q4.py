import pandas as pd

ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
title = ser.str.title()
txt = ''
for i in title:
    txt += i + " "

print(txt)