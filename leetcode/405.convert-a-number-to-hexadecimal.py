#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.78%)
# Total Accepted:    45.4K
# Total Submissions: 108.7K
# Testcase Example:  '26'
#
# 
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
# 
# 
# Note:
# 
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
# 
# 
# 
# Example 1:
# 
# Input:
# 26
# 
# Output:
# "1a"
# 
# 
# 
# Example 2:
# 
# Input:
# -1
# 
# Output:
# "ffffffff"
# 
# 
#
class Solution:
    def toHex(self, num: int) -> str:
        mp = '0123456789abcdef'
        if num == 0:
            return '0'
        if num < 0:
            num = 2**32 + num
        ret = ''
        while num != 0:
            index = num & 0xf
            ret = mp[index] + ret
            num = num >> 4
        return ret

