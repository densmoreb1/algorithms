def lengthOfLongestSubstring(s):
    #    longest = 0
    #    seen = set()
    #
    #    i, j = 0, 0
    #    while i <= len(s):
    #        print(s[i], s[j])
    #        if s[j] in seen:
    #            longest = max(longest, j)
    #            i = j
    #        else:
    #            seen.add(s[j])
    #        j += 1
    #
    #    return longest

    seen = set()
    longest = 0

    left = 0
    right = 0

    while right < len(s):

        if s[right] not in seen:
            # adds new characters
            seen.add(s[right])
            right += 1
        else:
            # removes seen characters
            seen.remove(s[left])
            left += 1

        # right - left gives the space between each letter
        longest = max(longest, right - left)


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
