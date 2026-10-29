# Module 2: Reflection Agent Exercise

## Objective
Build a reflection agent that generates and iteratively improves text summaries through self-critique.

## Learning Goals
By completing this exercise, you will:
- Implement a basic reflection loop
- Design effective self-critique prompts
- Add stopping conditions to prevent infinite loops
- Compare outputs with and without reflection
- Understand the tradeoffs of reflection (quality vs. speed)

## Scenario
You're building a document summarization agent for a research team. The initial summaries are often too verbose or miss key points. Your task is to implement a reflection pattern where the agent critiques and improves its own summaries.

## Task Requirements

### Part 1: Basic Reflection Loop (Required)
Implement a `ReflectionAgent` class with these methods:

1. **`generate_summary(text, max_length)`**
   - Generate an initial summary of the input text
   - Target length: max_length words

2. **`critique_summary(original_text, summary)`**
   - Critique the summary for:
     - Accuracy (does it capture key points?)
     - Clarity (is it easy to understand?)
     - Conciseness (is it within target length?)
   - Return specific feedback

3. **`improve_summary(original_text, summary, critique)`**
   - Generate an improved summary based on the critique
   - Address the issues identified

4. **`reflect(text, max_length, max_iterations)`**
   - Run the full reflection loop:
     - Generate initial summary
     - For each iteration:
       - Critique current summary
       - If critique says "acceptable", stop
       - Otherwise, improve and continue
     - Return final summary and iteration history

### Part 2: Stopping Conditions (Required)
Implement these stopping conditions:
- Maximum iterations reached
- Critique indicates quality is acceptable
- No significant changes between iterations

### Part 3: Evaluation (Required)
Create a method to compare outputs:
- Run the same input with 0, 1, 2, and 3 reflection iterations
- Print the results showing how quality improves
- Track time taken for each approach

### Part 4: Extensions (Optional)
Choose one or more:
- Add quality scoring (0-10) for each iteration
- Implement multiple critique dimensions (accuracy, clarity, completeness, conciseness)
- Create a visualization of improvement over iterations
- Add user-configurable quality thresholds

## Starter Code Structure

```python
class ReflectionAgent:
    def __init__(self):
        # Initialize your agent
        pass
    
    def generate_summary(self, text, max_length=100):
        # TODO: Implement initial summary generation
        pass
    
    def critique_summary(self, original_text, summary):
        # TODO: Implement self-critique
        pass
    
    def improve_summary(self, original_text, summary, critique):
        # TODO: Implement improvement based on critique
        pass
    
    def reflect(self, text, max_length=100, max_iterations=3):
        # TODO: Implement reflection loop with stopping conditions
        pass
    
    def evaluate_reflection_benefit(self, text):
        # TODO: Compare 0, 1, 2, 3 iterations
        pass
```

## Test Data

Use this sample text for testing:

```python
SAMPLE_TEXT = """
Artificial intelligence has transformed many industries over the past decade. 
Machine learning algorithms can now perform tasks that once required human 
expertise, from medical diagnosis to financial forecasting. Deep learning, 
a subset of machine learning, uses neural networks with multiple layers to 
learn patterns from vast amounts of data. Companies like Google, Amazon, and 
Microsoft have invested billions in AI research and development. However, 
challenges remain, including bias in training data, lack of interpretability, 
and concerns about job displacement. Researchers are working on explainable AI, 
fairness in algorithms, and responsible AI development. The field continues to 
evolve rapidly, with new breakthroughs announced regularly.
"""
```

## Expected Output Format

```
=== Reflection Agent Evaluation ===

Original Text Length: 150 words
Target Summary Length: 50 words

--- Iteration 0 (No Reflection) ---
Summary: [initial summary]
Time: 0.5s

--- Iteration 1 (One Reflection) ---
Initial: [initial summary]
Critique: [specific feedback]
Improved: [improved summary]
Time: 1.2s

--- Iteration 2 (Two Reflections) ---
Initial: [initial summary]
Critique 1: [feedback]
Version 2: [improved]
Critique 2: [feedback]
Final: [final summary]
Time: 2.1s

=== Analysis ===
Quality improvements observed: [your analysis]
Diminishing returns after iteration: [observation]
```

## Implementation Tips

### Mock LLM Approach (Recommended for Learning)
If you don't have API access, simulate the LLM with rule-based logic:

```python
def mock_generate_summary(text, max_length):
    # Simple: take first N words
    words = text.split()[:max_length]
    return ' '.join(words) + '...'

def mock_critique(summary):
    # Check simple rules
    issues = []
    if len(summary.split()) > max_length:
        issues.append("Too long")
    if not summary.endswith('.'):
        issues.append("Incomplete sentence")
    return issues if issues else ["Acceptable"]
```

### Real LLM Approach
If using OpenAI or Anthropic APIs:

```python
def generate_summary(self, text, max_length):
    prompt = f"""Summarize the following text in approximately {max_length} words:

{text}

Summary:"""
    # Call your LLM API here
    response = self.llm.complete(prompt)
    return response

def critique_summary(self, original_text, summary):
    prompt = f"""Review this summary for accuracy, clarity, and conciseness.

Original Text: {original_text}

Summary: {summary}

Critique (identify specific issues or say 'Acceptable'):"""
    response = self.llm.complete(prompt)
    return response
```

## Testing Your Implementation

Run these tests:

1. **Basic functionality**: Can it generate, critique, and improve?
2. **Stopping conditions**: Does it stop at max iterations?
3. **Quality improvement**: Does later iteration improve quality?
4. **Performance**: How much longer does reflection take?

## Success Criteria

Your implementation should:
- ✅ Complete all required parts
- ✅ Run without errors
- ✅ Show measurable improvement with reflection
- ✅ Implement proper stopping conditions
- ✅ Include clear documentation and comments

## Common Pitfalls

1. **Infinite loops**: Always have a max iteration limit
2. **Vague critiques**: Make critiques specific and actionable
3. **Ignoring stopping conditions**: Check if improvement is needed
4. **Poor prompts**: Be explicit about what to evaluate
5. **No improvement tracking**: Log each iteration to see progress

## Reflection Questions (Answer After Completing)

1. How many iterations typically produced the best results?
2. Did you observe diminishing returns? At what iteration?
3. What types of improvements did reflection make?
4. When would you choose NOT to use reflection?
5. How would you make this production-ready?

## Time Estimate
- Part 1: 45-60 minutes
- Part 2: 15-20 minutes
- Part 3: 20-30 minutes
- Part 4 (optional): 30-60 minutes

## Next Steps
After completing this exercise:
1. Compare your solution to the provided solution
2. Try the exercise with a real API if you used mocks
3. Apply reflection to a different domain (code generation, email writing, etc.)
4. Move to Module 3: Tool Usage Pattern

---

**Good luck! Remember: the goal is to understand the reflection pattern, not to create perfect summaries.**
