# Andrew Ng's Agentic AI Course - Practice Materials

## Course-Derived Practice Materials

This directory combines local notes, AI-generated study aids, and assignment/lab copies sourced from the public learner repository [jeffmasc/agentic_ai_andrew_ng](https://github.com/jeffmasc/agentic_ai_andrew_ng). Naming conventions and included grader files suggest that some copies originated from DeepLearning.AI's **Agentic AI** course, but this project has not independently verified every file against the current course platform. Treat them as course-derived study copies, not an official DeepLearning.AI distribution.

---

## ⚠️ Quiz Notice

**No course quiz questions are included.** No quiz-question files were found in the three mirrored learner repositories. Use the quizzes on the official DeepLearning.AI course platform for the course's own assessments.

The `quiz.md` files in each module are **AI-generated study aids** created for self-assessment purposes. They contain:
- ⚠️ **Prominent disclaimers** - Not DeepLearning.AI course quiz questions
- 📚 **Study questions** - Based on local lecture notes and transcripts
- 🔍 **Self-check tools** - Use them to test your understanding

**These are not the course platform's quiz questions.**

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
- ✅ = Course-derived copy included
- ❌ = Not included in this practice package
- ⚠️ = AI-generated or provenance not independently verified

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

### Step 3: Run Tests Locally
After filling the exercise placeholders, run the tests from that module's directory:

```bash
python unittests.py
```

The local runner extracts the graded functions from the adjacent assignment notebook and substitutes deterministic model responses. It requires no API key, makes no network requests, and exits with a nonzero status when an exercise fails. The untouched starter notebook is expected to fail until you implement it.

To verify the test harness itself against the supplied solution:

```bash
python unittests.py --notebook C1M2_Assignment_Solution.ipynb
```

### Step 4: Check Solution (After Genuine Attempt)
Only after completing your attempt, compare with the solution:

```bash
# View the solution notebook
jupyter notebook C1M2_Assignment_Solution.ipynb
```

---

## 📖 Recommended Learning Path

1. **Watch the course videos** on the [DeepLearning.AI learning platform](https://learn.deeplearning.ai/courses/agentic-ai/information), or review the local transcript-based notes
2. **Try the AI-generated quiz** as an optional self-check
3. **Explore ungraded demos** to see concepts in action
4. **Complete the assignment copy** by filling in the exercise blanks
5. **Run the local tests** to verify the implementation wiring
6. **Compare with the supplied solution copy** only after a genuine attempt

---

## 💡 Important Notes

### About Testing
- ✅ Run `python unittests.py` from the assignment directory after completing the placeholders.
- ✅ Local tests use fake model responses, so they require no API key and incur no API cost.
- ✅ The same `test_*` helpers also run from the notebook's test cells.
- ⚠️ These tests check function wiring, model-call arguments, tool-result bookkeeping, and return contracts. They do not grade prose quality or verify live APIs.
- 📝 The imported course-platform autograder remains under `autograder/` for reference and is not used by the local runner.

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

## Sources and Provenance

- **Course:** [Agentic AI](https://learn.deeplearning.ai/courses/agentic-ai/information), taught by Andrew Ng on DeepLearning.AI
- **Primary learner repository:** [jeffmasc/agentic_ai_andrew_ng](https://github.com/jeffmasc/agentic_ai_andrew_ng)
- **Assignment and demo status:** Course-derived copies from public learner repositories; not independently verified as unmodified official distributions
- **Quiz files:** AI-generated study aids, not DeepLearning.AI course quiz questions

---

## ✨ Tips for Success

1. **Don't skip demos** - They provide valuable context before the graded assignment
2. **Read instructions carefully** - Each assignment has specific requirements
3. **Test incrementally** - Run the deterministic local tests after completing each exercise section
4. **Understand, don't copy** - Solutions are for learning, not shortcuts
5. **Keep lecture notes handy** - Reference course concepts while coding
