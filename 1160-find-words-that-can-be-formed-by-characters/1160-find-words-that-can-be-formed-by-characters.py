class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        for word in words:
            aux = True
            for char in word:
                if word.count(char)>chars.count(char):
                    aux = False
                    break
                else:
                    aux += 1
            
            if aux:
                sum += len(word)
                
        return sum
        