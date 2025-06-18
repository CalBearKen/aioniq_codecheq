"""
LLM Code Analyzer CLI

This module provides the command-line interface for the LLM Code Analyzer.
"""

import json
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from ..analyzer import CodeAnalyzer
from ..models.analysis_result import Severity

app = typer.Typer(help="LLM Code Analyzer CLI")
console = Console()


@app.command()
def analyze(
    path: Path = typer.Argument(..., help="Path to file or directory to analyze"),
    provider: str = typer.Option("openai", help="LLM provider (openai or anthropic)"),
    model: str = typer.Option("gpt-4", help="Model to use for analysis"),
    output: Optional[Path] = typer.Option(None, help="Output file path"),
    format: str = typer.Option("text", help="Output format (text, json, or html)"),
    api_key: Optional[str] = typer.Option(None, help="API key for the provider"),
):
    """Analyze code for security vulnerabilities using LLMs."""
    try:
        # Initialize analyzer
        analyzer = CodeAnalyzer(
            provider=provider,
            model=model,
            api_key=api_key,
        )

        # Analyze file or directory
        if path.is_file():
            console.print(f"Analyzing file: {path}")
            result = analyzer.analyze_file(path)
        else:
            console.print(f"Analyzing directory: {path}")
            result = analyzer.analyze_directory(path)

        # Output results
        if output:
            if format == "json":
                output.write_text(result.to_json())
            elif format == "html":
                output.write_text(result.to_html())
            else:
                output.write_text(str(result))
        else:
            # Display results in console
            if format == "json":
                console.print_json(result.to_json())
            elif format == "html":
                console.print(result.to_html())
            else:
                display_results(result)

    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")
        raise typer.Exit(1)


def display_results(result):
    """Display analysis results in a formatted table."""
    # Create table
    table = Table(title="Code Analysis Results")
    table.add_column("Severity", style="bold")
    table.add_column("Location")
    table.add_column("Message")
    table.add_column("Description")

    # Add issues to table
    for issue in result.issues:
        severity_color = {
            Severity.ERROR: "red",
            Severity.WARNING: "yellow",
            Severity.INFO: "blue",
        }[issue.severity]

        table.add_row(
            f"[{severity_color}]{issue.severity}[/{severity_color}]",
            f"{issue.location.path}:{issue.location.start_line}",
            issue.message,
            issue.description,
        )

    # Display table
    console.print(table)

    # Display summary
    console.print("\n[bold]Summary:[/bold]")
    console.print(f"Total issues: {len(result.issues)}")
    for severity in Severity:
        count = len(result.get_issues_by_severity(severity))
        console.print(f"{severity.value}: {count}")


if __name__ == "__main__":
    app() 