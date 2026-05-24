# Day 2 — Lab 2A: Six-Pattern Drills (Completed Walkthrough)

## Student Question
> "Explain Big-O notation for a placement interview."

---

# Step 1 — Pattern 1: PERSONA

## Prompt
> "You are a senior placement coach at Aditya University. You have prepared 200 B.Tech CSE students for TCS, Infosys, and Cognizant placement interviews. A 3rd-year CSE student with 7.5 CGPA asks you about Big-O notation. Explain it the way you would in a 1-on-1 prep session — concrete, conversational, exam-relevant."

## Output
Big-O notation is a way to measure how an algorithm’s performance changes as input size increases. In placement interviews, companies use it to check whether you can write scalable code, not just working code.

For example, if you loop through an array once to find the maximum element, the time complexity is O(n) because the number of operations grows linearly with the array size.

```python
arr = [3, 7, 2, 9, 5]
max_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num

print(max_val)
```

If you use nested loops, like comparing every element with every other element, complexity usually becomes O(n²). Interviewers often ask you to compare two solutions and explain why one is more efficient.

## Score
4/5

---

# Step 2 — Pattern 2: FEW-SHOT

## Prompt
> "Here are example explanations from a placement coach:
>
> Q: What is recursion?
> A: A function calling itself with a smaller problem. Like Russian dolls — open one, find a smaller one inside. Stops at base case. Example: factorial.
>
> Q: What is a stack?
> A: LIFO data structure. Push to add, pop to remove. Like a stack of plates — you take from the top.
>
> Q: What is Big-O notation?
> A:"

## Output
Big-O notation tells how fast an algorithm grows as input size increases. Think of it like checking how much extra work a task needs when more data comes in. O(n) means work grows linearly, while O(n²) grows much faster because of nested loops. Example: searching one by one in a list is O(n).

## Score
5/5

---

# Step 3 — Pattern 3: CHAIN-OF-THOUGHT

## Prompt
> "Explain Big-O notation to a placement interview candidate. Think step by step before answering. Step 1: define Big-O in one sentence. Step 2: give one concrete example with code. Step 3: explain why interviewers ask about it. Step 4: synthesise into a 3-sentence summary."

## Output

### Step 1 — Definition
Big-O notation measures how the running time or memory usage of an algorithm grows as input size increases.

### Step 2 — Example with Code
```python
def print_numbers(arr):
    for num in arr:
        print(num)
```

This function runs in O(n) time because it visits each element once.

### Step 3 — Why Interviewers Ask
Interviewers ask Big-O questions to evaluate problem-solving efficiency. Two solutions may produce the same output, but the better engineer chooses the more scalable approach.

### Step 4 — Summary
Big-O notation helps compare algorithm efficiency. It shows how performance changes with larger inputs. In placement interviews, understanding Big-O helps you justify why your solution is optimized.

## Score
5/5

---

# Step 4 — Pattern 4: STRUCTURED OUTPUT

## Prompt
> "Explain Big-O notation for a placement interview. Return ONLY valid JSON with this exact shape — no markdown fences, no commentary:
>
> {
>   "definition": "one-sentence definition",
>   "intuition": "concrete analogy",
>   "code_example": "Python snippet showing O(n) and O(n²)",
>   "common_pitfall": "what students get wrong",
>   "interview_test_question": "a follow-up question an interviewer might ask"
> }"

## Output
```json
{
  "definition": "Big-O notation describes how algorithm performance changes as input size increases.",
  "intuition": "It is like measuring how much extra time a task takes when the amount of work keeps growing.",
  "code_example": "O(n): for i in arr: print(i) | O(n^2): for i in arr: for j in arr: print(i, j)",
  "common_pitfall": "Students often count exact operations instead of focusing on growth rate.",
  "interview_test_question": "Why is binary search O(log n) instead of O(n)?"
}
```

## Score
4/5

---

# Step 5 — Pattern 5: SYSTEM PROMPT

## System Prompt
> "You are a senior placement coach for B.Tech CSE students at an Indian engineering college. You prepare students for TCS / Infosys / Cognizant interviews. You explain technical concepts in 50-80 words max, conversationally, with one concrete code example."

## User Prompt
> "Explain Big-O notation."

## Output
Big-O notation tells how efficiently an algorithm works as data size grows. For example, a single loop through an array is O(n), while nested loops are usually O(n²). Interviewers ask this to check whether you can write scalable solutions, not just correct ones.

```python
for i in arr:
    print(i)
```

## Score
5/5

---

# Step 6 — Pattern 6: PROMPT CHAINING

## Conversation 1 — Extract

### Prompt
> "List the 5 most important sub-concepts a B.Tech student must understand about Big-O notation. Just the list, no explanation."

### Output
1. Definition of Big-O notation  
2. Common time complexities  
3. Difference between time and space complexity  
4. Comparing algorithm efficiency  
5. Importance in coding interviews  

---

## Conversation 2 — Expand

### Prompt
> "For each of these 5 sub-concepts of Big-O notation, write a 1-paragraph explanation tailored to a 3rd-year B.Tech CSE student preparing for placement interviews."

### Output

#### 1. Definition of Big-O notation
Big-O notation measures how the performance of an algorithm changes when input size increases. It helps programmers estimate efficiency without depending on hardware speed.

#### 2. Common time complexities
The most common complexities are O(1), O(log n), O(n), O(n log n), and O(n²). Placement interviews often expect students to identify these quickly.

#### 3. Difference between time and space complexity
Time complexity measures execution speed, while space complexity measures memory usage. A good solution balances both.

#### 4. Comparing algorithm efficiency
Two algorithms may solve the same problem, but one may scale better for large inputs. Big-O helps compare them objectively.

#### 5. Importance in coding interviews
Interviewers use Big-O questions to evaluate optimization skills and analytical thinking. It shows whether you can design scalable software.

---

## Conversation 3 — Polish

### Prompt
> "Synthesise these 5 paragraphs into ONE concise 80-word interview-prep explanation of Big-O notation. Preserve all 5 sub-concepts. Conversational tone. End with one practice question."

### Output
Big-O notation explains how an algorithm’s speed or memory usage changes as input size grows. Common complexities like O(n), O(log n), and O(n²) help compare algorithms and identify scalable solutions. Time complexity focuses on execution speed, while space complexity measures memory usage. In placement interviews, interviewers use Big-O to test optimization and problem-solving ability.

Practice Question: Why is binary search faster than linear search?

## Score
5/5

---

# Final Observation

Prompt engineering patterns significantly affect response quality, structure, tone, and usefulness. Among the six patterns, Prompt Chaining and Chain-of-Thought produced the most detailed and interview-ready explanations, while Few-Shot and System Prompt approaches produced concise, highly consistent outputs suitable for rapid learning.
