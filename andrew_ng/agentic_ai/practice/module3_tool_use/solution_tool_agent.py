"""
Module 3: Tool-Using Agent Solution
A complete implementation of a tool-using agent with multiple tools.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import re


class Tool:
    """Base class for tools that agents can use."""
    
    def __init__(self, name: str, description: str, parameters: Dict[str, str]):
        self.name = name
        self.description = description
        self.parameters = parameters
    
    def execute(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement execute()")


class WebSearchTool(Tool):
    """Tool for searching the web (mock implementation)."""
    
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Search the web for information on any topic",
            parameters={"query": "string - the search query"}
        )
        
        # Mock search database
        self.mock_data = {
            "capital of france": "Paris is the capital and largest city of France.",
            "python programming": "Python is a high-level programming language known for its simplicity and readability.",
            "population of tokyo": "Tokyo has a population of approximately 14 million people in the city proper, and about 37 million in the greater metropolitan area.",
            "eiffel tower": "The Eiffel Tower is a wrought-iron lattice tower in Paris, France. Built in 1889, it's one of the most famous landmarks in the world.",
        }
    
    def execute(self, query: str) -> Dict[str, Any]:
        """Search for information."""
        query_lower = query.lower()
        
        # Find best match
        for key, value in self.mock_data.items():
            if key in query_lower or query_lower in key:
                return {
                    "success": True,
                    "query": query,
                    "result": value,
                    "source": "Mock Search Engine"
                }
        
        return {
            "success": True,
            "query": query,
            "result": f"Search results for '{query}' (mock result)",
            "source": "Mock Search Engine"
        }


class CalculatorTool(Tool):
    """Tool for mathematical calculations."""
    
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Evaluate mathematical expressions (supports +, -, *, /, parentheses)",
            parameters={"expression": "string - the mathematical expression to evaluate"}
        )
    
    def execute(self, expression: str) -> Dict[str, Any]:
        """Evaluate a mathematical expression."""
        try:
            # Clean the expression
            expression = expression.strip()
            
            # Safe evaluation (restricted namespace)
            # In production, use ast.literal_eval or a proper math parser
            allowed_chars = set('0123456789+-*/()., ')
            if not all(c in allowed_chars for c in expression):
                return {
                    "success": False,
                    "error": "Expression contains invalid characters"
                }
            
            result = eval(expression, {"__builtins__": {}}, {})
            
            return {
                "success": True,
                "expression": expression,
                "result": result
            }
        except ZeroDivisionError:
            return {"success": False, "error": "Division by zero"}
        except Exception as e:
            return {"success": False, "error": f"Calculation error: {str(e)}"}


class GetTimeTool(Tool):
    """Tool for getting current date/time."""
    
    def __init__(self):
        super().__init__(
            name="get_time",
            description="Get the current date and time",
            parameters={}
        )
    
    def execute(self) -> Dict[str, Any]:
        """Get current date and time."""
        now = datetime.now()
        return {
            "success": True,
            "datetime": now.isoformat(),
            "formatted": now.strftime("%A, %B %d, %Y at %I:%M %p"),
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S")
        }


class SaveNoteTool(Tool):
    """Tool for saving notes to files (mock implementation)."""
    
    def __init__(self):
        super().__init__(
            name="save_note",
            description="Save a note or content to a file",
            parameters={
                "content": "string - the content to save",
                "filename": "string - the name of the file"
            }
        )
        self.saved_notes = {}  # Mock storage
    
    def execute(self, content: str, filename: str) -> Dict[str, Any]:
        """Save content to a file (mocked)."""
        try:
            # In a real implementation, write to actual file
            # For this exercise, store in memory
            self.saved_notes[filename] = content
            
            return {
                "success": True,
                "filename": filename,
                "message": f"Successfully saved note to {filename}",
                "size": len(content)
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to save note: {str(e)}"
            }


class ToolUsingAgent:
    """An agent that can use tools to accomplish tasks."""
    
    def __init__(self):
        """Initialize the agent and register tools."""
        self.tools: Dict[str, Tool] = {}
        self._register_tools()
        self.conversation_history = []
    
    def _register_tools(self):
        """Register all available tools."""
        tools = [
            WebSearchTool(),
            CalculatorTool(),
            GetTimeTool(),
            SaveNoteTool()
        ]
        
        for tool in tools:
            self.tools[tool.name] = tool
    
    def select_tool(self, user_request: str) -> Optional[Tool]:
        """Select the most appropriate tool for the request."""
        request_lower = user_request.lower()
        
        # Calculator keywords
        calc_keywords = ['calculate', 'compute', 'what is', 'what\'s', 'multiply', 
                        'divide', 'add', 'subtract', 'plus', 'minus', 'times']
        # Check for mathematical operators
        has_math = any(op in request_lower for op in ['*', '+', '-', '/', '×', '÷'])
        has_numbers = bool(re.search(r'\d', request_lower))
        
        if (has_math and has_numbers) or any(kw in request_lower for kw in calc_keywords):
            # Check if it's actually a calculation request
            if 'search' not in request_lower and 'find' not in request_lower:
                return self.tools.get('calculator')
        
        # Time keywords
        time_keywords = ['what time', 'current time', 'date', 'what day', 'time is it']
        if any(kw in request_lower for kw in time_keywords):
            return self.tools.get('get_time')
        
        # Save note keywords
        save_keywords = ['save', 'write', 'create note', 'save note']
        if any(kw in request_lower for kw in save_keywords):
            return self.tools.get('save_note')
        
        # Search keywords (default for information requests)
        search_keywords = ['search', 'find', 'look up', 'what is', 'who is', 
                          'where is', 'tell me about', 'information about']
        if any(kw in request_lower for kw in search_keywords):
            return self.tools.get('web_search')
        
        return None
    
    def extract_parameters(self, user_request: str, tool: Tool) -> Dict[str, Any]:
        """Extract parameters from the user request for a specific tool."""
        
        if tool.name == 'calculator':
            # Extract mathematical expression
            # Look for numbers and operators
            match = re.search(r'[\d\s+\-*/().]+', user_request)
            if match:
                expression = match.group().strip()
                return {'expression': expression}
            
            # Try to find "what is X" or "what's X"
            match = re.search(r"what'?s?\s+([\d\s+\-*/().]+)", user_request, re.IGNORECASE)
            if match:
                return {'expression': match.group(1).strip()}
            
            return {'expression': user_request}
        
        elif tool.name == 'web_search':
            # Extract search query
            patterns = [
                r'search (?:for |about )?(.+)',
                r'find (?:information about |out about |about )?(.+)',
                r'look up (.+)',
                r'tell me about (.+)',
                r'what is (.+)',
                r'who is (.+)',
            ]
            
            for pattern in patterns:
                match = re.search(pattern, user_request, re.IGNORECASE)
                if match:
                    query = match.group(1).strip()
                    # Clean up the query
                    query = re.sub(r'\?+$', '', query)  # Remove trailing questions marks
                    return {'query': query}
            
            # Default: use the whole request
            return {'query': user_request}
        
        elif tool.name == 'save_note':
            # Extract content and filename
            # Pattern: "save ... to filename"
            match = re.search(r'save\s+(?:a note )?(?:saying )?["\']?(.+?)["\']?\s+to\s+(\S+)', 
                            user_request, re.IGNORECASE)
            if match:
                content = match.group(1).strip()
                filename = match.group(2).strip()
                return {'content': content, 'filename': filename}
            
            # Fallback
            return {'content': user_request, 'filename': 'note.txt'}
        
        elif tool.name == 'get_time':
            # No parameters needed
            return {}
        
        return {}
    
    def execute_tool(self, tool_name: str, **parameters) -> Dict[str, Any]:
        """Execute a tool with given parameters."""
        tool = self.tools.get(tool_name)
        
        if not tool:
            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found"
            }
        
        try:
            result = tool.execute(**parameters)
            return result
        except TypeError as e:
            return {
                "success": False,
                "error": f"Invalid parameters for {tool_name}: {str(e)}"
            }
        except Exception as e:
            return {
                "success": False,
                "error": f"Tool execution error: {str(e)}"
            }
    
    def format_response(self, tool: Tool, parameters: Dict, result: Dict) -> str:
        """Format the agent's response based on tool results."""
        
        if not result.get("success", True):
            return f"I encountered an error: {result.get('error', 'Unknown error')}"
        
        if tool.name == 'calculator':
            expr = result.get('expression', parameters.get('expression'))
            value = result.get('result')
            return f"The result of {expr} is {value:,.2f}" if isinstance(value, float) else f"The result is {value}"
        
        elif tool.name == 'web_search':
            query = result.get('query')
            info = result.get('result')
            return f"Based on my search for '{query}': {info}"
        
        elif tool.name == 'get_time':
            return f"The current date and time is: {result.get('formatted')}"
        
        elif tool.name == 'save_note':
            return result.get('message', 'Note saved successfully')
        
        return str(result)
    
    def process_request(self, user_request: str) -> str:
        """Process a user request end-to-end."""
        print(f"\n[Processing request: {user_request}]")
        
        # Select tool
        tool = self.select_tool(user_request)
        
        if not tool:
            return "I'm not sure how to help with that. I can search the web, perform calculations, tell you the time, or save notes."
        
        print(f"[Selected tool: {tool.name}]")
        
        # Extract parameters
        parameters = self.extract_parameters(user_request, tool)
        print(f"[Parameters: {parameters}]")
        
        # Execute tool
        result = self.execute_tool(tool.name, **parameters)
        print(f"[Tool result: {result.get('success', False)}]")
        
        # Format response
        response = self.format_response(tool, parameters, result)
        
        # Store in history
        self.conversation_history.append({
            "request": user_request,
            "tool": tool.name,
            "parameters": parameters,
            "result": result,
            "response": response
        })
        
        return response
    
    def list_tools(self) -> str:
        """List all available tools."""
        result = "Available tools:\n\n"
        for tool in self.tools.values():
            result += f"• {tool.name}\n"
            result += f"  {tool.description}\n"
            if tool.parameters:
                result += f"  Parameters: {', '.join(tool.parameters.keys())}\n"
            result += "\n"
        return result


