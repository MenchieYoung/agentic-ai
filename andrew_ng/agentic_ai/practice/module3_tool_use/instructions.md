# Module 3: Tool-Using Agent Exercise

## Objective
Build an agent that can use external tools to accomplish tasks it couldn't do through text generation alone.

## Learning Goals
By completing this exercise, you will:
- Define tools with clear descriptions and parameters
- Implement tool selection logic
- Handle tool calls and results
- Combine multiple tools in a workflow
- Understand the Model Context Protocol (MCP) principles

## Scenario
You're building a research assistant agent that can:
1. Search the web for information
2. Perform mathematical calculations
3. Get current date/time
4. Save notes to a file

The agent should automatically decide which tool to use based on the user's request.

## Task Requirements

### Part 1: Define Tools (Required)
Create tool definitions with:
- Tool name
- Clear description of what it does
- Parameter specifications
- Example usage

Implement these tools:
1. **web_search(query: str) → dict**
   - Searches the web and returns results
   
2. **calculator(expression: str) → float**
   - Evaluates mathematical expressions
   
3. **get_current_time() → str**
   - Returns current date and time
   
4. **save_note(content: str, filename: str) → bool**
   - Saves content to a file

### Part 2: Tool Selection (Required)
Implement logic to:
- Parse user requests
- Identify which tool(s) to use
- Extract parameters from the request
- Handle cases where no tool is needed

### Part 3: Tool Execution (Required)
Implement:
- Tool calling with error handling
- Result processing
- Response generation using tool results

### Part 4: Multi-Tool Workflow (Required)
Handle requests that require multiple tools:
- Example: "Search for the population of Tokyo and calculate 10% of it"
- Sequential tool calls
- Using results from one tool in another

### Part 5: Extensions (Optional)
- Add more tools (weather, currency conversion, etc.)
- Implement tool result caching
- Add conversation context for follow-up questions
- Create a simple MCP-like interface

## Starter Code Structure

```python
class Tool:
    """Base class for tools."""
    def __init__(self, name: str, description: str, parameters: dict):
        self.name = name
        self.description = description
        self.parameters = parameters
    
    def execute(self, **kwargs):
        raise NotImplementedError

class ToolUsingAgent:
    def __init__(self):
        self.tools = {}
        self._register_tools()
    
    def _register_tools(self):
        # TODO: Register available tools
        pass
    
    def select_tool(self, user_request: str):
        # TODO: Decide which tool to use
        pass
    
    def extract_parameters(self, user_request: str, tool: Tool):
        # TODO: Extract parameters from request
        pass
    
    def execute_tool(self, tool_name: str, **parameters):
        # TODO: Execute the tool and handle errors
        pass
    
    def process_request(self, user_request: str):
        # TODO: Main workflow
        pass
```

## Test Cases

```python
test_cases = [
    "What's 156 * 89?",
    "Search for the capital of France",
    "What time is it?",
    "Save a note saying 'Meeting at 3pm' to reminder.txt",
    "Search for Python tutorials and save the results to notes.txt",
]
```

## Expected Output Format

```
User: What's 156 * 89?
Agent: I'll use the calculator tool to compute that.
[Tool Call: calculator(expression="156 * 89")]
[Tool Result: 13884.0]
Agent: The result is 13,884.

User: Search for the capital of France
Agent: I'll search for that information.
[Tool Call: web_search(query="capital of France")]
[Tool Result: {...}]
Agent: The capital of France is Paris.
```

## Implementation Tips

### Mock Tool Implementations

For the exercise, use simple mock implementations:

```python
class WebSearchTool(Tool):
    def __init__(self):
        super().__init__(
            name="web_search",
            description="Search the web for information on a topic",
            parameters={"query": "string - the search query"}
        )
    
    def execute(self, query: str):
        # Mock implementation - return fake but relevant results
        mock_results = {
            "capital of france": "Paris is the capital of France.",
            "python tutorials": "Python.org offers official tutorials.",
            # Add more mock data
        }
        # Simple matching
        for key, value in mock_results.items():
            if key.lower() in query.lower():
                return {"result": value, "source": "mock_search"}
        return {"result": "No results found", "source": "mock_search"}

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="calculator",
            description="Evaluate mathematical expressions",
            parameters={"expression": "string - the mathematical expression"}
        )
    
    def execute(self, expression: str):
        try:
            # Use eval safely for mock (in production, use ast.literal_eval or a math parser)
            result = eval(expression, {"__builtins__": {}}, {})
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}
```

### Tool Selection Logic

Simple approach using keyword matching:

```python
def select_tool(self, user_request: str):
    request_lower = user_request.lower()
    
    # Check for calculation keywords
    calc_keywords = ['calculate', 'compute', 'what is', '*', '+', '-', '/', 'multiply']
    if any(kw in request_lower for kw in calc_keywords):
        return self.tools.get('calculator')
    
    # Check for search keywords
    search_keywords = ['search', 'find', 'look up', 'what is', 'who is']
    if any(kw in request_lower for kw in search_keywords):
        return self.tools.get('web_search')
    
    # ... more logic
```

### Parameter Extraction

```python
def extract_parameters(self, user_request: str, tool: Tool):
    if tool.name == 'calculator':
        # Extract mathematical expression
        # Look for expressions with numbers and operators
        import re
        match = re.search(r'[\d+\-*/\(\)\s]+', user_request)
        if match:
            return {'expression': match.group().strip()}
    
    elif tool.name == 'web_search':
        # Extract search query - often everything after "search for"
        if 'search for' in user_request.lower():
            query = user_request.lower().split('search for', 1)[1].strip()
            return {'query': query}
    
    return {}
```

## Testing Your Implementation

1. **Single tool calls**: Test each tool independently
2. **Tool selection**: Verify correct tool is chosen for various requests
3. **Parameter extraction**: Ensure parameters are correctly extracted
4. **Error handling**: Test with invalid inputs
5. **Multi-tool workflows**: Test requests requiring multiple tools

## Success Criteria

Your implementation should:
- ✅ Define at least 4 tools with clear descriptions
- ✅ Correctly select tools based on requests
- ✅ Extract parameters accurately
- ✅ Execute tools and handle results
- ✅ Handle errors gracefully
- ✅ Support multi-tool workflows

## Common Pitfalls

1. **Vague tool descriptions**: Be specific about what each tool does
2. **Poor parameter extraction**: Use robust parsing, not fragile string matching
3. **No error handling**: Always handle tool execution failures
4. **Ambiguous requests**: Handle cases where multiple tools could apply
5. **Ignoring context**: Consider conversation history for follow-ups

## Extension Ideas

After completing the basic exercise:
1. Add a tool for current weather using a mock API
2. Implement a simple conversation memory
3. Create a tool that uses results from another tool
4. Build a simple MCP-compatible interface
5. Add logging to track tool usage patterns

## Reflection Questions (Answer After Completing)

1. How did you decide between competing tools for ambiguous requests?
2. What's the most challenging part of parameter extraction?
3. How would you extend this to support 20+ tools?
4. What would change if using real APIs instead of mocks?
5. How does MCP simplify tool integration?

## Time Estimate
- Part 1: 30-40 minutes
- Part 2: 40-50 minutes
- Part 3: 30-40 minutes
- Part 4: 30-40 minutes
- Part 5 (optional): 60+ minutes

## Next Steps
After completing this exercise:
1. Compare your solution with the provided solution
2. Try integrating a real API (weather, news, etc.)
3. Research MCP implementations
4. Move to Module 4: Practical Tips

---

**Good luck! Focus on understanding tool selection and integration patterns.**
