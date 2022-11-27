class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        for word in words:
            aux = 0
            for char in word:
                #print(word.count(char))
                #print(char.count(char))
                if word.count(char)>chars.count(char):
                    break
                else:
                    aux += 1
            if aux == len(word):
                sum += aux
                
        return sum
        