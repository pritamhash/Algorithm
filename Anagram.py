def anagram(ar1,ar2):
    ar1 = ar1.replace(' ', '')
    ar2 = ar2.replace(' ', '')

    return sorted(ar1) == sorted(ar2)


print(anagram('god', 'dogg'))


def anagram1(ar1,ar2):
    ar1 = ar1.replace(' ', '')
    ar2 = ar2.replace(' ', '')

    #Edge Case Check
    if len(ar1)!=len(ar2):
        return False

    k = {}
    for letter in ar1:
        if letter in k:
            k[letter]+=1
        else:
            k[letter]=1

    for letter in ar2:
         if letter in k:
             k[letter]-=1
         else:
             k[letter]=1

    for i in k:
        if k[i]!=0:
            return False
        else:
            return True

print(anagram1('dogs', 'gods'))