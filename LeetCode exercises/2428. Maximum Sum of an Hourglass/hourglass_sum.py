class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xors = [0] * len(arr)
        result_xors = []
        #Prefix XORS
        for index,element_array in enumerate(arr):
            if index == 0:
                prefix_xors[index] ^= element_array
            else:
                prefix_xors[index] = prefix_xors[index - 1] ^ element_array

        #Get result of xors
        for left,right in queries:
            if left == 0:
                result_xors.append(prefix_xors[right])
            else:
                result_xors.append(prefix_xors[right] ^ prefix_xors[left-1])

        return result_xors
