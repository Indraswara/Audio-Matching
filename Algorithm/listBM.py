from Algorithm.BM import *

class listBM: 
    def __init__(self, list_text: list[dict[str, str]], pattern: str): 
        self.list_text: list[dict[str, str]] = list_text
        self.pattern: str = pattern
        self.results: list[int] = self.search_in_list()

    def search_in_list(self) -> list[int]: 
        self.results: list[int] = [-1] * len(self.list_text)
        idx: int = 0
        for entry in self.list_text: 
            text = entry['text']
            bm = BM(text, self.pattern)
            result: int = bm.BMSearch()
            self.results[idx] = result
            idx += 1
        return self.results

    def result(self) -> dict[str, str]: 
        idx_ans: int = -1
        for idx, item in enumerate(self.results): 
            # print(item)
            if(item != -1): 
                idx_ans = idx
                break
        
        if(idx_ans != -1):
            return self.list_text[idx_ans]

# if __name__ == '__main__':
        
#     def show_list_matches(list_text, pattern):
#         lbm = listBM(list_text, pattern)
#         results = lbm.search_in_list()
#         for i, (entry, pos) in enumerate(zip(list_text, results)):
#             filename = entry['filename']
#             text = entry['text']
#             print(f'Filename {i+1}: {filename}')
#             print(f'Text: {text}')
#             if pos != -1:
#                 print(f'Match: {"."*pos}{pattern}')
#             else:
#                 print('No match found')
#             print()

#     list_text = [
#         {'filename': 'file1.txt', 'text': 'abacaabadcabacabaabb'},
#         {'filename': 'file2.txt', 'text': 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.'},
#         {'filename': 'file3.txt', 'text': 'Hello world, this is a test text.'},
#         {'filename': 'file4.txt', 'text': 'Another example text without the pattern.'},
#         {'filename': 'file5.txt', 'text': 'abacabacabcacabcaba'},
#         {'filename': 'file6.txt', 'text': 'lakjsdhflawehfiljdakhfaewhfabacab'}
#     ]
#     pattern = 'abacab'
#     show_list_matches(list_text, pattern)

#     # pattern = 'dolor'
#     # show_list_matches(list_text, pattern)
#     # show_list_matches(list_text, pattern + 'e')
