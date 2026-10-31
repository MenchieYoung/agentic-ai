# Module 5 Quiz: Multi-Agent Collaboration

> ⚠️ **DISCLAIMER: AI-Generated Study Aid**
> 
> This quiz was created by AI as a study aid based on the local transcript-based notes.
> **These are not DeepLearning.AI course quiz questions.** No quiz-question files were found in the mirrored learner repositories.
> 
> Use these questions to:
> - Test your understanding of the local notes
> - Identify concepts to review
> - Prepare for coding exercises
> 
> Use the [official DeepLearning.AI course](https://learn.deeplearning.ai/courses/agentic-ai/information) for its current assessments.

## Instructions
- This quiz contains 13 multiple-choice questions
- Each question has one correct answer
- Answer all questions before checking the answer key
- Passing score: 70% (10/13 correct)

---

## Questions

### Q1. What is the primary benefit of using multiple agents instead of a single complex agent?
A) It's always faster  
B) Modularity, specialization, and easier debugging  
C) It costs less  
D) It requires less code

### Q2. In a sequential orchestration pattern, how do agents typically interact?
A) All agents run simultaneously  
B) One agent completes its task, passes results to the next agent  
C) Agents compete to solve the problem  
D) Agents vote on the best solution

### Q3. What is concurrent dialogue in multi-agent systems?
A) Multiple agents talking to users at the same time  
B) Multiple agents working on different aspects of a problem simultaneously  
C) Agents interrupting each other  
D) Running the same agent multiple times

### Q4. Which communication pattern involves a central coordinator that delegates tasks to specialized agents?
A) Peer-to-peer  
B) Blackboard  
C) Hierarchical  
D) Democratic

### Q5. In a hierarchical multi-agent system, what is the role of the "orchestrator" or "manager" agent?
A) To perform all the actual work  
B) To coordinate, delegate, and synthesize results from specialized agents  
C) To monitor system performance only  
D) To handle user authentication

### Q6. What is the "blackboard" pattern in multi-agent collaboration?
A) A shared workspace where agents read and write information  
B) A type of user interface  
C) A debugging tool  
D) A storage system for training data

### Q7. In the customer service pipeline example, what might be the role of a "routing agent"?
A) To handle all customer requests directly  
B) To determine which specialized agent should handle a request  
C) To close tickets  
D) To send emails to customers

### Q8. What is a key challenge in multi-agent systems compared to single-agent systems?
A) They always fail  
B) Coordinating communication and managing state across agents  
C) They can't use tools  
D) They don't work with LLMs

### Q9. In a research team multi-agent system, what might different agents specialize in?
A) All agents do the same thing for redundancy  
B) Literature search, data analysis, and report writing  
C) Only data collection  
D) Only report formatting

### Q10. What is an advantage of the peer-to-peer (P2P) communication pattern?
A) It's the simplest to implement  
B) Agents can collaborate directly without always going through a central coordinator  
C) It eliminates the need for coordination  
D) It works only with two agents

### Q11. When should you consider using concurrent execution in a multi-agent system?
A) Never, sequential is always better  
B) When tasks are independent and can be done in parallel to save time  
C) Only for simple tasks  
D) When you have only one agent

### Q12. What is a common pattern for handling failures in multi-agent systems?
A) Crash the entire system immediately  
B) Have fallback agents or retry mechanisms  
C) Ignore errors and continue  
D) Always escalate to humans

### Q13. In a multi-agent workflow, how is context typically shared between agents?
A) Agents never share information  
B) Through shared state, message passing, or a central datastore  
C) Through the internet  
D) Context sharing is impossible

---

## Answer Key

### Q1. Answer: B
**Explanation**: The primary benefit of multi-agent systems is modularity (separating concerns), specialization (each agent excels at specific tasks), and easier debugging (isolate problems to specific agents). While multi-agent systems can sometimes be faster (A) or use less code (D), these aren't the primary benefits. Cost (C) varies depending on implementation.

### Q2. Answer: B
**Explanation**: Sequential orchestration means agents work one after another in a pipeline: Agent 1 completes its task and passes results to Agent 2, which then completes its task and passes to Agent 3, etc. This is different from concurrent execution (A), competition (C), or voting (D).

