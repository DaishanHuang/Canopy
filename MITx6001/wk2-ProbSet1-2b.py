# counting bobs
# s = 'bob be bob and not robert, just bob'

s = 'fbobfabbobbbobbbobobxbuu'
     #bob   bob bob bobob 
# fails on overlapping bobs
string = s
str2 = 'bob'
count = string.count(str2)
print('Number of times bob occurs is: ' + str(count))