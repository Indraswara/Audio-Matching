class BM: 
    def __init__(self, text: str, pattern: str): 
        self.text: str = text
        self.pattern: str = pattern
        self.occurences: dict = self.lastOccurences()

    def lastOccurences(self) -> dict: 
        occurences = dict()
        for letter in set(self.pattern):
            occurences[letter] = self.pattern.rfind(letter)
        return occurences

    def BMSearch(self) -> int: 
        # find occurence of pattern in text
        patternSize: int = len(self.pattern)
        textSize: int = len(self.text)

        i = patternSize - 1  # text index
        j = patternSize - 1  # pattern index

        while i < textSize:
            if self.text[i] == self.pattern[j]:
                if j == 0: 
                    return i  # Return the start index of the match
                else: 
                    j -= 1
                    i -= 1
            else:
                l = self.occurences.get(self.text[i], -1)
                i = i + patternSize - min(j, l + 1)
                j = patternSize - 1
        return -1

if __name__ == '__main__':
        
    def show_match(text, pattern):
        print ('Text:  %s' % text)
        p = BM(text, pattern).BMSearch()
        if p != -1:
            print('Match: %s%s' % ('.'*p, pattern))
        else:
            print('No match found')

    text = 'abacaabadcabacabaabb'
    pattern = 'abacab'
    show_match(text, pattern)

    text = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'
    pattern = 'dolor'
    show_match(text, pattern)
    show_match(text, pattern + 'e')
