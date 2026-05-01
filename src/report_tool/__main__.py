import argparse
import logging
import sys
from .analyzer import parse_numbers, analyze_numbers
from .formatter import build_sorted_report, build_sorted_json_report
from .storage import save_report, read_input

logger = logging.getLogger(__name__)

def setup_logging(level_name: str) -> None:
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%H:%M:%S'
    )

def main() -> None:
    parser = argparse.ArgumentParser(description="Report Tool: A CLI for numeric data analysis.")
    parser.add_argument("--input", required=True, help="Path to the input file containing numeric data")
    parser.add_argument("--out", required=True, help="Path where the report will be saved")
    parser.add_argument("--format", choices=['text', 'json'], default='text', help="Output format for the report")
    parser.add_argument("--log-level", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], default='INFO', help="Set the logging level")

    args = parser.parse_args()
    setup_logging(args.log_level)

    logger.info("Starting Report Tool pipeline")

    try:
        # Step 1: Read input
        raw_text = read_input(args.input)

        # Step 2: Parse and Analyze
        numbers = parse_numbers(raw_text)
        stats = analyze_numbers(numbers)

        # Step 3: Format output
        if args.format == 'json':
            logger.info("Formatting output as JSON")
            report = build_sorted_json_report(numbers, stats)
        else:
            logger.info("Formatting output as Text")
            report = build_sorted_report(numbers, stats)

        # Step 4: Write output
        save_report(report, args.out)
        logger.info(f"Pipeline finished successfully. Output saved to {args.out}")

    except Exception as e:
        logger.error(f"An error occurred during execution: {e}", exc_info=args.log_level == 'DEBUG')
        sys.exit(1)

if __name__ == "__main__":
    main()