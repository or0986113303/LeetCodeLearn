# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:03:27 2020

@author: User
"""


def partition(nums, begin, end):
	pivot = begin
	for i in range(begin+1, end+1):
		if nums[i] <= nums[begin]:
			pivot += 1
			nums[i], nums[pivot] = nums[pivot], nums[i]
	nums[pivot], nums[begin] = nums[begin], nums[pivot]
	return pivot

def quickSort(nums, begin=0, end=0):
	if begin >= end:
		return
	p = partition(nums, begin, end)
	quickSort(nums, begin, p-1)
	quickSort(nums, p+1, end)

def sortArray(nums):
	quickSort(nums, begin=0, end=len(nums)-1)
	return nums

if __name__ == '__main__':
    source = [1,5,6,7,8,9,23,6,10,19]
    result = sortArray(nums= source)
    print(result)