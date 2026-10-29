"""
Module 5: Multi-Agent Collaboration Solution
Complete implementation of multi-agent system with various patterns.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field
from enum import Enum
import time


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
    timestamp: float = field(default_factory=time.time)


@dataclass
class Task:
    """A task to be completed by an agent."""
    task_id: str
    description: str
    agent_role: AgentRole
    input_data: Any
    dependencies: List[str] = field(default_factory=list)


class BaseAgent:
    """Base class for all agents."""
    
    def __init__(self, agent_id: str, role: AgentRole):
        """Initialize an agent."""
        self.agent_id = agent_id
        self.role = role
        self.inbox: List[Message] = []
        self.completed_tasks: List[str] = []
        self.message_log: List[Message] = []
    
    def receive_message(self, message: Message):
        """Receive a message from another agent."""
        self.inbox.append(message)
        self.message_log.append(message)
        print(f"  [{self.agent_id}] Received {message.message_type} from {message.sender}")
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """
        Process a task and return results.
        Base implementation - should be overridden by subclasses.
        """
        print(f"  [{self.agent_id}] Processing task: {task.description}")
        self.completed_tasks.append(task.task_id)
        
        return {
            "success": True,
            "task_id": task.task_id,
            "agent_id": self.agent_id,
            "result": "Base implementation"
        }
    
    def send_message(self, recipient: str, content: Any, message_type: str) -> Message:
        """Send a message to another agent."""
        message = Message(
            sender=self.agent_id,
            recipient=recipient,
            content=content,
            message_type=message_type
        )
        print(f"  [{self.agent_id}] Sending {message_type} to {recipient}")
        return message


class ResearchAgent(BaseAgent):
    """Agent specialized in research and information gathering."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.RESEARCHER)
        
        # Mock research database
        self.knowledge_base = {
            "AI coding assistants": {
                "tools": ["GitHub Copilot", "Cursor", "Tabnine", "Amazon Q"],
                "market_size": "$500M in 2024",
                "growth_rate": "45% YoY"
            },
            "machine learning": {
                "trends": ["Deep Learning", "LLMs", "AutoML"],
                "applications": ["NLP", "Computer Vision", "Recommendations"]
            },
            "cloud computing": {
                "leaders": ["AWS", "Azure", "GCP"],
                "trends": ["Serverless", "Edge Computing", "AI/ML Services"]
            }
        }
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """Perform research on a topic."""
        print(f"  [{self.agent_id}] Researching: {task.input_data}")
        
        topic = str(task.input_data)
        
        # Search knowledge base
        findings = None
        for key, value in self.knowledge_base.items():
            if key.lower() in topic.lower():
                findings = value
                break
        
        if not findings:
            findings = {
                "summary": f"General information about {topic}",
                "sources": ["Source A", "Source B"]
            }
        
        self.completed_tasks.append(task.task_id)
        
        return {
            "success": True,
            "task_id": task.task_id,
            "agent_id": self.agent_id,
            "topic": topic,
            "findings": findings,
            "sources_count": len(findings.get("sources", [f"source_{i}" for i in range(3)]))
        }


