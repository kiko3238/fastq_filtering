#!/usr/bin/python

# USAGE: python fastqQC.py

# High-quality reads for which > [min_percent]% bases showed Phred quality scores > [min_quality] were extracted.
# Variables [min_percent] and [min_quality] should be specified in below.

import sys

# Specify [min_percent] and [min_quality].
min_quality = 20
min_percent = 0.90

# Specify input FASTQ files.
in_f1 = "read1.fastq"
in_f2 = "read2.fastq"



###### Def ######

fh1 = open(in_f1, 'r')
fh2 = open(in_f2, 'r')

out_fh1 = open('out_read1.fastq', 'w')
out_fh2 = open('out_read2.fastq', 'w')

line_num  = 0
read_out1 = ''
read_out2 = ''
result    = -1


def quality_check(string):
    
    num_high_qual = 0.
    
    quality_dic = {
        '!':33, '\"':34, '#':35, '$':36, '%':37, '&':38, '\'':39,
        '(':40, ')':41, '*':42, '+':43, ',':44, '-':45, '.':46,
        '/':47, '0':48, '1':49, '2':50, '3':51, '4':52, '5':53,
        '6':54, '7':55, '8':56, '9':57, ':':58, ';':59, '<':60,
        '=':61, '>':62, '?':63, '@':64, 'A':65, 'B':66, 'C':67,
        'D':68, 'E':69, 'F':70, 'G':71, 'H':72, 'I':73, 'J':74,
        'K':75, 'L':76, 'M':77, 'N':78, 'O':79, 'P':80, 'Q':81,
        'R':82, 'S':83, 'T':84, 'U':85, 'V':86, 'W':87, 'X':88,
        'Y':89, 'Z':90, '[':91, '\\':92, ']':93, '^':94, '_':95,
        '`':96, 'a':97, 'b':98, 'c':99, 'd':100, 'e':101, 'f':102,
        'g':103, 'h':104, 'i':105, 'j':106, 'k':107, 'l':108,
        'm':109, 'n':110, 'o':111, 'p':112, 'q':113, 'r':114,
        's':115, 't':116, 'u':117, 'v':118, 'w':119, 'x':120,
        'y':121, 'z':122, '{':123, '|':124, '}':125, '~':126,
    }
    
    string_list = list(string)
    
    for i in range(0,len(string_list)):
        if quality_dic[string_list[i]] - 33 > min_quality:
            num_high_qual += 1
    
    if num_high_qual/len(string_list) > min_percent:
        return 1
    else:
        return 0


def processing(line, read_out, line_num):

    result = -1

    if line_num%4 == 1:
        read_out += line
        return(read_out, result)
    elif line_num%4 == 2:
        read_out += line
        return(read_out, result)
    elif line_num%4 == 3:
        read_out += line
        return(read_out, result)
    else:
        read_out += line
        result = quality_check(line.strip())
        return(read_out, result)


###### Main ######

for line1 in fh1:
    line_num += 1
    (read_out1, result1) = processing(line1, read_out1, line_num)
    for line2 in fh2:
        (read_out2, result2) = processing(line2, read_out2, line_num)
        break

    if result1 == 1 and result2 == 1:
        out_fh1.write(read_out1)
        out_fh2.write(read_out2)

    if line_num%4 == 0:
        read_out1 = ''
        read_out2 = ''

fh1.close()
fh2.close()
out_fh1.flush()
out_fh2.flush()
out_fh1.close
out_fh2.close
