s = 'azcbobobegghakl'
sstr = s   # input search string
astr = ''  # longest alphabetical string
nstr = ''  # new alpha str
isBstr = False # break of alpha str
nstr = sstr[0]
#for i, _ in enumerate(sstr): 
for i in range(1,len(sstr)):
    #print('i: ' + str(i))
    if sstr[i] >= sstr[i-1]:
        nstr += sstr[i]  # add char existing str
        isBstr = False
    else:   # break in length of nstr
        #print('break - sstr[i]: ' + str(sstr[i]) + ' nstr is: ' + str(nstr) + ' astr is: ' + str(nstr))
        if not isBstr and len(nstr) > len(astr):  # if new aplhs str longer than existing alpha str 
            astr = nstr  # new aplha str is longest alpa str
        nstr = sstr[i]  # begin new str
        isBstr = True
if len(nstr) > len(astr):  # if new aplhs str longer than existing alpha str 
    astr = nstr  # new aplha str is longest alpa str
print('Longest substring in alphabetical order is: ' + str(astr))
#print('nstr is: ' + str(nstr))
