"""2365. Task Scheduler II
Medium
Topics
Companies
Hint
You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

Each day, until all tasks have been completed, you must either:

Complete the next task from tasks, or
Take a break.
Return the minimum number of days needed to complete all tasks.

 

Example 1:

Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9
Explanation:
One way to complete all tasks in 9 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
Day 7: Take a break.
Day 8: Complete the 4th task.
Day 9: Complete the 5th task.
It can be shown that the tasks cannot be completed in less than 9 days.
Example 2:

Input: tasks = [5,8,8,5], space = 2
Output: 6
Explanation:
One way to complete all tasks in 6 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
It can be shown that the tasks cannot be completed in less than 6 days.
 

Constraints:

1 <= tasks.length <= 105
1 <= tasks[i] <= 109
1 <= space <= tasks.length"""

from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_done = {}  # Stores the last day a task was executed
        day = 0  # Start counting days
        
        for task in tasks:
            day += 1  # Always move to the next day
            
            if task in last_done:
                min_next_day = last_done[task] + space + 1
                if day < min_next_day:
                    day = min_next_day  # Skip days to satisfy space requirement
            
            last_done[task] = day  # Update the last execution day
        
        return day  # Total days taken

# Example Test Cases
solution = Solution()
print(solution.taskSchedulerII([1,2,1,2,3,1], 3))  # Output: 9
print(solution.taskSchedulerII([5,8,8,5], 2))  # Output: 6

"""
Explanation:
For tasks = [1,2,1,2,3,1], space = 3:

Day	 Task	Action	Last Done
1	  1	    Execute	{1: 1}
2	  2	    Execute	{1: 1, 2: 2}
3	  -	    Skip	{1: 1, 2: 2}
4	  -	    Skip	{1: 1, 2: 2}
5	  1	    Execute	{1: 5, 2: 2}
6	  2	    Execute	{1: 5, 2: 6}
7	  -	    Skip	{1: 5, 2: 6}
8	  3	    Execute	{1: 5, 2: 6, 3: 8}
9	  1	    Execute	{1: 9, 2: 6, 3: 8}
Final answer = 9 days.

Time Complexity:
O(N) → We iterate through tasks once, updating a dictionary.
Space Complexity: 
O(U) where U is the number of unique task types."""