
# Day - 15 Solutions

# Defanging an ip address
def defange(strg):
    return strg.replace('.','[.]')
print(defange("1.1.1.1"))

# Shuffle string
def shuffle(strg,arr):
    rep = ''
    for i in arr:
        rep+=strg[i]
    return rep
print(shuffle("codeleet",[4,5,6,7,0,2,1,3]))

# Goal Parser Interpretation 
def strg(val):
    return val.replace('()','o').replace('(al)','al')
print(strg("G()(al)"))

# Count Items Matching a Rule 
def count_items(items,ruleKey,ruleValue):
    idx = {'type':0, 'color':1, 'name':2}[ruleKey]
    count = 0
    for item in items:
        if  item[idx]==ruleValue:
            count+=1
    return count
print(count_items([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color", "silver"))

# Sorting sentence
def sen_sor(strg):
    words = strg.split()
    res = [""]*len(words)
    for word in words:
        pos = int(word[-1])
        res[pos-1] = word[:-1]
    return " ".join(res)

print(sen_sor("is2 sentence4 This1 a3"))

# Check if Two String Arrays are Equivalent 
def if_check(str1,str2):
    return ''.join(str1)==''.join(str2)
print(if_check(["ab", "c"],["a", "bc"]))

# To Lower Case
def lower_of(str1):
    return str1.lower()
print(lower_of("LOVELY"))
