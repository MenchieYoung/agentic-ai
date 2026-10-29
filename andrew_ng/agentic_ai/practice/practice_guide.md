# Andrew Ng's Agentic AI Course - Practice Guide

## Overview

This guide helps you work through **authentic Andrew Ng Agentic AI course materials** sourced from the jeffmasc repository. These materials are designed to match the official Coursera course experience as closely as possible.

## Materials Authenticity

### ✅ Graded Assignments (AUTHENTIC)
- **Source**: Official course assignments from jeffmasc/agentic_ai_andrew_ng
- **Status**: **Identical to official Coursera course assignments**
- **Available for**: Modules 2, 3, and 5
- **Format**: Jupyter notebooks with exercise blanks (### START CODE HERE ###)
- **Testing**: Includes unit tests (`unittests.py`) for local validation

### ✅ Ungraded Demos (AUTHENTIC)
- **Source**: Official reference implementations from course materials
- **Purpose**: Explore concepts before attempting graded assignments
- **Format**: Complete working examples (no blanks to fill)

### ⚠️ Quizzes (AI-GENERATED STUDY AIDS)
- **Status**: **NOT official course quizzes**
- **Reason**: Official quizzes are locked within Coursera platform
- **Purpose**: Study aids for self-assessment
- **Recommendation**: Use for review, but focus on assignments for authentic practice

## Available Authentic Assignments

### Module 2: Reflection Pattern
- **Assignment**: `C1M2_Assignment.ipynb`
- **Focus**: Build a chart generation agent with reflection/self-critique
- **Skills**: Prompt engineering, iterative improvement, visualization
- **Unit Tests**: Available for local validation

### Module 3: Tool Use Pattern  
- **Assignment**: `C1M3_Assignment.ipynb`
- **Focus**: Implement function calling and tool integration
- **Skills**: API integration, structured outputs, tool selection
- **Unit Tests**: Available for local validation

### Module 5: Multi-Agent Systems
- **Assignment**: `C1M5_Assignment.ipynb`
- **Focus**: Build coordinated multi-agent workflows
- **Skills**: Agent orchestration, communication patterns, task decomposition
- **Unit Tests**: Available for local validation

## How to Use Assignments

### 1. Setup Your Environment
```bash
# Navigate to the assignment directory
cd module2_reflection/  # or module3_tool_use/ or module5_multiagent/

# Install dependencies (if not already done)
pip install jupyter openai python-dotenv

# Set up API key
echo "OPENAI_API_KEY=your_key_here" > .env
```

### 2. Open the Assignment
```bash
# Launch Jupyter notebook
jupyter notebook C1M2_Assignment.ipynb  # Replace with appropriate module
```

### 3. Complete the Assignment

**READ INSTRUCTIONS CAREFULLY**
- Each assignment starts with a clear description of what you'll build
- Follow the narrative - it guides you through concepts progressively

**FILL IN CODE BLANKS ONLY**
```python
### START CODE HERE ###
# Your implementation goes here
# Only modify code within these markers
### END CODE HERE ###
```

**DO NOT MODIFY**:
- Setup cells (imports, configurations)
- Test cells (they validate your work)
- Helper function definitions (unless explicitly told to)

### 4. Test Your Implementation

**Run cells sequentially**:
- Execute each cell from top to bottom
- Don't skip cells - later cells depend on earlier ones
- Watch for output and error messages

**Use unit tests**:
```bash
# Run local tests (in terminal, from assignment directory)
python unittests.py

# Expected output when passing:
# ✓ test_function_name_1
# ✓ test_function_name_2
# All tests passed!
```

### 5. Iterate and Debug

**When tests fail**:
- Read the error message carefully
- Check your logic in the ### START CODE HERE ### section
- Print intermediate values to understand what's happening
- Compare your approach with the assignment hints

**Common mistakes**:
- Forgetting to return a value
- Wrong variable names
- Incorrect indentation
- Missing edge case handling

### 6. When to Check Solutions

**✅ Check solutions AFTER**:
- You've genuinely attempted the exercise (>30 minutes)
- Your code works but you want to see alternative approaches
- You're stuck and need a hint (peek at structure, not full code)
- Tests pass and you want to compare implementations

**❌ DON'T check solutions**:
- As your first step (defeats the learning purpose)
- Without attempting the exercise
- To copy-paste code (you won't learn the pattern)

## Local Testing Setup

### Understanding Unit Tests

Each assignment includes `unittests.py` - automated tests that validate your implementation.

**How to run**:
```bash
# From the assignment directory (e.g., module2_reflection/)
python unittests.py
```

**Understanding output**:

✅ **All tests pass**:
```
✓ test_generate_chart
✓ test_reflection_loop
✓ test_tool_usage
===========================
All 3 tests passed!
```

❌ **Test failure**:
```
✗ test_generate_chart
  Expected: {"type": "bar", "data": [...]}
  Got: None
  
1 of 3 tests failed
```

**What to do when tests fail**:
1. **Read the failure message** - tells you what went wrong
2. **Check the expected vs actual output** - shows the mismatch
3. **Review your code** in the corresponding ### START CODE HERE ### section
4. **Add debug prints** to see intermediate values
5. **Re-run** after fixes

### Autograder Limitations

⚠️ **Important**: The official autograder only works within Coursera platform

**What you have locally**:
- Unit tests that validate core functionality
- Same test logic as the autograder (where possible)
- Immediate feedback on correctness

**What you DON'T have locally**:
- Official Coursera grading
- Course completion credit
- Some advanced integration tests that require Coursera infrastructure

**Recommendation**: Local tests are sufficient for learning and practice. If you want official certification, enroll in the Coursera course.

## Recommended Study Workflow

### For Each Module:

```
1. WATCH lectures (1-2 hours)
   └─> Understand concepts and patterns
   
2. TRY AI-generated quiz (15-30 min) [OPTIONAL]
   └─> Self-check conceptual understanding
   
3. EXPLORE ungraded demos (30-60 min) [OPTIONAL]
   └─> See patterns in action
   └─> Experiment with working code
   
4. READ assignment instructions (10-15 min)
   └─> Understand what you'll build
   └─> Note the learning objectives
   
5. IMPLEMENT exercise blanks (2-4 hours)
   └─> Work through each ### START CODE HERE ### section
   └─> Test frequently by running cells
   
6. RUN unit tests (5-10 min)
   └─> Validate your implementation
   └─> Debug failures
   
7. DEBUG and iterate (variable time)
   └─> Fix failing tests
   └─> Improve code quality
   └─> Handle edge cases
   
8. CHECK solution (30-60 min)
   └─> Compare approaches
   └─> Understand alternatives
   └─> Learn optimization techniques
   
9. REFLECT on learning (15-30 min)
   └─> What pattern did you implement?
   └─> Where could you apply this?
   └─> What was challenging?
```

### Time Estimates Per Module:
- **Module 2 (Reflection)**: 4-6 hours total
- **Module 3 (Tool Use)**: 4-6 hours total  
- **Module 5 (Multi-Agent)**: 6-8 hours total

## Common Pitfalls

### ❌ 1. Modifying Code Outside Exercise Boundaries
**Problem**: Changing setup code, test cells, or helper functions
**Why it's bad**: Breaks the assignment's test infrastructure
**Fix**: Only edit code between `### START CODE HERE ###` and `### END CODE HERE ###`

### ❌ 2. Skipping Unit Tests
**Problem**: Running notebook cells but not `python unittests.py`
**Why it's bad**: You might miss edge cases or incorrect behavior
**Fix**: Always run unit tests before considering an exercise complete

### ❌ 3. Looking at Solutions Too Early
**Problem**: Checking solution code before genuine attempt
**Why it's bad**: You miss the learning that comes from struggling and figuring it out
**Fix**: Set a timer for 30+ minutes of genuine effort before peeking

### ❌ 4. Not Understanding WHY Solutions Work
**Problem**: Copying solution code without understanding the logic
**Why it's bad**: You won't be able to apply patterns to new problems
**Fix**: For each line in the solution, ask "Why is this needed? What pattern does this implement?"

### ❌ 5. Running Cells Out of Order
**Problem**: Jumping around the notebook, re-running cells randomly
**Why it's bad**: State becomes inconsistent, variables may have wrong values
**Fix**: Use "Kernel → Restart & Run All" to ensure clean execution order

### ❌ 6. Ignoring Error Messages
**Problem**: Seeing an error and immediately checking the solution
**Why it's bad**: Error messages often tell you exactly what's wrong
**Fix**: Read error messages carefully - they guide you to the problem

### ❌ 7. Hardcoding Test Cases
**Problem**: Writing code that only works for the specific test example
**Why it's bad**: Doesn't generalize to other inputs
**Fix**: Think about edge cases and make your code work for any valid input

## Module-Specific Notes

### Module 2: Reflection Pattern (Chart Generation)
**Key Concepts**:
- Self-critique: Agent evaluates its own output
- Iterative improvement: Multiple rounds of refinement
- Structured feedback: Clear criteria for "good" vs "bad"

**What You'll Build**:
- A chart generation agent that creates visualizations
- A reflection mechanism that critiques the chart
- An improvement loop that iterates until quality threshold

**Common Challenges**:
- Designing effective critique prompts
- Balancing strictness (too picky vs too lenient)
- Preventing infinite loops in reflection

**Tips**:
- Start with simple charts before complex ones
- Make critique criteria explicit and measurable
- Limit reflection iterations (e.g., max 3 rounds)

### Module 3: Tool Use (Function Calling)
**Key Concepts**:
- Function schemas: Describing tools to LLMs
- Tool selection: Choosing the right tool for the task
- Structured outputs: Parsing LLM responses into function calls

**What You'll Build**:
- Tool definitions (search, calculate, lookup)
- Function calling logic
- Result integration back to the agent

**Common Challenges**:
- Correct JSON schema format for tools
- Parsing LLM responses reliably
- Handling tool errors gracefully

**Tips**:
- Test each tool independently first
- Use explicit tool descriptions (clear, specific)
- Add validation for tool arguments
- Handle cases where LLM doesn't call any tool

### Module 5: Multi-Agent Systems (Coordination)
**Key Concepts**:
- Agent roles: Different agents with specialized capabilities
- Communication: How agents share information
- Orchestration: Sequential vs parallel workflows

**What You'll Build**:
- Multiple specialized agents (planner, executor, reviewer)
- Communication protocols between agents
- Orchestration logic (who runs when)

**Common Challenges**:
- Managing state across agents
- Preventing agent "conversations" from diverging
- Coordinating outputs from multiple agents

**Tips**:
- Define clear roles and responsibilities per agent
- Use explicit handoffs between agents
- Keep communication structured (not free-form chat)
- Test each agent independently before integration

## Resources

### Original Course
- **Platform**: Coursera
- **Course**: "AI Agentic Design Patterns with AutoGen" by Andrew Ng
- **Link**: Search "Andrew Ng Agentic AI" on Coursera
- **Includes**: Video lectures, official quizzes (with grading), assignment autograder

### Source Repository
- **GitHub**: [jeffmasc/agentic_ai_andrew_ng](https://github.com/jeffmasc/agentic_ai_andrew_ng)
- **Contains**: Authentic graded assignments, ungraded demos, solutions
- **Status**: Most faithful reproduction of official course materials available publicly

### Documentation
- **OpenAI API**: https://platform.openai.com/docs/
- **Function Calling**: https://platform.openai.com/docs/guides/function-calling
- **Prompt Engineering**: https://platform.openai.com/docs/guides/prompt-engineering

### Community
- Course discussion forums (if enrolled in Coursera)
- GitHub issues on jeffmasc repository for technical problems
- OpenAI developer forum for API questions

## How to Get Help

### Step 1: Debug Systematically
```python
# Add print statements to understand what's happening
def your_function(input_data):
    print(f"Input: {input_data}")  # See what you're working with
    
    ### START CODE HERE ###
    result = your_implementation(input_data)
    print(f"Result: {result}")  # Check intermediate output
    ### END CODE HERE ###
    
    return result
```

### Step 2: Consult Resources
1. **Re-read assignment instructions** - often contains hints
2. **Review lecture content** - reinforces the pattern
3. **Check function docstrings** - explains expected behavior
4. **Read test cases** - shows expected input/output

### Step 3: Use Solution Strategically
```
❌ Don't: Copy entire solution
✅ Do: Look at solution structure
✅ Do: Understand the approach
✅ Do: Re-implement in your own words
```

### Step 4: Ask Specific Questions
When seeking help:
- ✅ "I'm getting X error when trying Y approach, expected Z"
- ✅ "My reflection loop runs forever, how do I add a stopping condition?"
- ❌ "How do I do Exercise 2?" (too broad)
- ❌ "Can someone share the solution?" (defeats learning)

## Prerequisites

### Required
- **Python**: Intermediate level (functions, classes, basic data structures)
- **APIs**: Understanding of REST APIs and JSON
- **LLMs**: Basic familiarity with how language models work
- **Command line**: Can navigate directories, run Python scripts

### Nice to Have
- **Jupyter**: Experience with notebook environments
- **Async/await**: For advanced concurrent patterns (Module 5)
- **Testing**: Understanding of unit tests (makes debugging easier)

### Software Setup
```bash
# Python 3.8 or higher
python --version

# Install core dependencies
pip install jupyter openai python-dotenv

# Verify installation
python -c "import openai; print('Ready to go!')"
```

## Quick Reference

### File Structure
```
practice/
├── practice_guide.md (this file)
├── README.md (overview of materials)
│
├── module2_reflection/
│   ├── C1M2_Assignment.ipynb (✅ authentic assignment)
│   ├── unittests.py (local validation)
│   ├── solution/ (reference implementations)
│   └── ungraded_demos/ (optional exploration)
│
├── module3_tool_use/
│   ├── C1M3_Assignment.ipynb (✅ authentic assignment)
│   ├── unittests.py (local validation)
│   ├── solution/ (reference implementations)
│   └── ungraded_demos/ (optional exploration)
│
└── module5_multiagent/
    ├── C1M5_Assignment.ipynb (✅ authentic assignment)
    ├── unittests.py (local validation)
    ├── solution/ (reference implementations)
    └── ungraded_demos/ (optional exploration)
```

### Command Cheatsheet
```bash
# Start working on an assignment
cd module2_reflection/
jupyter notebook C1M2_Assignment.ipynb

# Run unit tests
python unittests.py

# Check test output
# ✓ = test passed
# ✗ = test failed (read error message)

# Restart Jupyter kernel (if state is inconsistent)
# In notebook: Kernel → Restart & Run All

# View solution (after attempting)
jupyter notebook solution/C1M2_Solution.ipynb
```

### Learning Checklist

**For each assignment**:
- [ ] Watched corresponding lecture videos
- [ ] Read assignment instructions completely
- [ ] Attempted all exercise blanks (30+ min minimum)
- [ ] All unit tests passing (`python unittests.py`)
- [ ] Compared approach with solution
- [ ] Understood why solution works
- [ ] Can explain the pattern to someone else

---

## Final Tips for Success

### 🎯 Focus on Patterns, Not Code
The course teaches **design patterns**:
- **Reflection**: Self-critique and improvement
- **Tool Use**: Extending LLM capabilities  
- **Multi-Agent**: Coordinated specialized agents

Understanding these patterns > memorizing code

### 🔄 Embrace Iteration
Your first attempt won't be perfect - that's expected!
- Try → Test → Debug → Improve → Repeat
- This mirrors how real agents work (especially reflection pattern)

### 🧪 Experiment Actively  
- Change prompts and observe behavior
- Try different parameter values
- Break things intentionally to understand boundaries
- Add print statements everywhere

### 📊 Track Your Learning
After each module, note:
- What pattern did you implement?
- Where could you apply this in your work?
- What was surprisingly easy/hard?
- What would you do differently?

### 🚀 Build Real Projects
After completing assignments:
- Adapt patterns to your own problems
- Combine patterns (reflection + tool use)
- Scale up complexity gradually
- Share what you build!

---

**Remember**: These are **authentic course materials**. The assignments you're completing are the same ones used in the official Coursera course. Take them seriously, work through them thoroughly, and you'll gain the same practical skills as enrolled students.

**The difference**: You won't get a certificate without Coursera enrollment, but you'll learn the patterns just as well. Focus on understanding > credential collection.

Good luck, and enjoy building agentic AI systems! 🤖✨
