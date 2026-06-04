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
            j=s.find("#", i)
            length=int(s[i:j])

            i=j+1

            word=s[i:i+length]
            decoded.append(word)

            i+=length
        return decoded

