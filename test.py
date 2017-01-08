import editdistance

dict = {0: 'human', 1: 'chimp', 2: 'asiatic toad', 3: 'black titi', 4: 'saki', 5: 'lemur', 6: 'mouse', 7: 'snub-nosed monkey'}
dict2 = {}

with open('sequences/homosapien_mtDNA.fasta', 'r') as myfile:
    dict2['human']=myfile.read().replace('\n', '')

with open('sequences/pantroglodytes_mtDNA.fasta', 'r') as myfile:
    dict2['chimp']=myfile.read().replace('\n', '')

with open('sequences/bufo_gargarizans_mtDNA.fasta', 'r') as myfile:
    dict2['asiatic toad']=myfile.read().replace('\n', '')

with open('sequences/callicebus_lugens_mtDNA.fasta', 'r') as myfile:
    dict2['black titi']=myfile.read().replace('\n', '')

with open('sequences/chiropotes_israelita_mtDNA.fasta', 'r') as myfile:
    dict2['saki']=myfile.read().replace('\n', '')

with open('sequences/lemurcatta_mtDNA.fasta', 'r') as myfile:
    dict2['lemur']=myfile.read().replace('\n', '')

with open('sequences/musmusculus_mtDNA.fasta', 'r') as myfile:
    dict2['mouse']=myfile.read().replace('\n', '')

with open('sequences/rhinopithecus_bieti_mtDNA.fasta', 'r') as myfile:
    dict2['snub-nosed monkey']=myfile.read().replace('\n', '')

for i in range(0, len(dict2)):
    for j in range(i+1, len(dict2)):
        print dict[i] + " : " + dict[j]
        print editdistance.eval(dict2[dict[i]], dict2[dict[j]])
