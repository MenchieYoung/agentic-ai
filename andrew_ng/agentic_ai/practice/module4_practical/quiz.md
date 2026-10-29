# Module 4 Quiz: Practical Tips for Agentic AI

> ⚠️ **DISCLAIMER: AI-Generated Study Aid**
> 
> This quiz was created by AI as a study aid based on course lecture content.
> **These are NOT the official course quiz questions**, which are platform-locked on Coursera.
> 
> Use these questions to:
> - Test your understanding of lecture concepts
> - Prepare for the actual course quizzes
> - Review key topics before moving to coding exercises
> 
> The official course uses different questions that you can only access through Coursera enrollment.

## Instructions
- This quiz contains 12 multiple-choice questions
- Each question has one correct answer
- Answer all questions before checking the answer key
- Passing score: 70% (9/12 correct)

---

## Questions

### Q1. Why is evaluation particularly important for agentic AI systems?
A) They're more expensive to run  
B) Their multi-step nature makes it harder to predict outputs  
C) They require more compute resources  
D) They're newer technology

### Q2. What is F1-score in the context of agent evaluation?
A) The speed of the agent's response  
B) A metric combining precision and recall to measure classification quality  
C) The cost per API call  
D) The number of function calls made

### Q3. In agent evaluation, what does "precision" measure?
A) How fast the agent responds  
B) Of the items the agent identified, how many were correct  
C) How many correct items the agent found out of all possibilities  
D) The computational precision of calculations

### Q4. What is "recall" in agent evaluation?
A) The agent's ability to remember previous conversations  
B) Of all possible correct items, how many did the agent find  
C) The agent's error recovery capability  
D) How often the agent is called

### Q5. Why is hyperparameter optimization important for agentic systems?
A) It makes agents run faster  
B) Different values (temperature, max tokens, etc.) can significantly affect output quality  
C) It reduces API costs to zero  
D) It's required by LLM providers

### Q6. What is a common production architecture pattern for agentic AI?
A) Running everything in a single long API call  
B) Separating orchestration, tool execution, and state management  
C) Using only synchronous processing  
D) Avoiding databases entirely

### Q7. When tracking agent performance in production, what's important to monitor?
A) Success rate and error types  
B) Latency and cost per request  
C) Tool usage patterns  
D) All of the above

### Q8. What is "prompt versioning" and why does it matter?
A) Tracking changes to prompts to understand impact on quality  
B) Using different Python versions  
C) Updating the LLM model version  
D) Organizing code files

### Q9. How should you handle agent failures in production?
A) Crash and require manual restart  
B) Implement graceful degradation and fallback strategies  
C) Ignore errors and continue  
D) Always escalate to humans immediately

### Q10. What role does logging play in agentic systems?
A) It's optional for simple agents  
B) It's crucial for debugging and understanding agent behavior  
C) It only matters for legal compliance  
D) It should be avoided due to cost

### Q11. When optimizing agent latency, what tradeoff often exists?
A) Speed vs. accuracy/quality  
B) Speed vs. cost (they always move together)  
C) Speed vs. simplicity  
D) There are no tradeoffs

### Q12. What is a "golden dataset" in agent evaluation?
A) The most expensive test cases  
B) A curated set of examples with known correct answers for testing  
C) Data about gold prices  
D) The training data for the LLM

---

## Answer Key

### Q1. Answer: B
**Explanation**: Evaluation is particularly important for agentic AI because their multi-step, autonomous nature makes outputs harder to predict compared to single-shot LLM calls. Multiple steps with branching logic create more complexity. While cost (A) and compute (C) are considerations, they don't explain why evaluation is *particularly* important. Being newer technology (D) isn't the fundamental reason.

### Q2. Answer: B
**Explanation**: F1-score is a metric that combines precision (how many identified items were correct) and recall (how many correct items were found) into a single measure of classification quality. It's the harmonic mean of precision and recall. It's not about speed (A), cost (C), or function call count (D).

### Q3. Answer: B
**Explanation**: Precision measures: of the items the agent identified/predicted, what fraction were actually correct? For example, if an agent identifies 10 entities but only 7 are correct, precision is 70%. It's not about speed (A), finding all possibilities (that's recall, C), or computational precision (D).

