# python_iteration

A small Python project demonstrating linked list utilities with a generator and an iterator.

Contents
- `src/node.py` - linked list node implementation.
- `src/linked_list_generator.py` - generator-based linked list traversal utilities.
- `src/linked_list_iterator.py` - iterable/iterator implementation for the linked list.
- `tests/` - unit tests for the modules above.

Requirements
- Python 3.8+

Installation (uv-based)
1. (Optional) Create and activate a virtual environment:

```bash
uv sync
```

2. Install the package and any dependencies using the project's `uv` helper:

```bash
uv run pip install -e .
```

Running the project
- Run the simple entry point:

```bash
uv run main.py
```

Running tests

```bash
uv run pytest
```

Running lint
```bash
uv run pylint src tests
```

Contributing
- Add tests for new behavior under `tests/` and run `uv run pytest`.
- Keep code style consistent; run `uv run pylint src tests` before opening PRs.

License
- See `pyproject.toml` for packaging metadata.

