# Andrew Ng's Agentic AI Course - Practice Materials

## 🎓 Authentic Course Materials

This directory contains **authentic course materials** from Andrew Ng's Agentic AI course, sourced from the [jeffmasc/agentic_ai_andrew_ng](https://github.com/jeffmasc/agentic_ai_andrew_ng) repository. These are the actual graded assignments and ungraded lab demos used in the Coursera course.

---

## ⚠️ Quiz Notice

**No official quiz questions are included.** Quiz questions are platform-locked on Coursera and cannot be legally extracted. 

The `quiz.md` files in each module are **AI-generated study aids** created for self-assessment purposes. They contain:
- ⚠️ **Prominent disclaimers** - Not official Coursera questions
- 📚 **Study questions** - Based on lecture concepts and materials
- 🔍 **Self-check tools** - Use them to test your understanding

**These are NOT the real quiz questions from the course.**

---

## 📊 Assignment Status

| Module | Graded Assignment | Ungraded Demos | Quiz |
|--------|------------------|----------------|------|
| **Module 1: Introduction** | ❌ None | ❌ None | ⚠️ AI-generated |
| **Module 2: Reflection** | ✅ C1M2_Assignment.ipynb | ✅ 2 demos | ⚠️ AI-generated |
| **Module 3: Tool Use** | ✅ C1M3_Assignment.ipynb | ✅ 2 demos | ⚠️ AI-generated |
| **Module 4: Practical** | ❌ None | ⚠️ Check directory | ⚠️ AI-generated |
| **Module 5: Multi-Agent** | ✅ C1M5_Assignment.ipynb | ✅ 2 demos | ⚠️ AI-generated |

**Legend:**
- ✅ = Authentic material included
- ❌ = Not available (no graded assignment for this module)
- ⚠️ = AI-generated or status uncertain

---

## 🚀 Quick Start

### Step 1: Explore Ungraded Demos (Optional)
If available, start with ungraded demos to get familiar with the concepts:

```bash
cd module2_reflection/demos/chart_generation
# Explore the Jupyter notebook
```

### Step 2: Work Through Graded Assignment
Open the assignment notebook and work through the exercises:

```bash
cd module2_reflection
jupyter notebook C1M2_Assignment.ipynb
```

**Look for exercise blanks:**
```python
### START CODE HERE ###
# Your code goes here
### END CODE HERE ###
```

### Step 3: Run Unit Tests Locally
Verify your solution with the provided unit tests:

```bash
python unittests.py
```

### Step 4: Check Solution (After Genuine Attempt)
Only after completing your attempt, compare with the solution:

```bash
# View the solution notebook
jupyter notebook C1M2_Assignment_Solution.ipynb
```

---

## 📖 Recommended Learning Path

1. **Watch lecture videos** on Coursera (or your video notes)
2. **Try AI-generated quiz** (optional self-check, not official questions)
3. **Explore ungraded demos** to see concepts in action
4. **Complete graded assignment** - fill in the exercise blanks yourself
5. **Run unit tests** to verify your implementation
6. **Compare with solution** only after genuine attempt

---

## 💡 Important Notes

### About the Autograder
- ⚠️ **Autograder won't work** without active Coursera course enrollment
- ✅ **Unit tests are for local verification** - use `python unittests.py`
- 📝 **Autograder directory included** for reference (you won't need it for practice)

### About Exercise Blanks
- ✅ **Exercise blanks are preserved** in `C1MX_Assignment.ipynb` files
- 🎯 **Fill in `### START CODE HERE ###` sections** yourself
- 🔍 **Solutions are reference only** - attempt exercises first

### About API Keys
- 🔑 You'll need OpenAI API key for assignments (set `OPENAI_API_KEY` environment variable)
- 💰 Assignments use OpenAI API calls (costs apply)
- ⚙️ Some demos might require additional API keys (check demo README files)

---

## 📁 Directory Structure

```
module1_intro/
  ├── quiz.md                    # ⚠️ AI-generated study questions
  
module2_reflection/
  ├── C1M2_Assignment.ipynb      # ✅ Graded assignment (with blanks)
  ├── C1M2_Assignment_Solution.ipynb  # ✅ Reference solution
  ├── unittests.py               # ✅ Local verification
  ├── quiz.md                    # ⚠️ AI-generated study questions
  └── demos/                     # ✅ Ungraded demos
      ├── chart_generation/
      └── sql_reflection/

module3_tool_use/
  ├── C1M3_Assignment.ipynb      # ✅ Graded assignment (with blanks)
  ├── C1M3_Assignment_Solution.ipynb  # ✅ Reference solution
  ├── unittests.py               # ✅ Local verification
  ├── quiz.md                    # ⚠️ AI-generated study questions
  └── demos/                     # ✅ Ungraded demos
      ├── ugl1/
      └── ugl2/

module4_practical/
  ├── quiz.md                    # ⚠️ AI-generated study questions
  
module5_multiagent/
  ├── C1M5_Assignment.ipynb      # ✅ Graded assignment (with blanks)
  ├── C1M5_Assignment_Solution.ipynb  # ✅ Reference solution
  ├── unittests.py               # ✅ Local verification
  ├── quiz.md                    # ⚠️ AI-generated study questions
  └── demos/                     # ✅ Ungraded demos
      ├── ugl1/
      └── ugl2/
```

---

## 📚 Source

Authentic course materials sourced from:
- **Primary:** [jeffmasc/agentic_ai_andrew_ng](https://github.com/jeffmasc/agentic_ai_andrew_ng)
- **Quiz files:** AI-generated study aids (not official Coursera quizzes)

---

## ✨ Tips for Success

1. **Don't skip demos** - They provide valuable context before the graded assignment
2. **Read instructions carefully** - Each assignment has specific requirements
3. **Test incrementally** - Run unit tests after completing each exercise section
4. **Understand, don't copy** - Solutions are for learning, not shortcuts
5. **Keep lecture notes handy** - Reference course concepts while coding
