def longestSubstring(s: str) -> int:
    if s:
        result = {}
        ans = 0
        i, initial = 0, 0
        while(i<len(s)):
            if s[i] in result:
                ans = max(ans, i-initial)
                initial = result[s[i]]+1
            result[s[i]] = i
            i += 1
        ans = max(ans, i - initial)
        return ans
    return 0

def lengthOfLongestSubstring(s: str) -> int:
    if s:
        last_idx = {}
        max_len = 0

        # starting index of current
        # window to calculate max_len
        start_idx = 0

        for i in range(0, len(s)):

            # Find the last index of str[i]
            # Update start_idx (starting index of current window)
            # as maximum of current value of start_idx and last
            # index plus 1
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)

            # Update result if we get a larger window
            max_len = max(max_len, i - start_idx + 1)

            # Update last index of current char.
            last_idx[s[i]] = i

        return max_len

    return 0


print(lengthOfLongestSubstring("abba"))

