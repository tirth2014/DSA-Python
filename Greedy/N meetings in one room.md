# [N meetings in one room](https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1)

## Problem Description

<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">There is <strong>one</strong> meeting room in a firm. There are <strong>N</strong> meetings in the form of <strong>(start[i], end[i])</strong> where <strong>start[i]&nbsp;</strong>is start time of meeting <strong>i </strong>and <strong>end[i] </strong>is finish time of meeting <strong>i.</strong><br>
What is the <strong>maximum</strong> number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? </span></p>

<p><span style="font-size:18px"><strong>Note:</strong>&nbsp;Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.</span></p>

<p><br>
<span style="font-size:18px"><strong>Example 1:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
</strong>N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
<strong>Output: </strong>
4<strong>
Explanation:
</strong>Maximum four meetings can be held with
given start and end timings.</span>
<span style="font-size:18px">The meetings are - (1, 2),(3, 4), (5,7) and (8,9)</span>
</pre>

<p><span style="font-size:18px"><strong>Example 2:</strong></span></p>

<pre><span style="font-size:18px"><strong>Input:
N</strong> = 3
<strong>start[]</strong> = {10, 12, 20}
<strong>end[]</strong> = {20, 25, 30}
<strong>Output: </strong>
1<strong>
Explanation:
</strong>Only one&nbsp;meetings can be held
with given start and end timings.</span></pre>

<p><br>
<span style="font-size:18px"><strong>Your Task</strong>&nbsp;:<br>
You don't need to read inputs or print anything. Complete the function <strong>maxMeetings()</strong><em>&nbsp;</em>that takes two&nbsp;arrays <strong>start[] </strong>and <strong>end[] </strong>along with their size <strong>N</strong> as input parameters and returns the <strong>maximum</strong> number of meetings that can be held in the meeting room.</span></p>

<p><br>
<span style="font-size:18px"><strong>Expected Time Complexity </strong>: O(N*LogN)</span><br>
<span style="font-size:18px"><strong>Expected Auxilliary Space</strong> : O(N)</span></p>

<p><br>
<span style="font-size:18px"><strong>Constraints:</strong></span><br>
<span style="font-size:18px">1 ≤ N&nbsp;≤ 10<sup>5</sup></span><br>
<span style="font-size:18px">0 ≤ <strong>star</strong>t<strong>[i]</strong> &lt; <strong>end[i]</strong>&nbsp;≤ 10<sup>5</sup></span></p>
</div>

<hr/>

## Solution

```py
class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        paired = list(zip(start, end))
        sorted_pairs = sorted(paired, key=lambda x: x[1])
        last_end = 0
        max_meetings = 0

        for s, e in sorted_pairs:
            if s > last_end:
                max_meetings += 1
                last_end = e

        return max_meetings


if __name__ == '__main__':
    ob = Solution()
    if input("custom input: ").lower() in ['yes', 'y', 'yep', 'h', 'ha']:
        arr1 = ast.literal_eval(input("arr1: "))
        arr2 = ast.literal_eval(input("arr2: "))
    else:
        arr1 = [1,2,4,7]
        arr2 = [6,3,6,8]
    n = len(arr1)
    ans = ob.maximumMeetings(n, arr1, arr2)
    print('\nans', ans)  # 3
```
