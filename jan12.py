#1704. Determine if String Halves Are Alike

#You are given a string s of even length. 
#Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
#Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). 
#Notice that s contains uppercase and lowercase letters.
#Return true if a and b are alike. Otherwise, return false.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2

        a=s[0:n]
        b=s[n:len(s)]

        suma=0
        sumb=0
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

        for i in a:
            if i in vowels:
                suma+=1
        for j in b:
            if j in vowels:
                sumb+=1

        if suma==sumb:
            return True
        else:
            return False
