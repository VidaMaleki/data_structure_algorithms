"""621. Task Scheduler
Medium
Topics
Companies
Hint
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100"""


from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())  # Maximum task frequency
        max_count = sum(1 for task in task_counts if task_counts[task] == max_freq)  # Tasks with max frequency
        
        # Compute minimum intervals
        min_intervals = (max_freq - 1) * (n + 1) + max_count
        
        return max(len(tasks), min_intervals)

# Example Test Cases
solution = Solution()
print(solution.leastInterval(["A","A","A","B","B","B"], 2))  # Output: 8
print(solution.leastInterval(["A","C","A","B","D","B"], 1))  # Output: 6
print(solution.leastInterval(["A","A","A", "B","B","B"], 3))  # Output: 10


"""
Explanation:
For tasks = ["A","A","A","B","B","B"], n = 2:

Task frequency: {A: 3, B: 3}
Maximum frequency (max_freq) = 3
Number of tasks with max_freq (max_count) = 2
Formula calculation:
(3−1)×(2+1)+2=8
✅ Output: 8

Complexity Analysis:
Building frequency counter: O(N)
Finding max frequency: O(26) (constant)
Final computation: O(1)
Overall Complexity: O(N)
"""