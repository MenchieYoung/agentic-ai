# Module 5: Multi-Agent Collaboration Exercise

## Objective
Build a multi-agent system demonstrating different collaboration patterns: sequential, concurrent, and hierarchical orchestration.

## Learning Goals
By completing this exercise, you will:
- Design specialized agents with distinct roles
- Implement sequential orchestration (pipeline pattern)
- Implement concurrent execution for independent tasks
- Implement hierarchical coordination with an orchestrator
- Handle inter-agent communication and state management
- Understand tradeoffs between different patterns

## Scenario
You're building a research automation system with multiple specialized agents:
- **Research Agent**: Gathers information on topics
- **Analyzer Agent**: Processes and analyzes data
- **Writer Agent**: Creates reports and summaries
- **Orchestrator Agent**: Coordinates the workflow

## Task Requirements

### Part 1: Base Agent Classes (Required)
Create a base agent with:
- Agent ID and role
- Message inbox for receiving communications
- Task processing capability
- Message sending/receiving methods

Create specialized agent classes:
- `ResearchAgent`: Searches for information
- `AnalyzerAgent`: Analyzes findings
- `WriterAgent`: Creates written output
- `OrchestratorAgent`: Coordinates others

### Part 2: Sequential Workflow (Required)
Implement a pipeline where:
1. Research agent gathers information
2. Passes results to analyzer agent
3. Analyzer processes and passes to writer
4. Writer produces final report

Example: "Research Python → Analyze trends → Write summary"

### Part 3: Concurrent Workflow (Required)
Implement parallel execution where:
1. Multiple agents work on different subtasks simultaneously
2. Results are collected and combined
3. Faster than sequential for independent tasks

Example: Three research agents investigate different topics in parallel

### Part 4: Hierarchical Workflow (Required)
Implement coordinator pattern where:
1. Orchestrator receives complex task
2. Breaks it into subtasks
3. Delegates to specialized agents
4. Synthesizes results into final output

Example: Orchestrator manages "Create market analysis report"

### Part 5: Extensions (Optional)
- Implement blackboard pattern (shared memory space)
- Add peer-to-peer communication
- Implement retry and fallback mechanisms
- Add agent monitoring and logging
- Create a visual workflow representation

## Starter Code Structure

```python
class BaseAgent:
    def __init__(self, agent_id, role):
        self.agent_id = agent_id
        self.role = role
        self.inbox = []
    
    def receive_message(self, message):
        # TODO
        pass
    
    def process_task(self, task):
        # TODO
        pass
    
    def send_message(self, recipient, content, msg_type):
        # TODO
        pass

class MultiAgentSystem:
    def __init__(self):
        self.agents = {}
    
    def execute_sequential_workflow(self, tasks):
        # TODO
        pass
    
    def execute_concurrent_workflow(self, tasks):
        # TODO
        pass
    
    def execute_hierarchical_workflow(self, orchestrator, tasks):
        # TODO
        pass
```

## Test Scenarios

### Scenario 1: Market Research Report (Sequential)
```
Task: "Create a market analysis report for AI coding assistants"

Workflow:
1. Research Agent: Gather data on AI coding tools
2. Analyzer Agent: Identify trends and patterns
3. Writer Agent: Create formatted report

Expected: Complete report with data and analysis
```

### Scenario 2: Competitive Analysis (Concurrent)
```
Task: "Analyze three competing products simultaneously"

Workflow:
1. Three Research Agents (parallel): Each investigates one product
2. Combine results
3. Analyzer Agent: Compare findings

Expected: Faster than sequential, combined analysis
```

### Scenario 3: Complex Project (Hierarchical)
```
Task: "Comprehensive industry report"

Workflow:
1. Orchestrator: Breaks into subtasks
   - Market size research
   - Competitor analysis
   - Trend prediction
2. Delegates to specialized agents
3. Synthesizes into cohesive report

Expected: Well-coordinated multi-aspect report
```

## Implementation Tips

### Message Passing

```python
@dataclass
class Message:
    sender: str
    recipient: str
    content: Any
    message_type: str  # "task", "result", "query"

# Usage
msg = Message(
    sender="research_agent_1",
    recipient="analyzer_agent_1",
    content={"findings": [...], "sources": [...]},
    message_type="result"
)
```

