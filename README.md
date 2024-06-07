# Turing_Tests
 2 scripts for Turiing Python Tests. Stairway to the Top & Word weight

## Word Weight Problem
A character's corresponding integer is equal to the position of the character in the alphabet. given a word s and an integer n, you need to apply the following steps in the given order and return the resulting integer.
    1. Replace the characters in the word s with their corresponding integers. Pass the resulting integer to the next step.
    2. sum up the digits of the integer. repeat the steps n times.

Example:
Input: s = "turing", n = 2
Output: 8
Explanation:
    - "turing" -> "(20)(21)(18)(9)(14)(7)" ->"2021189147" ->2021189147
    - n=1: 2021189147 -> 2+0+2+1+1+8+9+1+4+7  -> 35
    - n=2: 35 -> 3+5 ->8

Constraints:
    - 1<=s.length <=100
    - 1<=k<=10
    - s consists of lowercase English letters

## Stairway to the Top

A group of hikers need to make it to the top of a mountain. They can only move forward by either hopping over one rock or two rocks at a time. How many different ways can they reach the summit of the mountain, given that there are 'n rocks to hop over?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to reach the summit of the mountain.

 Hopping over one rock, then one more rock
 Hopping over two rocks at once

Example 2:

Input: n = 3
Output: 3

Explanation: There are three ways to reach the summit of the mountain.

Constraints:
1<= n <=40