"""
Basic usage example for CodeCheq.
"""

from codecheq import CodeAnalyzer

def main():
    # Initialize the analyzer
    analyzer = CodeAnalyzer(
        provider="openai",  # or "anthropic"
        model="gpt-4",      # or any other supported model
    )

    # Example code to analyze
    code = """
    def process_user_data(user_input):
        # Process user input without validation
        result = eval(user_input)
        return result

    def store_password(password):
        # Store password in plain text
        with open("passwords.txt", "a") as f:
            f.write(password + "\\n")
    """

    # Analyze the code
    result = analyzer.analyze_code(code, "example.py")

    # Print results
    print(f"Found {len(result.issues)} issues:")
    for issue in result.issues:
        print(f"\\nSeverity: {issue.severity}")
        print(f"Message: {issue.message}")
        print(f"Location: {issue.location.path}:{issue.location.start_line}")
        print(f"Description: {issue.description}")
        print(f"Recommendation: {issue.recommendation}")
        print("Code snippet:")
        print(issue.code_snippet)

if __name__ == "__main__":
    main() 