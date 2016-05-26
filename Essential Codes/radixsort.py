#================================================
# Código feito pelo usuario nlguillemot no github
#
#
# Funciona apenas com lista de strings sem numero
# P.S.: Se tiver acentos nos nomes, tirar
#================================================
def MSD_radix_string_sort(L, i):

    # base case (list must already be sorted)
    if len(L) <= 1:
        return L

    # divide (first by length, then by lexicographical order of the first character)
    done_bucket = []
    buckets = [ [] for x in range(27) ] # one for each letter in a-z

    for s in L:
        if i >= len(s):
            done_bucket.append(s)
        else:
            buckets[ ord(s[i]) - ord('a') ].append(s)

    # conquer (recursively sort buckets)
    buckets = [ MSD_radix_string_sort(b, i + 1) for b in buckets ]

    # marry (chain all buckets together)
    return done_bucket + [ b for blist in buckets for b in blist ]


#======================
#    teste
#=======================

lst = ['JackSpartt','asd','da', 'dsa','dsa', 'aaa']
print lst
lst = MSD_radix_string_sort(lst,0)
print lst
