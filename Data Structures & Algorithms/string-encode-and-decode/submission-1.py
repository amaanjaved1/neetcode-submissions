class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for elem in strs:
            encoded_string += str(len(elem)) + "#" + elem

        return encoded_string

    def decode(self, s: str) -> List[str]:
        if (len(s) == 0):
            return []

        decoded_string = []
        i = 0

        while i < len(s):
            j = i
            while (s[j] != "#"):
                j += 1
            str_length = int(s[i:j])
            decoded_string.append(s[j + 1 : j + 1 + str_length])
            i = j + 1 + str_length

        return decoded_string
