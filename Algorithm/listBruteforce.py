from Algorithm.Bruteforce import * 

class listBruteforce: 
    def __init__(self, list_text, pattern): 
        self.list_text = list_text
        self.pattern = pattern
        self.results: list[(bool, int)] = self.search_in_list()
    
    def search_in_list(self) -> list[(bool, int)]: 
        self.results: list[bool] = [(False, 0)] * len(self.list_text)
        idx: int = 0 
        for entry in self.list_text: 
            text = entry['text']
            bruteforce = Bruteforce(text, self.pattern)
            result: bool = bruteforce.BruteforceSearch()
            self.results[idx] = result 
            idx += 1 
        return self.results

    def result(self) -> dict[str, str]: 
        idx_ans: int = -1 
        for idx, item in enumerate(self.results): 
            if(item[0] != False):
                idx_ans = idx
                break

        if(idx_ans != -1): 
            # return self.list_text[idx_ans]
            return (self.list_text[idx_ans], self.results[idx_ans][1])