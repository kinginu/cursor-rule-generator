#!/usr/bin/env python3
import os
import glob
import re
import json
from pathlib import Path

def load_config(config_path="rules_config.json"):
    """Load MDC configurations from a JSON file."""
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        # Default configuration if file doesn't exist
        default_config = [
            {
                "output": ".cursor/rules/000_general.mdc",
                "source_dir": "rules/general",
                "header": "---\ndescription: General instructions for your project.\nglobs: *\nalwaysApply: true\n---\n\n",
                "file_pattern": "*.md",
            },
            {
                "output": ".cursor/rules/001_python_best_practices.mdc",
                "source_dir": "rules/python",
                "header": "---\ndescription: Python best practices for your project.\nglobs: *.py\nalwaysApply: true\n---\n\n",
                "file_pattern": "*.md",
            },
        ]
        # Create the default config file
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2)
        print(f"Created default configuration file: {config_path}")
        return default_config

def extract_number_prefix(filename):
    """Extract the numeric prefix from a filename for sorting."""
    match = re.match(r'^(\d+)_', os.path.basename(filename))
    return int(match.group(1)) if match else float('inf')

def build_mdc_file(config):
    """Build an MDC file from MD files in the specified directory."""
    # Get the root directory (current working directory)
    root_dir = os.getcwd()
    
    # Create the pattern for finding MD files
    pattern = os.path.join(root_dir, config["source_dir"], config["file_pattern"])
    
    # Find all MD files matching the pattern
    files = glob.glob(pattern)
    
    # Sort files by their numeric prefix
    files.sort(key=extract_number_prefix)
    
    # Initialize content with the header
    content = config["header"]
    
    # Combine the content of all MD files
    for file in files:
        print(f"Processing file: {file}")
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
            content += file_content + "\n\n"
    
    # Ensure the output directory exists
    output_path = os.path.join(root_dir, config["output"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Write the combined content to the MDC file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Generated {config['output']} from {len(files)} files in {config['source_dir']}")

def clean_mdc_files(output_dir=".cursor/rules"):
    """Clean existing MDC files in the specified rules directory."""
    rules_dir = os.path.join(os.getcwd(), output_dir)
    
    # Check if the directory exists
    if not os.path.exists(rules_dir):
        os.makedirs(rules_dir, exist_ok=True)
        return
    
    # Find all MDC files and clear their content
    mdc_files = glob.glob(os.path.join(rules_dir, '*.mdc'))
    for file in mdc_files:
        print(f"Clearing content of MDC file: {file}")
        with open(file, 'w', encoding='utf-8') as f:
            f.write('')  # Clear the file content

def create_template_structure():
    """Create a template directory structure if it doesn't exist."""
    template_dirs = [
        "rules/general",
        "rules/python",
        "rules/javascript",
        "rules/web",
        "rules/database"
    ]
    
    for directory in template_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
            print(f"Created template directory: {directory}")
            
            # Create a sample file in each directory
            sample_file = os.path.join(directory, "000_template.md")
            if not os.path.exists(sample_file):
                with open(sample_file, 'w', encoding='utf-8') as f:
                    category = directory.split('/')[-1].capitalize()
                    f.write(f"# {category} Guidelines\n\n")
                    f.write("## Best Practices\n")
                    f.write("- Add your best practices here\n")
                    f.write("- Each rule should be clear and specific\n\n")
                    f.write("## Conventions\n")
                    f.write("- Add your conventions here\n")
                    f.write("- Be consistent with your style guidelines\n")

def main():
    """Main function to generate all MDC files."""
    try:
        # Create template structure if needed
        create_template_structure()
        
        # Load configuration
        mdc_configurations = load_config()
        
        # Clean existing MDC files
        output_dirs = set(os.path.dirname(config["output"]) for config in mdc_configurations)
        for output_dir in output_dirs:
            clean_mdc_files(output_dir)
        
        # Generate each MDC file based on the configurations
        for config in mdc_configurations:
            build_mdc_file(config)
        
        print("All MDC files have been successfully generated!")
    except Exception as e:
        print(f"Error generating MDC files: {e}")
        exit(1)

if __name__ == "__main__":
    main() 