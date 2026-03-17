*These modules have been created as part of the 42 curriculum by mel-asla.*

# Python Learning Journey (Modules 00 -> 10)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Curriculum](https://img.shields.io/badge/42-Curriculum-000000?style=for-the-badge&logo=42&logoColor=white)
![Progress](https://img.shields.io/badge/Modules-00--10-1E9E63?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Learning%20by%20Building-E67E22?style=for-the-badge)
![Topics](https://img.shields.io/badge/OOP%20%7C%20Validation%20%7C%20Functional%20Programming-8E44AD?style=for-the-badge)

## Description
This repository contains my full progression through the 42 Python modules, from `python_module_00` to `python_module_10`.

Project goal:
- Build a strong and practical Python foundation.
- Apply concepts incrementally through small, focused exercises.
- Demonstrate software engineering growth across syntax, OOP, errors, data handling, packaging, validation, and functional programming.

Overview:
- `python_module_00`: Python fundamentals (functions, conditions, loops, recursion).
- `python_module_01`: Object-oriented programming basics.
- `python_module_02`: Exception handling and custom errors.
- `python_module_03`: Data structures, comprehensions, generators.
- `python_module_04`: File I/O, streams, context managers.
- `python_module_05`: Abstract classes, protocols, pipeline design.
- `python_module_06`: Imports, package structure, circular-import handling.
- `python_module_07`: Advanced OOP and design patterns.
- `python_module_08`: Environments, dependencies, and configuration.
- `python_module_09`: Data validation with Pydantic.
- `python_module_10`: Functional programming and decorators.

## Instructions
### Prerequisites
- Python `3.10+`
- `pip` and optionally `venv`
- Optional for module 08/ex1: `poetry`

### Installation
From repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install python-dotenv pydantic numpy pandas matplotlib requests
```

Optional Poetry setup for `python_module_08/ex1`:

```bash
cd python_module_08/ex1
poetry install
```

### Execution
Run each exercise file directly from the repository root:

```bash
python3 python_module_00/ex0/ft_hello_garden.py
python3 python_module_03/ex6/ft_analytics_dashboard.py
python3 python_module_10/ex4/decorator_mastery.py
```

For package-related exercises (notably in `python_module_06` and `python_module_07`), execute from repository root to preserve import resolution.

## Config File Structure and Format
This repository uses two practical configuration formats in module 08.

### 1) `pyproject.toml`
Path: `python_module_08/ex1/pyproject.toml`

Structure:
- `[tool.poetry]`: project metadata (`name`, `version`, `authors`, etc.)
- `[tool.poetry.dependencies]`: runtime dependencies and Python version range
- `[build-system]`: build backend requirements

Current format in this project:

```toml
[tool.poetry]
name = "ex1"
version = "0.1.0"
description = ""
authors = ["mel-asla <mel-asla@student.1337.ma>"]
package-mode = false

[tool.poetry.dependencies]
python = ">=3.10,<4.0"
pandas = ">=2.1.0"
numpy = ">=1.26.0"
matplotlib = ">=3.7.2"
requests = ">=2.31.0"

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

### 2) `.env` configuration
Path: `python_module_08/ex2/.env` (expected by `python_module_08/ex2/oracle.py`)

Expected keys:
- `MATRIX_MODE` (`development` or `production`)
- `DATABASE_URL`
- `API_KEY`
- `LOG_LEVEL` (optional, defaults to `INFO`)
- `ZION_ENDPOINT`

Example format:

```env
MATRIX_MODE=development
DATABASE_URL=postgresql://localhost:5432/matrix
API_KEY=replace_with_real_key
LOG_LEVEL=INFO
ZION_ENDPOINT=https://zion.example/api
```

## Maze Generation Algorithm
This repository does not currently implement a maze generator.

For a maze feature extension, I would use the `recursive backtracking` algorithm (depth-first search variant).

## Why This Algorithm
I would choose recursive backtracking because:
- It is simple to implement and explain.
- It generates valid perfect mazes (single unique path between any two cells).
- It offers good performance for typical school-project grid sizes.
- It is easy to adapt to iterative form with an explicit stack.

## Reusable Code and How
Reusable parts already present in this repository include:
- Validation patterns: custom exceptions and structured checks (`python_module_02`, `python_module_09`).
- OOP abstractions: ABC/protocol interfaces reusable for new domains (`python_module_05`, `python_module_07`).
- Package/import architecture: reusable module layout for medium projects (`python_module_06`).
- Functional helpers: decorators, higher-order functions, and `functools` utilities (`python_module_10`).
- Environment/config handling: `.env` and dependency-loading patterns (`python_module_08`).

How they are reused:
- By copying interface definitions and adapting domain-specific implementations.
- By reusing validation logic as a service layer before business logic.
- By reusing decorators for logging, retries, input checks, and timing.
- By reusing package structure and import conventions in new projects.

## Resources
Classic references:
- Python Official Documentation: https://docs.python.org/3/
- PEP 8 (Style Guide): https://peps.python.org/pep-0008/
- `typing` module docs: https://docs.python.org/3/library/typing.html
- `abc` module docs: https://docs.python.org/3/library/abc.html
- `functools` module docs: https://docs.python.org/3/library/functools.html
- Pydantic Documentation: https://docs.pydantic.dev/
- Poetry Documentation: https://python-poetry.org/docs/

AI usage disclosure:
- AI was used to improve documentation quality in this repository.
- AI-assisted tasks: README structure, wording refinement, and concept summarization.
- AI was not used as a blind replacement for understanding; code and concepts were reviewed and validated through the exercises.