### Q3. Answer: B
**Explanation**: Concurrent dialogue means multiple agents work on different aspects of a problem at the same time, then their results are combined. For example, one agent researches while another analyzes data, happening in parallel. It's not about talking to users simultaneously (A), interrupting (C), or duplication (D).

### Q4. Answer: C
**Explanation**: The hierarchical pattern features a central coordinator (manager/orchestrator) that delegates tasks to specialized worker agents. Peer-to-peer (A) has no central authority, blackboard (B) uses shared memory, and democratic (D) isn't a standard pattern discussed in the course.

### Q5. Answer: B
**Explanation**: In hierarchical systems, the orchestrator/manager agent coordinates the workflow by delegating tasks to specialized agents, collecting their results, and synthesizing a final answer. It doesn't do all the work itself (A), just monitor (C), or handle auth (D).

### Q6. Answer: A
**Explanation**: The blackboard pattern is a shared workspace (memory space) where multiple agents can read information posted by other agents and write their own contributions. It's a collaboration model, not a UI (B), debugging tool (C), or training storage (D).

### Q7. Answer: B
**Explanation**: A routing agent's role is to analyze incoming requests and determine which specialized agent (billing, technical support, account management, etc.) should handle each request. It doesn't handle requests directly (A), close tickets (C), or send emails (D) - specialized agents do those tasks.

### Q8. Answer: B
**Explanation**: A key challenge in multi-agent systems is coordinating communication between agents and managing shared state, which is more complex than in single-agent systems. Multi-agent systems don't always fail (A), they can use tools (C), and they work well with LLMs (D).

### Q9. Answer: B
**Explanation**: In a research team, different agents would specialize in different aspects of research: one for literature search, one for data analysis, one for synthesis and writing, etc. This specialization is more effective than all doing the same thing (A) or focusing on only one narrow task (C, D).

### Q10. Answer: B
**Explanation**: In P2P patterns, agents can collaborate and communicate directly with each other without every message going through a central coordinator, allowing for more flexible collaboration. It's not the simplest (A), coordination is still needed (C), and it works with many agents (D).

### Q11. Answer: B
**Explanation**: Concurrent execution is valuable when you have independent tasks that can run in parallel, reducing total time. For example, searching multiple databases at once. Sequential is not always better (A), concurrency helps with both simple and complex tasks (C), and you need multiple agents by definition (D).

### Q12. Answer: B
**Explanation**: Common failure handling patterns include having fallback agents (if primary agent fails, try another) and retry mechanisms (try again with adjusted parameters). Crashing immediately (A), ignoring errors (C), and always escalating (D) are not robust patterns.

### Q13. Answer: B
**Explanation**: Context is shared through mechanisms like shared state (variables accessible to all agents), message passing (agents send context to each other), or a central datastore (database or blackboard). Agents definitely share information (A), this is not about internet access (C), and sharing is definitely possible (D).

---

## Scoring Guide

Count your correct answers:

- **12-13 correct (92-100%)**: Excellent! You understand multi-agent patterns deeply.
- **10-11 correct (77-85%)**: Good! You grasp the core concepts well.
- **8-9 correct (62-69%)**: Fair. Review Module 5, especially communication patterns.
- **Below 8 (< 62%)**: Needs improvement. Rewatch Module 5 with focus on examples.

## Key Concepts to Review

If you missed several questions, focus on:

1. **Orchestration Patterns**: Sequential vs. Concurrent execution
2. **Communication Patterns**: Hierarchical, P2P, Blackboard
3. **Benefits**: Modularity, specialization, easier debugging
4. **Challenges**: Coordination, state management
5. **Practical Applications**: Customer service, research teams
6. **Failure Handling**: Fallbacks and retry mechanisms
7. **Context Sharing**: Message passing, shared state, central storage

## Reflection Questions

After completing the quiz, consider:

1. When would you choose a hierarchical vs. peer-to-peer pattern?
2. What tasks in your domain could benefit from agent specialization?
3. How would you debug a failure in a multi-agent system?
4. When is the added complexity of multiple agents justified?
5. How would you handle conflicting outputs from different agents?

## Practical Connection

Before moving to the coding exercise, think about:
- What agents would you need for your use case?
- How would they communicate?
- What would each agent specialize in?
- How would you coordinate their work?
- What failure modes should you plan for?

---

**Next Steps**: Complete the multi-agent collaboration coding exercise to implement these concepts hands-on!