### Task Dependencies

```python
@dataclass
class Task:
    task_id: str
    description: str
    agent_role: AgentRole
    input_data: Any
    dependencies: List[str] = None  # Tasks that must complete first

# Sequential dependencies
task1 = Task("t1", "Research", AgentRole.RESEARCHER, "AI tools", [])
task2 = Task("t2", "Analyze", AgentRole.ANALYZER, None, ["t1"])
task3 = Task("t3", "Write", AgentRole.WRITER, None, ["t2"])
```

### Mock Implementation for Learning

```python
class ResearchAgent(BaseAgent):
    def process_task(self, task):
        # Mock research
        topic = task.input_data
        return {
            "success": True,
            "findings": f"Mock research findings about {topic}",
            "sources": ["source1", "source2"],
            "agent": self.agent_id
        }

class AnalyzerAgent(BaseAgent):
    def process_task(self, task):
        # Mock analysis
        data = task.input_data
        return {
            "success": True,
            "analysis": f"Analysis of: {data}",
            "trends": ["trend1", "trend2"],
            "agent": self.agent_id
        }
```

### Sequential Execution

```python
def execute_sequential_workflow(self, tasks):
    results = []
    previous_result = None
    
    for task in tasks:
        # Use previous result as input
        if previous_result:
            task.input_data = previous_result
        
        # Find agent for this task
        agent = self._find_agent_by_role(task.agent_role)
        
        # Execute task
        result = agent.process_task(task)
        results.append(result)
        previous_result = result
    
    return {"results": results, "final": results[-1]}
```

### Concurrent Execution (Simulated)

```python
def execute_concurrent_workflow(self, tasks):
    # In real implementation, use threading or async
    # For exercise, simulate by executing all then combining
    
    results = []
    for task in tasks:
        agent = self._find_agent_by_role(task.agent_role)
        result = agent.process_task(task)
        results.append(result)
    
    # Combine results
    combined = self._combine_results(results)
    return {"results": results, "combined": combined}
```

### Hierarchical Coordination

```python
class OrchestratorAgent(BaseAgent):
    def orchestrate_workflow(self, main_task):
        # 1. Break down task
        subtasks = self._decompose_task(main_task)
        
        # 2. Delegate to specialists
        subtask_results = []
        for subtask in subtasks:
            agent = self.worker_agents[subtask.agent_role]
            result = agent.process_task(subtask)
            subtask_results.append(result)
        
        # 3. Synthesize results
        final_output = self._synthesize(subtask_results)
        
        return final_output
```

## Testing Your Implementation

Test each pattern with:

1. **Correctness**: Do tasks complete in right order?
2. **Data Flow**: Is information passed correctly between agents?
3. **Error Handling**: What if an agent fails?
4. **Performance**: Is concurrent faster for independent tasks?

## Success Criteria

Your implementation should:
- ✅ Create at least 4 specialized agent types
- ✅ Implement sequential workflow (pipeline)
- ✅ Implement concurrent workflow (parallel)
- ✅ Implement hierarchical workflow (orchestration)
- ✅ Handle inter-agent communication
- ✅ Pass results between agents correctly
- ✅ Include clear documentation

## Common Pitfalls

1. **Not handling dependencies**: Tasks may run in wrong order
2. **Lost messages**: Ensure messages reach recipients
3. **State management**: Track which tasks completed
4. **No error handling**: One agent failure shouldn't crash system
5. **Tight coupling**: Agents should be independent, loosely coupled

## Reflection Questions

1. When would you choose sequential vs. concurrent execution?
2. What's the overhead of having an orchestrator vs. direct P2P?
3. How would you handle conflicting results from multiple agents?
4. What failure scenarios should you plan for?
5. How does multi-agent complexity scale with agent count?

## Time Estimate
- Part 1: 45-60 minutes
- Part 2: 30-40 minutes
- Part 3: 30-40 minutes
- Part 4: 40-50 minutes
- Part 5 (optional): 60+ minutes

## Next Steps
After completing:
1. Compare your solution with provided solution
2. Try implementing a blackboard pattern
3. Add real async/threading for true concurrency
4. Build a practical multi-agent application

---

**Good luck! Focus on understanding how agents collaborate and coordinate.**
