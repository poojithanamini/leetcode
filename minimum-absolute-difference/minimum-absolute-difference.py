class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # Sort the array.
        arr.sort()
        # Calculate the minimum so far.
        minimum = arr[1] - arr[0]
        
        # Array to store the result.
        result = []
        
        # For each adjacent pairs.
        for i in range(len(arr) - 1):
            # Calculate the difference.
            diff = arr[i+1] - arr[i]
            
            # If we found a new minimum.
            if diff < minimum:
                # Clear the result.
                result.clear()
                # Store the new minimum.
                minimum = diff
                # Add pair to the result.
                result.append([arr[i], arr[i+1]])
            # If the pair matches the minimum.
            elif diff == minimum:
                result.append([arr[i], arr[i+1]])

        # Return.
        return result