class KMP:
    def __init__(self, pattern: str, text: str):
        self.pattern: str = pattern
        self.text: str = text
        self.lps: list[int] = self.GenerateLPS()

    def KMPSearch(self) -> bool:
        patternSize: int = len(pattern)
        textSize: int  = len(text)

        i: int = 0 
        j: int = 0

        while(i < textSize):
            if(self.pattern[j] == self.text[i]):
                j += 1
                i += 1

            if j == patternSize: 
                return True

            # if mismatch occur 
            elif i < textSize and self.pattern[j] != self.text[i]:
                if j != 0: 
                    j = self.lps[j-1]
                else: 
                    i += 1

        return False

    def GenerateLPS(self) -> list[int]:
        size: int = len(self.pattern)
        self.lps = [0] * size
        i = 0
        for j in range(1, size):
            while(i > 0 and self.lps[i] != self.lps[j]):
                i = self.lps[i - 1]
            if self.pattern[i] == self.pattern[j]:
                i += 1
            self.lps[j] = i

        return self.lps


pattern = "ABABCABAB"
text = "ABABDABACDABABCABAB"
kmp = KMP(pattern, text)
result = kmp.KMPSearch()
print("Pattern found:", result)