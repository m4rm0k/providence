# gencomp - convert ordinals to c texture content
# Copyright (C) 2017/2018 Alexander Kraus <nr4@z10.info>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import freetype
import numpy
import struct
import sys
    
# Rescale to [-1., 1.]
def rescale(x):
    xmax = -1.e9
    xmin = 1.e9
    for xi in x:
        xmax = max(xmax, xi)
        xmin = min(xmin, xi)
    ret = []
    for xi in x:
        ret += [ -1. + 2.*(xi-xmin)/(xmax-xmin) ]
    return ret

# Read string database
strings = None
with open('strings.txt', 'rt', newline='\n') as f:
    strings = f.readlines()
    f.close()

# Get the list of unique contained ordinals
ordinals = sorted(list(set(''.join(strings).replace('\n', ''))))
nglyphs = len(ordinals)
print("Packing glyph data of: ", ordinals)

# Open font file
font = freetype.Face('../thirdparty/Roboto_Mono/RobotoMono-Regular.ttf')
font.set_char_size(48*64)

# Specify format, it is signed 16-bit ieee float
fmt = '@e'

# Pack number of chars
texture = struct.pack(fmt, float(len(ordinals)));
data = bytes(0)
index = bytes(0)
offset = 2 + 2 * len(ordinals)

# Pack the ordinals
for char in ordinals:
    print("Processing char: "+char)
    
    # pack offset
    index += struct.pack(fmt, float(ord(char))) + struct.pack(fmt, float(offset))
    
    # Load glyph outline
    font.load_char(char)
    glyph = font.glyph
    outline = glyph.outline
    
    # Get outline points
    points = numpy.array(outline.points, dtype=[('x',float), ('y',float)]) 
    x = list(points['x'])
    y = list(points['y'])
    
    x = rescale(x)
    y = rescale(y)
    
    # pack glyph data
    n = len(x)
    ncont = len(outline.contours)

    glyph_data = struct.pack(fmt, n)
    for xi in x:
        glyph_data += struct.pack(fmt, xi)
    for yi in y:
        glyph_data += struct.pack(fmt, yi)
    for ti in outline.tags:
        glyph_data += struct.pack(fmt, ti)
    glyph_data += struct.pack(fmt, ncont)
    if ncont != 0:
        for ci in outline.contours:
            glyph_data += struct.pack(fmt, ti)
            
    # pack offset
    offset += 3*n + ncont + 2
    
    data += glyph_data

# Assemble texture
texture += struct.pack(fmt, float(offset)) + index + data

print("Packing string database.")
# Pack the string database index
offset += 1 + 2*len(strings)

# Pack the database length
texture += struct.pack(fmt, float(len(strings)))

# Pack the database index
for string in strings:
    # Pack offset
    texture += struct.pack(fmt, float(offset))
    
    # Pack size
    texture += struct.pack(fmt, float(len(string)));
    
    # Update offset. We waste loads of space here by packing floats instead of chars! but I do not want to distinguish between two data types.
    offset += len(string)
    
# Pack the database
for string in strings:
    for char in string:
        texture += struct.pack(fmt, float(ord(char)))

print("Finished packing texture.")

#Generate C header text with texture data
# Write output to c header file or stdout
# Fill last 4-byte-block with zero
length = int(len(texture)) # in bytes
while ((length % 4) != 0):
    texture += bytes(1)
    length += 1
print("Packed font and text database is "+str(length)+" bytes.")

# Get necessary texture size from data
texs = str(int(numpy.ceil(numpy.sqrt(float(length)/4.))))
print("Required texture size: " + texs)

# Generate output header file
array = []
arrayf = []
for i in range(int(numpy.ceil(length/2))):
    array += [ struct.unpack('@H', texture[2*i:2*i+2]) ][0] 
    arrayf += [ struct.unpack(fmt, texture[2*i:2*i+2]) ][0]
text = "// Generated by tx210 (c) 2018 NR4/Team210\n\n#ifndef FONT_H\n#define FONT_H\n\n"
text += "// Data:\n//"
for val in arrayf:
    text += ' ' + str(val) + ','
text += "\nconst unsigned short font_texture[{:d}]".format(int(numpy.ceil(length/2)))+" = {"
for val in array[:-1]:
    text += str(val) + ',' 
text += str(array[-1]) + '};\n'
text += "const int font_texture_size = " + str(texs) + ";"
text += '\n#endif\n'

# Write to file
with open("font.h", "wt", newline='\n') as f:
    f.write(text)
    f.close()
