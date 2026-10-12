class Solution:
    def longestSubarray(self, arr, k):
        left = 0
        total = 0
        max_length = 0

        for right in range(len(arr)):
            # Add the current element to the sum
            total += arr[right]

            # Remove elements from the left if the sum exceeds k
            while total > k and left <= right:
                total -= arr[left]
                left += 1

            # Check if the current subarray has sum k
            if total == k:
                length = right - left + 1
                max_length = max(max_length, length)

        return max_length



      #Changes from minimum subarray sum
      #while total >= target --> while total > k
      #min_length = min(min_length, length) --> max_length = max(max_length, length)
      
