class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict = defaultdict(list) # key = tuple of frequency per character, value = index in strs

        for string_index, string in enumerate(strs):
            string_list = [0] * 26

            for char_index, char in enumerate(string):
                order = ord(char) - ord("a")
                string_list[order] += 1
                
            result_dict[tuple(string_list)].append(string)
        
        return list(result_dict.values())