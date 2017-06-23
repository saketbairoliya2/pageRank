from operator import itemgetter
import re

class UserInput:
    '''
    Used for taking user Input. Currently get_user_input reads value from command line, and can be stopped by entering "-1".
    P Bangalore Mumbai -> format for page tag entry
    Q Bangalore -> format for Query tag entry
    '''
    def __init__(self):
        self.user_input = {'pages_keywords': [], 'queries_keywords': []}
        self.INPUT_SEPERATOR = " "
        self.PAGE = "P"
        self.QUERY = "Q"

    def get_user_input(self):
        input_str = ''
        while (input_str != '-1'):
            input_str = self._read_input_from_cmd()
            self._convert_input_to_array_of_string(input_str)
            
        return self.user_input
            
    def _convert_input_to_array_of_string(self, input_str):
        word_list = re.sub("[^\w]", self.INPUT_SEPERATOR, input_str).split()
        
        if word_list[0].upper() == self.PAGE:
            self.user_input['pages_keywords'].append(word_list[1:])
        elif word_list[0].upper() == self.QUERY:
            self.user_input['queries_keywords'].append(word_list[1:])
        elif (word_list[0] == "1"):
            # Do nothing
            pass
        else:
            print ("Please enter value in either of the format:\n P <tag_name> <another_tag>\n      OR \n Q <tag_name> ")
    
    def _read_input_from_cmd(self):
        val = input('Enter -1 to exit OR check the result. \n')
        return val
        
class Search:
    '''
    Finds the page rank for each query.
    Steps: 
    1. Takes user input for pages and queries keywords.
    2. loop over each queries tags and find the weight with tags in each page, sum them.
    3. Loop for all the queries.
    4. Make heap/dict of the ranking to have both index and weightage.
    5. Sort in decreading order, based on weightage.
    6. return keys in list.
    7. use _output_format to format returned rank, as asked in assignment
    '''

    def __init__(self, user_input={'pages_keywords': [], 'queries_keywords': []}):
        self.pages_keywords = user_input['pages_keywords']
        self.queries_keywords = user_input['queries_keywords']
        self.MAX_KEYWORDS_ALLOWED = 8
        self.MAX_RELEVANT_PAGES_FOR_A_QUERY = 5
        
    def page_rank(self):
        for query_no in range(len(self.queries_keywords)):
            print(self._output_format(query_no + 1, self._rank_pages_for_a_query(query_no)))
        
    # All function onwards are private, accessible only for class members.
    def _output_format(self, query_number, ranks):
        output_str = "Q" + str(query_number) + ": "
        for rank in ranks:
            output_str += "P" + str(rank + 1) + " "
        return output_str
        
    def _rank_pages_for_a_query(self, query_no):
        search_strength_of_pages = self._search_strength_of_all_pages_for_query(query_no)
        search_strength_of_page_in_hash = self._convert_array_to_hash(search_strength_of_pages)
        sorted_page_ranks = self._sort_hash_by_page_rank_dec(search_strength_of_page_in_hash)
        
        ranking = [item[0] for item in sorted_page_ranks if item[1] != 0]
        return ranking[:self.MAX_RELEVANT_PAGES_FOR_A_QUERY]
            
    def _sort_hash_by_page_rank_dec(self, hash_map):
        sorted_x = sorted(hash_map.items(), key=itemgetter(1), reverse=True)
        return sorted_x
        
    def _convert_array_to_hash(self, page_rank_array):
        page_rank = {}
        for i in range(len(page_rank_array)):
            page_rank[i] = page_rank_array[i]
        return page_rank
        
    def _search_strength_of_all_pages_for_query(self, query_no):
        search_strengths = []
        for page_no in range(len(self.pages_keywords)):
            search_strengths.append(self._search_strength_of_a_page_for_query(query_no, page_no))
        return search_strengths
        
    def _search_strength_of_a_page_for_query(self, query_no, page_no):
        max_strength = self.MAX_KEYWORDS_ALLOWED
        search_strength = 0
        for each_query in self.queries_keywords[query_no]:
            search_strength += max_strength * self._weight_of_a_query_keyword_in_a_page(each_query, page_no)
            max_strength -= 1
        return search_strength
    
    def _weight_of_a_query_keyword_in_a_page(self, query_keyword, page_no):
        if query_keyword in self.pages_keywords[page_no]:
            return int(8 - self.pages_keywords[page_no].index(query_keyword))
        else:
            return 0
   
# Program Starts here.

if __name__ == "__main__":
    user_input = UserInput().get_user_input()
    s = Search(user_input)
    s.page_rank()
    
    