class AnalyzerAgent(BaseAgent):
    """Agent specialized in data analysis."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.ANALYZER)
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """Analyze data or information."""
        print(f"  [{self.agent_id}] Analyzing data...")
        
        data = task.input_data
        
        # Perform mock analysis
        if isinstance(data, dict) and "findings" in data:
            findings = data["findings"]
            
            # Extract insights
            insights = []
            if "trends" in findings:
                insights.append(f"Key trends identified: {len(findings['trends'])} major trends")
            if "market_size" in findings:
                insights.append(f"Market analysis: {findings['market_size']}")
            if "growth_rate" in findings:
                insights.append(f"Growth projection: {findings['growth_rate']}")
            
            analysis = {
                "insights": insights if insights else ["Data analyzed successfully"],
                "confidence": 0.85,
                "recommendations": ["Continue monitoring", "Expand research"]
            }
        else:
            analysis = {
                "insights": ["General analysis completed"],
                "confidence": 0.75,
                "recommendations": ["Gather more data"]
            }
        
        self.completed_tasks.append(task.task_id)
        
        return {
            "success": True,
            "task_id": task.task_id,
            "agent_id": self.agent_id,
            "analysis": analysis
        }


class WriterAgent(BaseAgent):
    """Agent specialized in content writing."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.WRITER)
    
    def process_task(self, task: Task) -> Dict[str, Any]:
        """Write content based on research and analysis."""
        print(f"  [{self.agent_id}] Writing report...")
        
        data = task.input_data
        
        # Generate report based on input
        report_sections = []
        
        if isinstance(data, dict):
            # Extract information from previous stages
            if "analysis" in data:
                analysis = data["analysis"]
                insights = analysis.get("insights", [])
                
                report_sections.append("# Analysis Report\n")
                report_sections.append("## Key Insights\n")
                for insight in insights:
                    report_sections.append(f"- {insight}\n")
                
                if "recommendations" in analysis:
                    report_sections.append("\n## Recommendations\n")
                    for rec in analysis["recommendations"]:
                        report_sections.append(f"- {rec}\n")
            
            elif "findings" in data:
                findings = data["findings"]
                report_sections.append("# Research Report\n")
                report_sections.append(f"## Topic: {data.get('topic', 'N/A')}\n")
                report_sections.append(f"\n## Findings\n")
                report_sections.append(f"{findings}\n")
        else:
            report_sections.append("# Report\n\nContent based on provided data.\n")
        
        report = "".join(report_sections)
        
        self.completed_tasks.append(task.task_id)
        
        return {
            "success": True,
            "task_id": task.task_id,
            "agent_id": self.agent_id,
            "report": report,
            "word_count": len(report.split())
        }


class OrchestratorAgent(BaseAgent):
    """Agent that coordinates other agents."""
    
    def __init__(self, agent_id: str):
        super().__init__(agent_id, AgentRole.ORCHESTRATOR)
        self.worker_agents: Dict[AgentRole, BaseAgent] = {}
    
    def register_agent(self, agent: BaseAgent):
        """Register a worker agent."""
        self.worker_agents[agent.role] = agent
        print(f"  [{self.agent_id}] Registered {agent.role.value} agent: {agent.agent_id}")
    
    def delegate_task(self, task: Task) -> Dict[str, Any]:
        """Delegate a task to the appropriate worker agent."""
        print(f"  [{self.agent_id}] Delegating task to {task.agent_role.value}")
        
        agent = self.worker_agents.get(task.agent_role)
        if not agent:
            return {
                "success": False,
                "error": f"No agent registered for role {task.agent_role}"
            }
        
        # Send task to agent
        result = agent.process_task(task)
        
        return result
    
    def orchestrate_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """Orchestrate a workflow of multiple tasks."""
        print(f"  [{self.agent_id}] Orchestrating workflow with {len(tasks)} tasks")
        
        results = []
        
        # Simple orchestration: delegate each task
        for task in tasks:
            result = self.delegate_task(task)
            results.append(result)
        
        # Synthesize results
        synthesis = self._synthesize_results(results)
        
        return {
            "success": True,
            "orchestrator": self.agent_id,
            "tasks_completed": len(results),
            "individual_results": results,
            "synthesis": synthesis
        }
    
    def _synthesize_results(self, results: List[Dict]) -> str:
        """Synthesize multiple results into a summary."""
        successful = sum(1 for r in results if r.get("success", False))
        
        synthesis = f"Workflow completed: {successful}/{len(results)} tasks successful. "
        
        # Extract key information
        for result in results:
            if "report" in result:
                synthesis += "Final report generated. "
            elif "analysis" in result:
                synthesis += "Analysis completed. "
            elif "findings" in result:
                synthesis += "Research completed. "
        
        return synthesis


