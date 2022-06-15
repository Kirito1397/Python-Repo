class Solution:
    def romanToInt(self, s: str) -> int:
        roman_mapping = {"I": 1, "V": 5, "X": 10,
                         "L": 50, "C": 100, "D": 500, "M": 1000}

        int_num = 0
        i = 0

        while (i < len(s)):
            r1 = roman_mapping[s[i]]
            # Provide the Integral value of Roman Integer
            if (i+1 < len(s)):
                # We utilize (i+1 < len(s)) condition so as handle 'out of index' error.
                r2 = roman_mapping[s[i+1]]
                if (r1 >= r2):
                    int_num = int_num + r1
                    i = i + 1
                else:
                    int_num = int_num - r1
                    i = i + 1
            else:
                int_num = int_num + r1
                i = i + 1
        return int_num

if __name__ == "__main__":
    prob = Solution()
    print(prob.romanToInt('MCMXCIV'))


# TEST:
# --------
# Input: s = "III"
# Output: 3
# Explanation: III = 3
