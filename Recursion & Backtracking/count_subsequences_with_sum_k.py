class Solution:
    def count_subsequences_with_sum_k(self, i, arr, k, n, sum=0, l=0, r=0):
        """
        This function calculates the number of subsequences of the given array
        `arr` with sum equal to `k`.

        Args:
        i (int): The current index of the array being considered
        arr (list): The input array
        k (int): The target sum
        n (int): The length of the input array
        sum (int): The current sum of the subsequence being considered
        l (int): The result of the left branch of the recursion
        r (int): The result of the right branch of the recursion

        Returns:
        The number of subsequences with sum equal to `k`.
        """
        # BASE CASE
        if i == n:
            # Condition satisfied
            if sum == k: 
                return 1
            # Condition not satisfied
            return 0

        # PICK CASE
        # Add the current element to the current sum and recursively call the
        # function on the next element in the array with the updated sum
        sum += arr[i]
        l = self.count_subsequences_with_sum_k(i+1, arr, k, n, sum)
        # Undo the addition to the sum to consider the "not pick" case
        sum -= arr[i]

        # NOT PICK CASE
        # Recursively call the function on the next element in the array with
        # the same sum
        r = self.count_subsequences_with_sum_k(i+1, arr, k, n, sum)

        # Return the sum of the results from the pick and not pick cases
        return l+r

ob = Solution()
arr = [1, 3, 2, 2, 5, 2, 3, 7]
k = 7
print(ob.count_subsequences_with_sum_k(0, arr, k, len(arr)))  # Prints 12




# SHORT WAY
# The function recursively considers two cases for each element in the array: the case where the element is included in the subsequence, and the case where it is excluded.
# i.e. PICK & NOT PICK
# The base case is reached when we have considered all elements in the array. 
# If the sum of the subsequence is equal to the desired sum k, we return 1 to indicate that a valid subsequence has been found. 
# If the sum is not equal to k, we return 0 to indicate that no valid subsequence has been found. 
# The final result is the sum of the number of valid subsequences that include the current element and the number of valid subsequences that don't.

class Solution:
    def count_subsequences_with_sum_k(self, i, arr, k, n, sum=0):
        if i == n:
            if sum == k:
                return 1
            return 0

        # Recursively count the number of subsequences that include the current element and the number that don't.
        return (
                self.count_subsequences_with_sum_k(i + 1, arr, k, n, sum + arr[i]) +
                self.count_subsequences_with_sum_k(i + 1, arr, k, n, sum)
        )

ob = Solution()
arr = [1, 3, 2, 2, 5, 2, 3, 7]
k = 7
print(ob.count_subsequences_with_sum_k(0, arr, k, len(arr)))  # Prints 12

