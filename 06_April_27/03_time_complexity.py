'''
https://github.com/shahwar-coder/TUF-Pinnacle/tree/main/time_complexity

But you can have a quick skim here.
'''

"""
Q1. Purpose of Complexity Analysis:
Measures algorithm efficiency (time & memory) as input grows, helps choose the best algorithm.

Q2. Time vs Space Complexity:
Time = growth of operations; Space = extra memory needed.

Q3. Big O Notation:
Describes upper bound of growth rate, focusing on scalability and ignoring constants.

Q4. Growth Order (fast → slow):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!).

Q5. Why Big O is Asymptotic:
Measures performance as input approaches infinity, ignoring small constant effects.

Q6. Quick Shorthand:
Time = speed, Space = memory, Big O = upper bound, focus on scalability, constants ignored.


Q7. Difference between Time Complexity and Time Taken:
Time complexity predicts growth of operations; time taken is the actual runtime on specific hardware.

Q8. Why two O(n) algorithms differ in speed:
Big O hides constants; real performance depends on implementation, hardware, language and optimizations.

Q9. What time complexity really tells us:
Predicts how runtime scales as input size grows; used to compare algorithm scalability.

Q10. Why measure real time taken:
Benchmarks reveal actual performance for realistic inputs since constants and hardware matter.

Q11. Correct way to evaluate an algorithm:
Use complexity for scalability and runtime benchmarks for practical performance; combine both for decisions.

Q12. Quick Shorthand:
Complexity = theoretical growth
Time taken = real speed
Same O(n) ≠ same performance
Both matter for evaluation
Constants matter for small inputs


Q13. What Big-O notation represents:
Upper bound on runtime growth rate, showing how performance scales with input size while ignoring constants.

Q14. Why Big-O ignores constants:
Constants do not impact long-term growth behavior; scaling trend matters more than exact operation count.

Q15. Common time complexities (best → worst):
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!).

Q16. Meaning of “upper bound” in Big-O:
Worst-case growth limit; runtime will not exceed this scaling rate.

Q17. How Big-O helps in real-world programming:
Predicts scalability, compares algorithms, and guides performance-aware design decisions before implementation.

Q18. Quick Shorthand:
Big-O = upper bound
Ignores constants
Shows scalability trend
Worst-case focus
Used to compare algorithms


Q19. Why constants are ignored in Big-O:
Big-O studies growth as n becomes huge; constants only scale runtime and do not change growth class.

Q20. Different cases in time complexity:
Best case (fastest), average case (expected), worst case (maximum runtime for any input).

Q21. Focus on worst-case complexity:
Guaranteed upper bound avoids surprises; vital for reliable and critical systems.

Q22. Average case vs worst case:
Average is probability-based expected behavior; worst assumes the toughest input always.

Q23. Do constants affect real runtime:
Yes for practical small inputs; no for theoretical scalability classification.

Q24. Quick Shorthand:
Drop constants → growth only
Best/avg/worst cases → full picture
Worst case = safest guarantee
Average depends on input probability
Constants matter in real execution


Q25. Meaning of Big-O, Big-Ω, Big-Θ:
Bounds on algorithm growth. O = upper bound, Ω = lower bound, Θ = tight bound (grows at that rate).

Q26. Θ(f(n)) meaning:
Runtime is both upper and lower bounded by f(n); actual growth matches f(n) asymptotically.

Q27. Why Θ used for average behavior:
Gives tight bounds for typical performance, not just extremes.

Q28. Can O(n²) and Θ(n) both be correct:
Yes. O(n²) may describe a loose upper bound; Θ(n) is the true growth rate.

Q29. Quick Shorthand:
O → at most this fast
Ω → at least this fast
Θ → about this fast
They describe bounds, not input cases
Best/avg/worst are scenarios, not symbols


Q30. Space Complexity:
Measures memory usage as size of input grows, including input storage and temporary memory.

Q31. Input Space vs Auxiliary Space:
Input space stores given data; auxiliary space is extra memory used by the algorithm.

Q32. Why focus on auxiliary space:
Input space is fixed; auxiliary space reflects algorithm efficiency.

Q33. Reducing space complexity:
Reuse variables, prefer in-place algorithms, use generators, avoid deep recursion if possible.

Q34. Quick Shorthand:
Space = input + auxiliary
Auxiliary depends on algorithm
Recursive stack counts as space
In-place minimizes memory usage


Q35. Sequential loops rule:
Loops executed one after another have their complexities added, then keep dominant term.

Q36. Nested loops rule:
Inner loop multiplies the outer loop’s complexity; multiply iteration counts for total complexity.

Q37. Mixed loops:
Combine addition and multiplication rules, then retain the slowest growing (dominant) term.

Q38. Constant loops:
Loops running a fixed number of times are O(1) and constants are ignored in Big-O.

Q39. Quick Shorthand:
Sequential → add
Nested → multiply
Dominant term decides final O()
Constants vanish in Big-O


Q40. Rate of change in time:
Shows how runtime increases with input size; helps observe actual scalability trend.

Q41. Big-O relation to rate of change:
Big-O models growth theoretically by focusing on how runtime scales as input increases.

Q42. Constant loops and O(1):
Runtime stays constant with no change as input grows; flat growth curve.

Q43. Doubling input to detect growth:
O(n) doubles time; O(n²) quadruples time; O(log n) increases slightly.

Q44. Big-O for scalability, not speed:
Same complexity class can differ in absolute runtime due to constants or optimizations.

Q45. Quick Shorthand:
Rate of change → experimental growth
Big-O → theoretical growth
Constant = zero slope
Linear = ×2 time on ×2 input
Quadratic = ×4 time on ×2 input
"""

