class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        freq = {}
        most_freq = 0

        for r in range(len(s)):
            #add s[r] into freq
            freq[s[r]] = freq.get(s[r],0) + 1
            most_freq = max(most_freq, freq[s[r]])

            #whlie r - l - most_freq > k take out s[l] from freq, and refind most_freq
            if r - l + 1 - most_freq > k:
                freq[s[l]] -= 1
                l += 1

            #update max_height

            max_length = max(max_length,r-l+1) #look at calc
        
        return max_length
