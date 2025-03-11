# Cursor Rules Generator

A template and generator for Cursor AI coding assistant rules. This repository helps you create and maintain custom rules for the Cursor AI assistant to follow when working on your projects.

## What are Cursor Rules?

Cursor Rules are instructions that guide the Cursor AI assistant's behavior when working with your codebase. They help ensure that the AI follows your project's specific conventions, best practices, and requirements.

Rules are stored in `.mdc` files within the `.cursor/rules/` directory of your project. Each `.mdc` file contains a set of instructions for the AI to follow when working with specific file types or parts of your codebase.

## Repository Structure

- `build_mdc.py`: Script to generate `.mdc` files from markdown files
- `rules_config.json`: Configuration file for defining rule categories and output files
- `rules/`: Directory containing markdown files with rules organized by category
  - `general/`: General project guidelines
  - `python/`: Python-specific guidelines
  - `javascript/`: JavaScript-specific guidelines
  - `web/`: Web development guidelines
  - `database/`: Database-related guidelines

## How to Use This Template

1. **Clone this repository** to your local machine or use it as a template for your own repository.

2. **Customize the rules** in the `rules/` directory to match your project's requirements:
   - Edit existing markdown files
   - Add new markdown files (use numeric prefixes like `001_` for ordering)
   - Create new category directories as needed

3. **Configure the rule generation** by editing `rules_config.json`:
   - Define output `.mdc` files
   - Specify source directories
   - Set file patterns and headers

4. **Generate the rules** by running:
   ```bash
   python build_mdc.py
   ```

5. **Copy the generated `.cursor/rules/` directory** to your project.

## Writing Effective Rules

Rules should be clear, specific, and actionable. Here are some tips for writing effective rules:

- **Be specific**: Instead of "Write good code", use "Follow PEP 8 style guidelines for Python code"
- **Provide examples**: Include code examples to illustrate the desired patterns
- **Explain reasoning**: Briefly explain why a rule exists to help the AI understand its importance
- **Use consistent formatting**: Structure your rules with headings, bullet points, and code blocks

## Rule File Format

Each rule file should be a markdown (`.md`) file with a clear structure:

```markdown
# Category Title

## Subcategory

- Rule 1
- Rule 2
  - Sub-rule A
  - Sub-rule B
- Rule 3

## Another Subcategory

- Rule 4
- Rule 5
```

## Configuration File Format

The `rules_config.json` file defines how rule files are combined into `.mdc` files:

```json
[
  {
    "output": ".cursor/rules/000_general.mdc",
    "source_dir": "rules/general",
    "header": "---\ndescription: General instructions for your project.\nglobs: *\nalwaysApply: true\n---\n\n",
    "file_pattern": "*.md"
  }
]
```

Each configuration object has the following properties:

- `output`: Path to the output `.mdc` file
- `source_dir`: Directory containing source markdown files
- `header`: YAML front matter for the `.mdc` file
- `file_pattern`: Pattern to match markdown files in the source directory

## Advanced Usage

### File Ordering

Files are processed in order based on their numeric prefixes (e.g., `001_`, `002_`). Use this to control the order of rules within a category.

### Custom Categories

You can create custom rule categories by:

1. Creating a new directory under `rules/`
2. Adding markdown files to the directory
3. Adding a new configuration object to `rules_config.json`

### Conditional Rules

In the header section, you can specify when rules should apply:

- `globs`: File patterns that the rules apply to (e.g., `*.py`, `src/*.js`)
- `alwaysApply`: Whether the rules should always apply or only when requested

## License

This project is open source and available under the MIT License.