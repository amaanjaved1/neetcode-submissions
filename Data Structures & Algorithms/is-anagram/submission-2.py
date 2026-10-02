class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        # build s_dict
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        
        # build t_dict
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        
        # Compare dictionaries
        if (len(s_dict) != len(t_dict)):
            return False
        else:
            for key in s_dict:
                if key not in t_dict:
                    return False
                else:
                    if (s_dict[key] != t_dict[key]):
                        return False
        
        return True