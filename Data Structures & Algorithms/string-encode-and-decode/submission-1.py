class Solution:

    def encode(self, strs: List[str]) -> str:
        phrase = ""
        num=0
        for word in strs:
            phrase = phrase +str(len(word)) +"#"+ word
            num+=1
        print(phrase)
        return phrase 

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        i=0
        while i<len(s):
            #finding the identifier hashtag between words by 
            #search for the # after the index i
            j=s.find("#", i)
            #finding the length of the word 
            length=int(s[i:j])
            #updating the marker i to the start of the word 
            i=j+1
            #finding the word by finding the substring from i 
            # and adding the word length to find the end of the word
            word=s[i:i+length]
            #adding the word to the decoded array   
            decoded.append(word)
            #updating the starting marker after this word in string
            i+=length
        return decoded

