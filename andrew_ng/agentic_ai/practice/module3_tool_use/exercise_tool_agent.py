"""
Module 3: Tool-Using Agent Exercise
Build an agent that can use external tools to accomplish tasks.
"""

from typing import Dict, List, Any, Optional
import re


class Tool:
    """Base class for tools that agents can use."""
    
    def __init__(self, name: str, description: str, parameters: Dict[str, str]):
        """
        Initialize a tool.
        
        Args:
            name: Tool identifier
            description: What the tool does (used by agent for selection)
            parameters: Dict of parameter_name: parameter_description
        """
        self.name = name
        self.description = description
        self.parameters = parameters
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        """
        Execute the tool with given parameters.
        
        Returns:
            Dictionary with results or error information
        """
        raise NotImplementedError("Subclasses must implement execute()")


# TODO: Implement these tool classes
class WebSearchTool(Tool):
    """Tool for searching the web."""
    
    def __init__(self):
        # TODO: Define name, description, and parameters
        pass
    
    def execute(self, query: str) -> Dict[str, Any]:
        """
        Search the web for information.
        
        TODO: Implement mock search
        Hint: Create a dictionary of mock results for common queries
        """
        pass


class CalculatorTool(Tool):
    """Tool for mathematical calculations."""
    
    def __init__(self):
        # TODO: Define name, description, and parameters
        pass
    
    def execute(self, expression: str) -> Dict[str, Any]:
        """
        Evaluate a mathematical expression.
        
        TODO: Implement calculator
        Hint: Use eval() carefully, or implement basic arithmetic
        """
        pass


class GetTimeTool(Tool):
    """Tool for getting current date/time."""
    
    def __init__(self):
        # TODO: Define name, description, and parameters
        pass
    
    def execute(self) -> Dict[str, Any]:
        """
        Get current date and time.
        
        TODO: Implement time retrieval
        Hint: Use datetime module
        """
        pass


class SaveNoteTool(Tool):
    """Tool for saving notes to files."""
    
    def __init__(self):
        # TODO: Define name, description, and parameters
        pass
    
    def execute(self, content: str, filename: str) -> Dict[str, Any]:
        """
        Save content to a file.
        
        TODO: Implement file saving
        Hint: For this exercise, just mock it (return success message)
        """
        pass


class ToolUsingAgent:
    """An agent that can use tools to accomplish tasks."""
    
    def __init__(self):
        """Initialize the agent and register tools."""
        self.tools: Dict[str, Tool] = {}
        self._register_tools()
    
    def _register_tools(self):
        """
        Register all available tools.
        
        TODO: Implement tool registration
        Create instances of each tool and add to self.tools dict
        """
        pass
    
    def select_tool(self, user_request: str) -> Optional[Tool]:
        """
        Select the most appropriate tool for the user's request.
        
        Args:
            user_request: The user's natural language request
            
        Returns:
            The selected Tool object, or None if no tool needed
            
        TODO: Implement tool selection logic
        Hints:
        - Look for keywords in the request
        - Match keywords to tool purposes
        - Handle ambiguous cases
        """
        pass
    
    def extract_parameters(self, user_request: str, tool: Tool) -> Dict[str, Any]:
        """
        Extract parameters from the user request for a specific tool.
        
        Args:
            user_request: The user's request
            tool: The tool that will be called
            
        Returns:
            Dictionary of parameter_name: value
            
        TODO: Implement parameter extraction
        Hints:
        - Use regex for extracting expressions or numbers
        - Look for patterns like "search for X"
        - Handle different phrasings
        """
        pass
    
    def execute_tool(self, tool_name: str, **parameters) -> Dict[str, Any]:
        """
        Execute a tool with given parameters.
        
        Args:
            tool_name: Name of the tool to execute
            **parameters: Parameters to pass to the tool
            
        Returns:
            Tool execution results
            
        TODO: Implement tool execution with error handling
        Hints:
        - Check if tool exists
        - Try to execute and catch exceptions
        - Return structured results
        """
        pass
    
    def process_request(self, user_request: str) -> str:
        """
        Process a user request end-to-end.
        
        Args:
            user_request: The user's natural language request
            
        Returns:
            Agent's response string
            
        TODO: Implement the main workflow
        Steps:
        1. Select appropriate tool
        2. Extract parameters
        3. Execute tool
        4. Format response based on results
        5. Handle multi-tool requests (optional)
        """
        pass
    
    def list_tools(self) -> str:
        """
        List all available tools and their descriptions.
        
        Returns:
            Formatted string of available tools
        """
        if not self.tools:
            return "No tools available."
        
        result = "Available tools:\n"
        for tool in self.tools.values():
            result += f"\n{tool.name}:\n"
            result += f"  Description: {tool.description}\n"
            result += f"  Parameters: {tool.parameters}\n"
        return result


def main():
    """Test the ToolUsingAgent implementation."""
    print("=== Tool-Using Agent Exercise ===\n")
    
    # TODO: Create the agent
    agent = ToolUsingAgent()
    
    # TODO: List available tools
    # print(agent.list_tools())
    # print()
    
    # Test cases
    test_cases = [
        "What's 156 * 89?",
        "Search for the capital of France",
        "What time is it?",
        "Save a note saying 'Meeting at 3pm' to reminder.txt",
        "What is 25 + 37?",
        "Find information about Python programming",
    ]
    
    # TODO: Process each test case
    # for request in test_cases:
    #     print(f"User: {request}")
    #     response = agent.process_request(request)
    #     print(f"Agent: {response}")
    #     print()


if __name__ == "__main__":
    main()
