# Lab 09 Report

## 1. What was wrong in the original project
The original project lacked a coherent structure and violated multiple Python best practices. 
* `run.py` was acting as an entry point but wasn't properly designated as a package main file (`__main__.py`). 
* Modules executed debugging code directly in the global scope, meaning that simply importing a module caused console output. 
* The project lacked an `__init__.py` file, forcing developers to know the internal structure of the package to import functions.
* Furthermore, internal helper functions were publicly exposed, module imports relied on unpredictable global paths, and `requirements.txt` was full of libraries that the standard library logic did not utilize. 

## 2. What was improved
* **Module Reorganization & Naming:** `run.py` was renamed to `__main__.py` to allow the project to be executed natively using `python -m report_tool`. Poorly named modules were renamed to clearly represent their usage (`helpers.py` $\rightarrow$ `analyzer.py`, `textstuff.py` $\rightarrow$ `formatter.py`, `saveit.py` $\rightarrow$ `storage.py`).
* **Public vs. Private Design:** Internal helper functions (e.g., `cleanupPieces`, `prettyTitle`) were renamed using the underscore convention (`_cleanup_pieces`, `_pretty_title`) to indicate they are private.
* **Package-Level API:** An `__init__.py` file was introduced to export only the intended public functions (`parse_numbers`, `analyze_numbers`, `build_report`, etc.), establishing a clean package API.
* **Cleaned Execution:** Module-level debugging code and global prints were removed. Modules were wrapped with `if __name__ == "__main__":` blocks to display their purpose and minimal usage examples safely.
* **Imports and Dependencies:** Implicit module imports were updated to safe relative imports (e.g., `from .analyzer import`). Unused dependencies were cleared from `requirements.txt`, and the `README.md` was rewritten to clearly explain functionality and usage.

## 3. Why these changes matter
* **Readability:** Renaming variables to standard Python conventions and isolating logic into properly named modules makes the codebase much easier for a developer to read and navigate.
* **Usability:** Adding the `__init__.py` file means external users only need a single import statement (e.g., `from report_tool import parse_numbers`) without guessing which nested file contains the code. The updated `README.md` and module-level printouts give users immediate, clear instructions.
* **Stability:** Removing debugging code from the global scope prevents unexpected prints or variable collisions during an import. Standardizing relative imports eliminates the need for path hacks like `sys.path.append`.
* **Maintainability:** By strictly distinguishing between public API and internal (`_`) functions, future developers can safely modify or refactor internal functions without worrying about breaking external code that relies on the tool.