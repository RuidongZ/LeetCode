# -*- Encoding:UTF-8 -*-

# 347. Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        # Build Dict
        counter = collections.Counter(nums)
        '''
        import heapq
        return heapq.nlargest(k, counter, key=lambda x: counter[x])
        '''
        '''
        :return sorted(counter, key = counter.get, reverse = True)[:k]
        '''
        return [item[0] for item in counter.most_common(k)]


    '''
    # Bucket Sort
    data, res = {}, []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        bucket = [[] for i in xrange(len(nums)+1)]
        for key in data:
            bucket[data[key]].append(key)
        for i in xrange(len(bucket)-1, -1, -1):
            if bucket[i]:
                res.extend(bucket[i])
            if len(res) >= k:
                break
        return res[:k]
    '''

    '''
    # Priority Queue
    import heapq
    data, res, pq = {}, [], []
        for i in nums:
            data[i] = data[i] + 1 if i in data else 1
        for key in data:
            heapq.heappush(pq, (-data[key], key))
        for i in xrange(k):
            res.append(heapq.heappop(pq)[1])
        return res
    '''
