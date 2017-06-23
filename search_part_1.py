from operator import itemgetter
import re

class UserInput:
    def __init__(self):
        self.user_input = {'pages_keywords': [], 'queries_keywords': []}
        self.INPUT_SEPERATOR = " "
        self.PAGE = "P"
        self.QUERY = "Q"

    def get_user_input(self):
        input_str = ''
        while (input_str != '-1'):
            input_str = input('Enter -1 to exit the program\n')
            self.convert_input_to_array_of_string(input_str)
            
        return self.user_input
            
    def convert_input_to_array_of_string(self, input_str):
        word_list = re.sub("[^\w]", self.INPUT_SEPERATOR, input_str).split()
        
        if word_list[0].upper() == self.PAGE:
            self.user_input['pages_keywords'].append(word_list[1:])
        elif word_list[0].upper() == self.QUERY:
            self.user_input['queries_keywords'].append(word_list[1:])
    
    def read_input_from_cmd(self):
        val = input('Enter -1 to exit\n')
        return val
        
class Solution:
    def __init__(self, user_input):
        self.pages_keywords = user_input['pages_keywords']
        self.queries_keywords = user_input['queries_keywords']
        self.MAX_KEYWORDS_ALLOWED = 8
        self.MAX_RELEVANT_PAGES_FOR_A_QUERY = 5
        
    def solution(self):
        for i in range(len(self.queries_keywords)):
            print(self.output_format(i + 1, self.rank_pages_for_a_query(i)))
            
    def output_format(self, query_number, rank_array):
        output_str = "Q" + str(query_number) + ": "
        for each in rank_array:
            output_str += "P" + str(each) + " "
        return output_str
        
    def rank_pages_for_a_query(self, query_no):
        search_strength_of_pages = self.search_strength_of_all_pages_for_query(query_no)
        search_strength_of_page_in_hash = self.convert_array_to_hash(search_strength_of_pages)
        sorted_page_ranks = self.sort_hash_by_page_rank_dec(search_strength_of_page_in_hash)
        
        ranking = [item[0] for item in sorted_page_ranks if item[1] != 0]
        return ranking[:self.MAX_RELEVANT_PAGES_FOR_A_QUERY]
            
    def sort_hash_by_page_rank_dec(self, hash_map):
        sorted_x = sorted(hash_map.items(), key=itemgetter(1))
        return sorted_x
        
    def convert_array_to_hash(self, page_rank_array):
        page_rank = {}
        for i in range(len(page_rank_array)):
            page_rank[i] = page_rank_array[i]
        return page_rank
        
    def search_strength_of_all_pages_for_query(self, query_no):
        search_strength = []
        for page_no in range(len(self.pages_keywords)):
            search_strength.append(self.search_strength_of_a_page_for_query(query_no, page_no))
        return search_strength
        
    def search_strength_of_a_page_for_query(self, query_no, page_no):
        max_strength = self.MAX_KEYWORDS_ALLOWED
        search_strength = 0
        for each_query in self.queries_keywords[query_no]:
            search_strength += max_strength * self.weight_of_a_query_keyword_in_a_page(each_query, page_no)
            max_strength -= 1
        return search_strength
    
    def weight_of_a_query_keyword_in_a_page(self, query_keyword, page_no):
        if query_keyword in self.pages_keywords[page_no]:
            return int(8 - self.pages_keywords[page_no].index(query_keyword))
        else:
            return 0
            
if __name__ == "__main__":
    user_input = UserInput().get_user_input()
    s = Solution(user_input)
    s.solution()
    
    