### Q4. Answer: B
**Explanation**: Recall measures: of all the correct items that exist, what fraction did the agent find? For example, if there are 10 correct entities and the agent found 7, recall is 70%. It's not about conversation memory (A), error recovery (C), or call frequency (D).

### Q5. Answer: B
**Explanation**: Hyperparameter optimization matters because settings like temperature, max tokens, top-p, and system prompts can significantly affect output quality, creativity, and reliability. Finding optimal values for your use case improves results. It doesn't make agents faster (A), eliminate costs (C), or satisfy requirements from providers (D).

### Q6. Answer: B
**Explanation**: A common production pattern separates concerns: orchestration (workflow control), tool execution (isolated function calls), and state management (conversation context, session data). This separation improves maintainability, scalability, and debugging. Single long calls (A), only synchronous processing (C), and avoiding databases (D) are not recommended patterns.

### Q7. Answer: D
**Explanation**: All of these are important to monitor in production: success rate and error types (to identify issues), latency and cost (to manage resources), and tool usage patterns (to understand behavior and optimize). Comprehensive monitoring requires tracking multiple dimensions.

### Q8. Answer: A
**Explanation**: Prompt versioning means tracking changes to prompts over time so you can understand how modifications impact quality, behavior, and performance. This is crucial for iterative improvement and debugging. It's not about Python versions (B), LLM versions (C), or code organization (D), though those matter separately.

### Q9. Answer: B
**Explanation**: Production agents should implement graceful degradation (reduced functionality when errors occur) and fallback strategies (alternative approaches when primary methods fail). Crashing (A), ignoring errors (C), and always escalating (D) are not robust patterns. Good systems degrade gracefully and recover when possible.

### Q10. Answer: B
**Explanation**: Logging is crucial for debugging agent behavior, understanding decision-making, identifying failure patterns, and optimizing performance. Given the multi-step nature of agents, logging each step and decision is essential. It's not optional (A), not just for compliance (C), and shouldn't be avoided (D) despite some cost.

### Q11. Answer: A
**Explanation**: There's often a tradeoff between speed and accuracy/quality. Faster responses might mean fewer reflection iterations, less thorough tool use, or simpler reasoning, potentially reducing quality. Speed and cost don't always move together (B), and the relationship with simplicity (C) varies. Tradeoffs definitely exist (D is wrong).

### Q12. Answer: B
**Explanation**: A golden dataset is a curated set of test examples with known correct answers, used to evaluate agent performance consistently over time. It's a benchmark for testing changes. It's not about cost (A), gold prices (C), or training data (D).

---

## Scoring Guide

Count your correct answers:

- **11-12 correct (92-100%)**: Excellent! You understand practical deployment considerations.
- **9-10 correct (75-83%)**: Good! You grasp most practical concepts.
- **7-8 correct (58-67%)**: Fair. Review Module 4, especially evaluation metrics and architecture.
- **Below 7 (< 58%)**: Needs improvement. Rewatch Module 4 focusing on production practices.

## Key Concepts to Review

If you missed several questions, focus on:

1. **Evaluation Metrics**: F1-score, precision, recall, and when to use each
2. **Hyperparameter Optimization**: Temperature, max tokens, and their effects
3. **Production Architecture**: Separation of concerns, state management
4. **Monitoring**: Success rates, latency, costs, error patterns
5. **Failure Handling**: Graceful degradation, fallback strategies
6. **Logging**: Comprehensive tracking for debugging and optimization
7. **Golden Datasets**: Benchmark testing and quality tracking

## Reflection Questions

After completing the quiz, consider:

1. How would you evaluate success for an agent in your domain?
2. What metrics matter most for your use case?
3. What hyperparameters would you optimize first?
4. How would you architect a production agent system?
5. What failure modes should you plan for?

## Practical Connection

Before the coding exercise, think about:
- What would constitute "success" vs. "failure" for your agent?
- How would you measure quality improvements?
- What logging would help you debug issues?
- What fallback strategies make sense for your domain?

---

**Next Steps**: Complete the evaluation exercise to implement these concepts hands-on!
