import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import Any

from .models import TaskItem
from .executor import run_sync, run_async, run_limited

def main() -> None:
    parser = argparse.ArgumentParser(description="Async Batch Processor")
    parser.add_argument("input", type=Path, help="Path to input JSON file")
    parser.add_argument("--mode", choices=["sync", "async", "limited"], default="sync", help="Execution mode (default: sync)")
    parser.add_argument("--limit", type=int, default=5, help="Concurrency limit for 'limited' mode (default: 5)")
    parser.add_argument("--continue_on_error", action="store_true", help="Continue processing if a task fails")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="WARNING", help="Logging level (default: WARNING)")

    args = parser.parse_args()

    numeric_level = getattr(logging, args.log_level.upper())
    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s %(message)s]",
        stream=sys.stderr
    )

    if not args.input.exists():
        logging.error(f"Input file not found: {args.input}")
        sys.exit(1)

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            raw_data: Any = json.load(f)

        items: list[TaskItem] = [
            {
                "id": int(d["id"]),
                "delay": float(d["delay"]),
                "good": bool(d["good"])
            }
            for d in raw_data
        ]
    except Exception as e:
        logging.error(f"Failed to parse input file: {e}")
        sys.exit(1)

    try:
        if args.mode == "sync":
            results = asyncio.run(run_sync(items, args.continue_on_error))
        elif args.mode == "async":
            results = asyncio.run(run_async(items, args.continue_on_error))
        elif args.mode == "limited":
            results = asyncio.run(run_limited(items, args.limit, args.continue_on_error))
        else:
            results = []

        print(json.dumps(results, indent=2))
    except Exception as e:
        logging.error(f"Execution aborted due to an error: {e}")
        sys.exit(1)
    
if __name__ == "__main__":
    main()