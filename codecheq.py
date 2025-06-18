#!/usr/bin/env python
"""
CodeCheq CLI Entry Point

This script serves as the main entry point for the CodeCheq command-line interface.
"""

import os
import sys

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from codecheq.cli.main import app

if __name__ == "__main__":
    app() 