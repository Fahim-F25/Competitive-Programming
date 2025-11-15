# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2):
        
        list1.extend(list2)
        list1.sort()
        
        return list1
    
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

print(Solution().mergeTwoLists(l1,l2))