class Bruteforce: 
    def __init__(self, pattern: str, text: str): 
        self.pattern = pattern
        self.text = text 
    def BruteforceSearch(self) -> (bool, int): 
        textLength: int = len(self.text)
        patternLength: int = len(self.pattern)
        comparison_count: int = 0
        for i in range(textLength - patternLength + 1):
            j = 0 
            while j < patternLength and self.text[i + j] == self.pattern[j]:
                j += 1
                comparison_count += 1
            if j == patternLength: 
                return (True, comparison_count)
        
        return (False, comparison_count)

# test = Bruteforce("ABABCABAB", "ABABDABACDABABCABAB")
# print(test.BruteforceSearch())