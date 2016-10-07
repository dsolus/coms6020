#Lab5 Protein Motifs
"""This program calls a main function which creates a list of motifs and motif files.
Any previous motif files are cleared as I use append to update the files. The data is read
in from the input file line by line. The data and sequence names are stored in a list of
list called seq_list. After the list is established the function motif_count is called
which loops through the list of motifs and the seq_list calling functions to calculate 
motif count and sequence count. The function find motifs writes the data to the motif
output files."""

import os

def main():
    #Read in the motifs and append to list
    motifs_file = open("motifs.txt", 'r')
    motifs = motifs_file.readlines()
    motifs_file.close()

    #Strip '\n' character from data
    temp = []
    for element in motifs:
        clean = element.rstrip('\n')
        temp.append(clean)
    motifs = temp

    #create files for motifs
    for element in motifs:
        os.remove('motif'+element+'.txt')
        #print('old {} file cleared'.format(element))
        f = open('motif'+element+'.txt', 'a')
        #print('motif {} output file created'.format(element))
        f.close

    #Read data from large file line by line
    seq = ""
    data = ""
    seq_list = []

    with open("human_aa_chr2_partial.txt", 'r') as f:
       #for loop to find sequences in data counts number of sequences
       for line in f:
            if line.find('>') != -1:
                seq = line.rstrip('\n')
                seq_list.append(seq)
            else:
                data = data + line.rstrip('\n')
                if line.find('*') != -1:
                    seq_list.append(data)
                    data = ""
    motif_count(motifs, seq_list)

#function that loops through the motif list to get counts for each motif 
def motif_count(motifs, seq_list):
    for motif in motifs:
        #create a list of lists for sequence and data
        #loop through seq value pair and call find_motif for each value
        seq_count = 0
        motif_count = 0
        for i in range(int(len(seq_list)/2)):
            seq =  seq_list[2*i]
            value = seq_list[2*i+1]
            seq_count += find_motif(motif, value)
            motif_count += find_motifs(motif, seq, value)
        with open('motif'+motif+'.txt', 'a') as motif_file:
            motif_file.write('{} sequence count: {} \n'.format(motif, seq_count))
            motif_file.write('{} motif count: {}'.format(motif, motif_count))
        print('{} sequence count: {}'.format(motif, seq_count))
        print('{} motif count: {}'.format(motif, motif_count))

#funtion to find motif in seq and update seq count
def find_motif(motif, value):
    seq_count = 0
    if value.find(motif) != -1:
        seq_count += 1
    return seq_count

#function checks for motif in value 
def find_motifs(motif, seq, value):
    len_motif = len(motif)
    motif_count = 0
    index = 0
    j = 0
    #loop that checks for multiple occurences of the motifi
    #and inserts a space before and after the motif
    while index < len(value):
        index = value.find(motif, index + j)
        if index == -1:
            break
        value = value[:index] + ' ' + value[index:index+len_motif] + ' ' + value[index+len_motif:]
        j += 1
        #print('motif found at', index)i
        #if a motif exists update the motif count and index
        motif_count += 1
        index += len_motif
    #if there is one motif in the sequence write data to the  corresponding file
    if motif_count > 0:
        with open('motif'+motif+'.txt', 'a') as motif_file:
            motif_file.write(seq)
            motif_file.write('\n')
            motif_file.write(value)
            motif_file.write('\n')
            motif_file.write('%s %d' % ('motifs in seq:', motif_count))
            motif_file.write('\n')
    return motif_count

main()