def main():
    """Test the ToolUsingAgent implementation."""
    print("=== Tool-Using Agent Solution Demo ===\n")
    
    # Create agent
    agent = ToolUsingAgent()
    
    # Show available tools
    print(agent.list_tools())
    print("\n" + "="*60 + "\n")
    
    # Test cases
    test_cases = [
        "What's 156 * 89?",
        "Search for the capital of France",
        "What time is it?",
        "Save a note saying 'Meeting at 3pm' to reminder.txt",
        "What is 25 + 37?",
        "Find information about Python programming",
        "Calculate 100 / 4",
        "What is the population of Tokyo?",
    ]
    
    # Process each test case
    for i, request in enumerate(test_cases, 1):
        print(f"Test {i}:")
        print(f"User: {request}")
        response = agent.process_request(request)
        print(f"Agent: {response}")
        print("\n" + "-"*60 + "\n")
    
    # Show conversation history summary
    print("\n=== Conversation Summary ===")
    tool_usage = {}
    for entry in agent.conversation_history:
        tool_name = entry['tool']
        tool_usage[tool_name] = tool_usage.get(tool_name, 0) + 1
    
    print("Tool usage statistics:")
    for tool_name, count in tool_usage.items():
        print(f"  {tool_name}: {count} times")


if __name__ == "__main__":
    main()
