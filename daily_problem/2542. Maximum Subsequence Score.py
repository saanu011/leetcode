class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [(nums1[i], nums2[i]) for i in range(len(nums1))]
        print(pairs)
        pairs.sort(key=lambda x: -x[1])
        print(pairs)

        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        answer = top_k_sum*pairs[k-1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])

            answer = max(answer, top_k_sum*pairs[i][1])
        return answer
        