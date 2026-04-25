"""
Handles saving reports to the filesystem and reading them back.
"""
import os

def save_report(report: str, filename: str) -> str:
    path = f"{filename}.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(report)
    return path

def read_back(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    print("Module: storage")
    print("Purpose: Saves string reports to text files and reads them back.")
    print("Public Functions: save_report, read_back")
    print('Example: save_report("My Report", "output")')