# Endeavor by Team210 - 64k intro by Team210 at Revision 2k19
# Copyright (C) 2018  Alexander Kraus <nr4@z10.info>
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import numpy
import struct
import font

# Pack everything as float. If executable size is a problem, this can be optimized slightly.
# Pack alignment:
# string database offset
# nglyphs
# for glyph in glyphs
#     ordinal
#     offset
# for glyph in glyphs
#     nlines
#     for line in lines
#         x1 y1 x2 y2
#     nsmoothlines
#     for line in smoothlines
#         x1 y1 x2 y2
# nstrings
# for string in nstrings
#     offset
#     length
# for string in nstrings
#     for char in string
#         char

# Read string database
strings = None
with open('strings.txt', 'rt', newline='\n') as f:
    strings = f.readlines()
    f.close()

# Font has only lowercase letters
for i in range(len(strings)):
    strings[i] = strings[i].lower().strip()
    
# Get the list of unique contained ordinals
ordinals = sorted(list(set(''.join(strings).replace('\n', ''))))
nglyphs = len(ordinals)
print("Packing glyph data of: ", ordinals)

# Pack number of glyphs
fmt = '@e'
texture = struct.pack(fmt, float(len(ordinals)));

# Pack the according glyph table
pack_len = 2 + nglyphs * 2
table = ""
for char in ordinals:
    # Pack ordinal
    texture += struct.pack(fmt, float(ord(char)))
    
    # Pack offset
    texture += struct.pack(fmt, float(pack_len))
    
    # Update offset
    pack_len += font.pack_length(char)
    
# Pack string database intex
texture = struct.pack(fmt, float(pack_len)) + texture

# Pack the glyph data
for char in ordinals:
    # Get glyph inlines
    glyph = font.glyph(char)
    
    # Pack number of lines
    lines = glyph[0]
    texture += struct.pack(fmt, float(len(lines)))
    
    # Pack lines
    for line in lines:
        for i in range(4):
            texture += struct.pack(fmt, float(line[i]))
            
    # Pack number of smoothlines
    smoothlines = glyph[1]
    texture += struct.pack(fmt, float(len(smoothlines)))
    
    # Pack smoothlines
    for line in smoothlines:
        for i in range(4):
            texture += struct.pack(fmt, float(line[i]))

print("Packing string database.")
# Pack the string database index
offset = pack_len + 1 + 2*len(strings)

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



