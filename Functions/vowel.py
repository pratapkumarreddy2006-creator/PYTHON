def vowel(s):
    vow = "aeiouAEIOU"
    count = 0
    n = len(s)
    for i in s:
        if i in vow:
            count += 1
    
    return count

print(vowel("Deba"))