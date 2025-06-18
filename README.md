# CodeCheq

A powerful library for analyzing code security using Large Language Models (LLMs). This tool helps identify potential security vulnerabilities, code smells, and best practice violations in your codebase.

## Features

- 🔍 Evidence-based code analysis using LLMs
- 🛡️ Security vulnerability detection
- 📊 Detailed analysis reports
- 🔄 Support for multiple LLM providers (OpenAI, Anthropic)
- 📝 Customizable analysis prompts
- 🎯 Multiple output formats (JSON, HTML, Text)
- 🚀 Easy-to-use CLI interface
- 🔒 HIPAA and healthcare compliance analysis

## Installation

### From PyPI

```bash
pip install codecheq
```

### From Source

```bash
# Clone the repository
git clone https://github.com/yourusername/codecheq.git
cd codecheq

# Install in editable mode
pip install -e .
```

## Quick Start

### Using the Library

```python
from codecheq import CodeAnalyzer

# Initialize the analyzer
analyzer = CodeAnalyzer(provider="openai", model="gpt-4")

# Analyze a file
results = analyzer.analyze_file("path/to/your/file.py")

# Print results
for issue in results.issues:
    print(f"Severity: {issue.severity}")
    print(f"Message: {issue.message}")
    print(f"Location: {issue.location}")
    print(f"Description: {issue.description}")
    print(f"Recommendation: {issue.recommendation}")
    print("---")
```

### Using the CLI

#### After Installation

If you've installed the package (either from PyPI or in editable mode), you can use the CLI directly:

```bash
# Analyze a single file
codecheq file.py

# Analyze a directory
codecheq directory/

# Generate HTML report
codecheq file.py --format html --output report.html

# Use specific model
codecheq file.py --model gpt-4
```

#### Without Installation

If you haven't installed the package, you can use the provided scripts:

```bash
# Using the Python script
python codecheq.py file.py

# Using the batch file (Windows)
codecheq.bat file.py

# Using the run script
python run_codecheq.py file.py
```

## Configuration

The library can be configured using environment variables or a configuration file:

```bash
# Environment variables
export OPENAI_API_KEY="your-api-key"
export ANTHROPIC_API_KEY="your-api-key"
export CODECHEQ_MODEL="gpt-4"
```

Or create a `.env` file:

```env
OPENAI_API_KEY=your-api-key
ANTHROPIC_API_KEY=your-api-key
CODECHEQ_MODEL=gpt-4
```

## Advanced Usage

### Custom Analysis Prompts

```python
from codecheq import CodeAnalyzer, PromptTemplate

# Create custom prompt
custom_prompt = PromptTemplate(
    template="""Analyze the following code for {analysis_type}:
    {code}
    
    Focus on:
    {focus_areas}
    """,
    variables=["analysis_type", "code", "focus_areas"]
)

# Use custom prompt
analyzer = CodeAnalyzer(prompt=custom_prompt)
```

### Batch Analysis

```python
from codecheq import BatchAnalyzer

# Initialize batch analyzer
batch = BatchAnalyzer()

# Add files to analyze
batch.add_file("file1.py")
batch.add_file("file2.py")
batch.add_directory("src/")

# Run analysis
results = batch.analyze()

# Export results
results.export_html("report.html")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/codecheq.git
cd codecheq

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all the contributors who have helped shape this project
- Inspired by various code analysis tools and security best practices 