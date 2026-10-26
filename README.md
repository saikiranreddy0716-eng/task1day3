
# Day 3 - Student Record Manager

## Description

A menu-driven Python application for creating, listing, searching,
and deleting student records.

The project uses functions, modules, type hints, docstrings,
input validation, and exception handling.

## Project structure

- record_manager/operations.py - Core record operations
- record_manager/cli.py - Command-line interface
- record_manager/__init__.py - Package initializer
- test_operations.py - Automated unit tests

## Requirements

- Python 3.10 or newer
- Git (for version control)

## Setup

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Run the application

```powershell
python -m record_manager.cli
```

## Run tests

```powershell
python -m unittest -v
```

## Note

Records are stored in memory and are not saved after the
application exits.
