# -- coding: utf-8 --
def aa():
    with open('/Users/H/Documents/happy_things.txt', 'r') as f:
        txt = f.read()
        tmp = txt.split()
        dic = {}
        for i in tmp:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    return dic

ret = aa()
ret = sorted(ret.items(), key=lambda x:x[1], reverse=False)
# for i, c in ret:
#     print ('%s : %d times' %(i, c))


with open('/Users/H/Documents/happy_things.txt', 'r') as f:
    txt = f.read()
    tmp = txt.split()
    print (len(tmp))

