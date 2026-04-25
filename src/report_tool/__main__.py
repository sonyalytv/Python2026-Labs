from .analyzer import parse_numbers, analyze_numbers
from .formatter import build_report, build_sorted_report
from .storage import save_report, read_back

def show_help() -> None:
    print("Report Tool")
    print("=" * 30)
    print("This tool works with simple numeric reports.")
    print("Use it to parse numbers, analyze them, format a report, and save it.\n")
    print("Public Capabilities:")
    print(" - parse_numbers: Convert string to list of floats")
    print(" - analyze_numbers: Calculate sum, min, max, and mean")
    print(" - build_report / build_sorted_report: Format stats into text")
    print(" - save_report / read_back: Handle file operations\n")
    print("Example usage in code:")
    print("  from report_tool import parse_numbers, analyze_numbers")
    print('  numbers = parse_numbers("1, 2, 3, 4.5")\n')

def example_workflow() -> str:
    text = "4, 8, 15, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze_numbers(numbers)
    report = build_sorted_report(numbers, stats)
    return report

def main() -> None:
    show_help()
    print("--- Running Example Workflow ---")
    report = example_workflow()
    print(report)

    path = save_report(report, "report_output")
    print(f"\nSaved to: {path}\n")
    print("Saved file content:")
    print(read_back(str(path)))

if __name__ == "__main__":
    main()