class MultiAgentSystem:
    """Manages a multi-agent system with different collaboration patterns."""
    
    def __init__(self):
        """Initialize the multi-agent system."""
        self.agents: Dict[str, BaseAgent] = {}
        self.message_bus: List[Message] = []
        self.task_results: Dict[str, Any] = {}
    
    def add_agent(self, agent: BaseAgent):
        """Add an agent to the system."""
        self.agents[agent.agent_id] = agent
        print(f"[System] Added agent: {agent.agent_id} ({agent.role.value})")
    
    def _find_agent_by_role(self, role: AgentRole) -> Optional[BaseAgent]:
        """Find an agent by its role."""
        for agent in self.agents.values():
            if agent.role == role:
                return agent
        return None
    
    def execute_sequential_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Execute tasks sequentially (pipeline pattern).
        Each task runs after the previous one completes.
        """
        print("\n[System] Executing Sequential Workflow")
        print("="*60)
        
        results = []
        previous_result = None
        
        for i, task in enumerate(tasks):
            print(f"\nStep {i+1}/{len(tasks)}: {task.description}")
            
            # Use previous result as input if available
            if previous_result:
                task.input_data = previous_result
            
            # Find agent for this task
            agent = self._find_agent_by_role(task.agent_role)
            if not agent:
                print(f"  ERROR: No agent found for role {task.agent_role}")
                continue
            
            # Execute task
            result = agent.process_task(task)
            results.append(result)
            previous_result = result
            
            self.task_results[task.task_id] = result
        
        print(f"\n[System] Sequential workflow completed: {len(results)} tasks")
        
        return {
            "pattern": "sequential",
            "results": results,
            "final_output": results[-1] if results else None
        }
    
    def execute_concurrent_workflow(self, tasks: List[Task]) -> Dict[str, Any]:
        """
        Execute independent tasks concurrently (simulated).
        In production, would use threading or async.
        """
        print("\n[System] Executing Concurrent Workflow")
        print("="*60)
        print(f"Running {len(tasks)} tasks in parallel (simulated)")
        
        results = []
        
        # Simulate concurrent execution
        for i, task in enumerate(tasks):
            print(f"\n[Concurrent Task {i+1}]: {task.description}")
            
            agent = self._find_agent_by_role(task.agent_role)
            if not agent:
                print(f"  ERROR: No agent found for role {task.agent_role}")
                continue
            
            result = agent.process_task(task)
            results.append(result)
            self.task_results[task.task_id] = result
        
        # Combine results
        combined = self._combine_results(results)
        
        print(f"\n[System] Concurrent workflow completed: {len(results)} tasks")
        
        return {
            "pattern": "concurrent",
            "results": results,
            "combined_output": combined
        }
    
    def execute_hierarchical_workflow(self, orchestrator: OrchestratorAgent,
                                     tasks: List[Task]) -> Dict[str, Any]:
        """Execute workflow with hierarchical pattern."""
        print("\n[System] Executing Hierarchical Workflow")
        print("="*60)
        
        # Orchestrator coordinates the workflow
        result = orchestrator.orchestrate_workflow(tasks)
        
        print(f"\n[System] Hierarchical workflow completed")
        print(f"Synthesis: {result.get('synthesis', 'N/A')}")
        
        return result
    
    def _combine_results(self, results: List[Dict]) -> Dict[str, Any]:
        """Combine results from concurrent tasks."""
        combined = {
            "total_tasks": len(results),
            "successful": sum(1 for r in results if r.get("success", False)),
            "all_findings": []
        }
        
        # Aggregate findings
        for result in results:
            if "findings" in result:
                combined["all_findings"].append({
                    "agent": result.get("agent_id"),
                    "findings": result["findings"]
                })
        
        return combined


# Test scenarios
def test_sequential_workflow():
    """Test sequential workflow: Research → Analyze → Write"""
    print("\n" + "="*70)
    print("TEST 1: SEQUENTIAL WORKFLOW (Pipeline)")
    print("="*70)
    
    # Create system and agents
    system = MultiAgentSystem()
    
    researcher = ResearchAgent("researcher_1")
    analyzer = AnalyzerAgent("analyzer_1")
    writer = WriterAgent("writer_1")
    
    system.add_agent(researcher)
    system.add_agent(analyzer)
    system.add_agent(writer)
    
    # Define sequential tasks
    tasks = [
        Task("t1", "Research AI coding assistants", AgentRole.RESEARCHER, 
             "AI coding assistants", []),
        Task("t2", "Analyze research findings", AgentRole.ANALYZER, 
             None, ["t1"]),
        Task("t3", "Write analysis report", AgentRole.WRITER, 
             None, ["t2"]),
    ]
    
    # Execute
    result = system.execute_sequential_workflow(tasks)
    
    # Show final report
    if result["final_output"] and "report" in result["final_output"]:
        print("\n" + "="*60)
        print("FINAL REPORT:")
        print("="*60)
        print(result["final_output"]["report"])


def test_concurrent_workflow():
    """Test concurrent workflow: Multiple researchers work in parallel"""
    print("\n" + "="*70)
    print("TEST 2: CONCURRENT WORKFLOW (Parallel Execution)")
    print("="*70)
    
    # Create system and multiple research agents
    system = MultiAgentSystem()
    
    researcher1 = ResearchAgent("researcher_1")
    researcher2 = ResearchAgent("researcher_2")
    researcher3 = ResearchAgent("researcher_3")
    
    system.add_agent(researcher1)
    system.add_agent(researcher2)
    system.add_agent(researcher3)
    
    # Define concurrent tasks
    tasks = [
        Task("t1", "Research AI coding tools", AgentRole.RESEARCHER, 
             "AI coding assistants", []),
        Task("t2", "Research machine learning trends", AgentRole.RESEARCHER, 
             "machine learning", []),
        Task("t3", "Research cloud computing", AgentRole.RESEARCHER, 
             "cloud computing", []),
    ]
    
    # Execute
    result = system.execute_concurrent_workflow(tasks)
    
    print("\n" + "="*60)
    print("COMBINED RESULTS:")
    print("="*60)
    print(f"Total findings collected: {len(result['combined_output']['all_findings'])}")


def test_hierarchical_workflow():
    """Test hierarchical workflow: Orchestrator coordinates specialized agents"""
    print("\n" + "="*70)
    print("TEST 3: HIERARCHICAL WORKFLOW (Orchestrator Pattern)")
    print("="*70)
    
    # Create system and agents
    system = MultiAgentSystem()
    
    orchestrator = OrchestratorAgent("orchestrator_1")
    researcher = ResearchAgent("researcher_1")
    analyzer = AnalyzerAgent("analyzer_1")
    writer = WriterAgent("writer_1")
    
    # Register workers with orchestrator
    orchestrator.register_agent(researcher)
    orchestrator.register_agent(analyzer)
    orchestrator.register_agent(writer)
    
    system.add_agent(orchestrator)
    system.add_agent(researcher)
    system.add_agent(analyzer)
    system.add_agent(writer)
    
    # Define tasks for orchestrator to manage
    tasks = [
        Task("t1", "Research AI trends", AgentRole.RESEARCHER, 
             "machine learning", []),
        Task("t2", "Analyze findings", AgentRole.ANALYZER, 
             {"findings": {"trends": ["LLMs", "AutoML"]}}, []),
        Task("t3", "Write report", AgentRole.WRITER, 
             {"analysis": {"insights": ["Growing adoption"]}}, []),
    ]
    
    # Execute through orchestrator
    result = system.execute_hierarchical_workflow(orchestrator, tasks)
    
    print("\n" + "="*60)
    print("ORCHESTRATION SUMMARY:")
    print("="*60)
    print(f"Tasks completed: {result['tasks_completed']}")
    print(f"Synthesis: {result['synthesis']}")


def main():
    """Run all multi-agent system tests."""
    print("="*70)
    print("MULTI-AGENT COLLABORATION SOLUTION DEMO")
    print("="*70)
    
    # Run all tests
    test_sequential_workflow()
    test_concurrent_workflow()
    test_hierarchical_workflow()
    
    print("\n" + "="*70)
    print("ALL TESTS COMPLETED")
    print("="*70)
    print("\nKey Takeaways:")
    print("1. Sequential: Good for dependent tasks, data flows through pipeline")
    print("2. Concurrent: Faster for independent tasks, results combined at end")
    print("3. Hierarchical: Orchestrator coordinates, good for complex workflows")
    print("\nChoose pattern based on task dependencies and coordination needs!")


if __name__ == "__main__":
    main()
