# counting bobs
#s = 'bob be bob and not robert, just bob'
#s = 'fbobfabbobbbobbbobobxbuu'
#s = 'ydboobebobbloboobbobbobhbobobobobo'
s = 'boboobvboboobobbooboocboobdpnbobobbobbvr'
string = s
bob = 'bob'
count = 0
for i in range(len(string)):
    if string[i:i+3] == bob:
        count += 1
print('Number of times ' + bob + ' occurs is: ' + str(count))
