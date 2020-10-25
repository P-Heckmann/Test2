import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
from collections import namedtuple

#Rocktype = ['Anorthosite','Troctolite','Gabbronorite','Bt Gabbronorite','Peridotite','Mt Gabbronorite','Pyroxenite','Plag Websterite']
#label = ['Anorthosite','Troctolite','Gabbronorite','Bt Gabbronorite','Peridotite','Mt Gabbronorite','Pyroxenite','Plag Websterite']
#color = ['#bac0d7','#12e8be','#74e812','#e87a12','#e81912','#132d52','#b0605f','#bb3c96']

Rocktype = ['Altered breccia','Diabase','Gneiss','Granitoid','Metasuprakrustal','Mixed rock','Qtz diorite','Xenolite']
label = ['Altered breccia','Diabase','Gneiss','Granitoid','Metasuprakrustal','Mixed rock','Qtz diorite','Xenolite']
color = ['#bac0d7','#12e8be','#74e812','#e87a12','#e81912','#132d52','#b0605f','#bb3c96']

#data = pd.read_excel('data/RawData.xlsx')
#data = pd.read_excel('data/alle_analyser_sorted_plag_websterite_color.xlsx')
data = pd.read_excel('data/alle_analyser.xlsx')
#data.head(2) 

X = data.Rocktype.unique()
#print(X)

FieldLine = namedtuple('FieldLine', 'x1 y1 x2 y2')
lines = (FieldLine(x1=41, y1=0, x2=41, y2=7),
    FieldLine(x1=41, y1=7, x2=52.5, y2=14),
    FieldLine(x1=45, y1=0, x2=45, y2=5),
    FieldLine(x1=41, y1=3, x2=45, y2=3),
    FieldLine(x1=45, y1=5, x2=61, y2=13.5),
    FieldLine(x1=45, y1=5, x2=52, y2=5),
    FieldLine(x1=52, y1=5, x2=69, y2=8),
    FieldLine(x1=49.4, y1=7.3, x2=52, y2=5),
    FieldLine(x1=52, y1=5, x2=52, y2=0),
    FieldLine(x1=48.4, y1=11.5, x2=53, y2=9.3),
    FieldLine(x1=53, y1=9.3, x2=57, y2=5.9),
    FieldLine(x1=57, y1=5.9, x2=57, y2=0),
    FieldLine(x1=52.5, y1=14, x2=57.6, y2=11.7),
    FieldLine(x1=57.6, y1=11.7, x2=63, y2=7),
    FieldLine(x1=63, y1=7, x2=63, y2=0),
    FieldLine(x1=69, y1=12, x2=69, y2=8),
    FieldLine(x1=45, y1=9.4, x2=49.4, y2=7.3),
    FieldLine(x1=69, y1=8, x2=77, y2=0))

FieldName = namedtuple('FieldName', 'name x y rotation')
names = (FieldName('Picro\nbasalt', 43, 2, 0),
    FieldName('Basalt', 48.5, 2, 0),
    FieldName('Basaltic\nandesite', 54.5, 2, 0),
    FieldName('Andesite', 60, 2, 0),
    FieldName('Dacite', 68.5, 2, 0),
    FieldName('Rhyolite', 76, 9, 0),
    FieldName('Trachyte\n(Q < 20%)\n\nTrachydacite\n(Q > 20%)',
                       64.5, 11.5, 0),
    FieldName('Basaltic\ntrachyandesite', 53, 8, -20),
    FieldName('Trachy-\nbasalt', 49, 6.2, 0),
    FieldName('Trachyandesite', 57.2, 9, 0),
    FieldName('Phonotephrite', 49, 9.6, 0),
    FieldName('Tephriphonolite', 53.0, 11.8, 0),
    FieldName('Phonolite', 57.5, 13.5, 0),
    FieldName('Tephrite\n(Ol < 10%)', 45, 8, 0),
    FieldName('Foidite', 44, 11.5, 0),
    FieldName('Basanite\n(Ol > 10%)', 43.5, 6.5, 0))

    # Plot the lines and fields
for line in lines:
    plt.plot([line.x1, line.x2], [line.y1, line.y2],
    '-',color='black',zorder=0)

for name in names:
    plt.text(name.x, name.y, name.name, color='Black', size=15,
    horizontalalignment='center', verticalalignment='top',
    rotation=name.rotation, zorder=0)
    


for x,y,z in zip(Rocktype,label,color):
    plt.scatter(data.loc[data['Rocktype'] == x].SiO2,data.loc[data['Rocktype'] == x].K2O+data.loc[data['Rocktype'] == x].Na2O,label=y,color=z)

    

plt.rcParams.update({'font.size': 20})
#plt.title("TAS diagram")
plt.xlabel(r'SiO$_2$ (wt%)')  
plt.ylabel(r'Na$_2$O + K$_2$O (wt%)')

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.rcParams['figure.figsize'] = [16, 8]
plt.rcParams["font.family"] = "Times New Roman"
plt.savefig('figures/TAS_others.pdf', bbox_inches='tight')
plt.savefig('figures/TAS_others.png',dpi=300, bbox_inches='tight')
plt.show()