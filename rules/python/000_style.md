# Python Style Guidelines

## Code Formatting
- Follow PEP 8 style guidelines
- Use 4 spaces for indentation (not tabs)
- Limit lines to 88 characters (Black formatter standard)
- Use consistent naming conventions:
  - `snake_case` for variables and functions
  - `PascalCase` for classes
  - `UPPER_CASE` for constants

## Documentation
- Use docstrings for all functions, classes, and modules
- Follow Google-style docstring format
- Include type hints for function parameters and return values
- Document complex algorithms with inline comments

## Imports
- Group imports in the following order:
  1. Standard library imports
  2. Third-party library imports
  3. Local application imports
- Sort imports alphabetically within each group
- Use absolute imports rather than relative imports when possible

## Error Handling
- Use specific exception types instead of catching all exceptions
- Provide meaningful error messages
- Log exceptions with appropriate context
- Clean up resources in finally blocks or use context managers

## Testing
- Write unit tests for all functions and classes
- Use pytest for testing
- Aim for high test coverage
- Use fixtures and parametrization for test reuse 