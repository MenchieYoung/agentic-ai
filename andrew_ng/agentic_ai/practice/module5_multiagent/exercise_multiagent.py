"""
Module 5: Multi-Agent Collaboration Exercise
Build a multi-agent system with different collaboration patterns.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum


class AgentRole(Enum):
    """Define different agent roles."""
    ORCHESTRATOR = "orchestrator"
    RESEARCHER = "researcher"
    ANALYZER = "analyzer"
    WRITER = "writer"
    REVIEWER = "reviewer"


@dataclass
class Message:
    """Message passed between agents."""
    sender: str
    recipient: str
    content: Any
    message_type: str  # "task", "result", "query", etc.


@dataclass
class Task:
    """A task to be completed by an agent."""
    task_id: str
    description: str
    agent_role: AgentRole
    input_data: Any
    dependencies: List[str] = None  # List of task_ids that must complete first


class BaseAgent:
    """Base class for all agents."""
    
    def __init__(self, agent_id: str, role: AgentRole):
        """
        Initialize an agent.
        
        TODO: Add any other initialization you need
        """
        self.agent_id = agent_id
        self.role = role
        self.inbox: List[Message] = []
        self.completed_tasks: List[str] = []
    
    def receive_message(self, message: Message):
        """
        Receive a message from another agent.
        
        TODO: Implement message receiving
        """
        pass
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """
        Process a task and return results.
        
        TODO: Implement task processing
        Hint: Different agent types will override this
        """
        pass
    
    def send_message(self, recipient: str, content: Any, message_type: str) -> Message:
        """
        Send a message to another agent.
        
        TODO: Implement message sending
        """
        pass


# TODO: Implement specialized agent classes
class ResearchAgent(BaseAgent):
    """Agent specialized in research and information gathering."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.RESEARCHER)
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """
        Perform research on a topic.
        
        TODO: Implement research logic
        Hint: For this exercise, use mock research results
        """
        pass


class AnalyzerAgent(BaseAgent):
    """Agent specialized in data analysis."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.ANALYZER)
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """
        Analyze data or information.
        
        TODO: Implement analysis logic
        """
        pass


class WriterAgent(BaseAgent):
    """Agent specialized in content writing."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.WRITER)
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """
        Write content based on research and analysis.
        
        TODO: Implement writing logic
        """
        pass


class OrchestratorAgent(BaseAgent):
    """Agent that coordinates other agents."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.ORCHESTRATOR)
        self.worker_agents: Dict[AgentRole, BaseAgent] = {}
    
    def register_agent(self, agent: BaseAgent):
        """
        Register a worker agent.
        
        TODO: Implement agent registration
        """
        pass
    
    def delegate_task(self, task: Task) -> Dict[str, Any]:
        """
        Delegate a task to the appropriate worker agent.
        
        TODO: Implement task delegation
        Steps:
        1. Identify which agent should handle this task
        2. Send task to that agent
        3. Collect results
        4. Return results
        """
        pass
    
    def orchestrate_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Orchestrate a workflow of multiple tasks.
        
        TODO: Implement workflow orchestration
        Steps:
        1. Determine task dependencies
        2. Execute tasks in correct order
        3. Handle sequential and concurrent execution
        4. Collect and synthesize results
        """
        pass


class MultiAgentSystem:
    """Manages a multi-agent system with different collaboration patterns."""
    
    def __init__(self):
        """
        Initialize the multi-agent system.
        
        TODO: Set up agents and communication infrastructure
        """
        self.agents: Dict[str, BaseAgent] = {}
        self.message_bus: List[Message] = []
        self.task_results: Dict[str, Any] = {}
    
    def add_agent(self, agent: BaseAgent):
        """
        Add an agent to the system.
        
        TODO: Implement agent addition
        """
        pass
    
    def execute_sequential_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Execute tasks sequentially (pipeline pattern).
        
        Args:
            tasks: List of tasks in order of execution
            
        Returns:
            Results from all tasks
            
        TODO: Implement sequential execution
        Each task runs after the previous one completes
        Output from one task can feed into the next
        """
        pass
    
    def execute_concurrent_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Execute independent tasks concurrently.
        
        Args:
            tasks: List of independent tasks
            
        Returns:
            Combined results from all tasks
            
        TODO: Implement concurrent execution
        Hint: For this exercise, simulate concurrency
        """
        pass
    
    def execute_hierarchical_workflow(self, orchestrator: OrchestratorAgent, 
                                     tasks: List[Task]) -> Dict[str, Any]:
        """
        Execute workflow with hierarchical pattern.
        
        Args:
            orchestrator: The coordinating agent
            tasks: Tasks to be delegated
            
        Returns:
            Synthesized results
            
        TODO: Implement hierarchical execution
        The orchestrator delegates to specialized agents
        """
        pass


# Test scenarios
def test_sequential_workflow():
    """
    Test sequential workflow: Research → Analyze → Write
    
    TODO: Implement test
    Create a workflow where:
    1. Research agent gathers information
    2. Analyzer agent processes it
    3. Writer agent creates a report
    """
    pass


def test_concurrent_workflow():
    """
    Test concurrent workflow: Multiple researchers work in parallel
    
    TODO: Implement test
    Create a workflow where:
    1. Multiple research agents work on different topics simultaneously
    2. Results are combined
    """
    pass


def test_hierarchical_workflow():
    """
    Test hierarchical workflow: Orchestrator coordinates specialized agents
    
    TODO: Implement test
    Create a workflow where:
    1. Orchestrator receives a complex task
    2. Breaks it down and delegates to specialists
    3. Synthesizes results
    """
    pass


def main():
    """Test the multi-agent system."""
    print("=== Multi-Agent Collaboration Exercise ===\n")
    
    # TODO: Create and test your multi-agent system
    
    # Test 1: Sequential workflow
    print("Test 1: Sequential Workflow")
    print("-" * 50)
    # test_sequential_workflow()
    # print()
    
    # Test 2: Concurrent workflow
    print("Test 2: Concurrent Workflow")
    print("-" * 50)
    # test_concurrent_workflow()
    # print()
    
    # Test 3: Hierarchical workflow
    print("Test 3: Hierarchical Workflow")
    print("-" * 50)
    # test_hierarchical_workflow()
    # print()


if __name__ == "__main__":
    main()
