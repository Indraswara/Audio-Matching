from Algorithm.KMP import * 

class listKMP: 
    def __init__(self, list_text: list[dict[str, str]], pattern: str): 
        self.list_text: list[dict[str, str]] = list_text 
        self.pattern: str = pattern 
        self.results: list[(bool, int)] = self.search_in_list()

    def search_in_list(self) -> list[(bool, int)]: #(found_status, comparison_count)
        self.results: list[(bool, int)] = [(False, 0)] * len(self.list_text)
        idx: int = 0
        for entry in self.list_text: 
            text = entry['text']
            kmp = KMP(text, self.pattern)
            result: (bool, int) = [kmp.KMPSearch(), kmp.comparison_count]
            self.results[idx] = result
            idx += 1
        return self.results

    def result(self) -> (dict[str, str], int): 
        idx_ans: int = -1
        for (idx, item) in enumerate(self.results): 
            if(item[0] == True): 
                idx_ans = idx
                break
        if(idx_ans != -1): 
            return self.list_text[idx_ans], self.results[idx_ans][1]