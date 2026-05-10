import asyncio
import logging
from .models import TaskItem, TaskResult, process_item

async def _execute_task(item: TaskItem, continue_on_error: bool) -> TaskResult:
    """Execution logic wrapper that handles logginh and error catching."""
    logging.info(f"Task {item['id']} started")

    if item["delay"] > 3.0:
        logging.warning(f"Task {item['id']} has a long delay ({item['delay']}s)")

    try:
        result = await process_item(item)
        logging.info(f"Task {item['id']} completed")
        return result
    except Exception as e:
        logging.error(f"Task {item['id']} failed: {e}")
        if not continue_on_error:
            logging.error(f"Task {item['id']} failed fatally: {e}")
            raise

        logging.warning(f"Task {item['id']} failed, but continuing. Reason: {e}")
        return {
            "id": item["id"],
            "status": "error",
            "message": str(e)
        }

async def _wrapped_limited_task(item: TaskItem, continue_on_error: bool, sem: asyncio.Semaphore) -> TaskResult:
    """Wraps task execution inside a semaphore."""
    async with sem:
        return await _execute_task(item, continue_on_error)
    
async def run_sync(items: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    """Processes tasks sequentially."""
    results: list[TaskResult] = []
    for item in items:
        results.append(await _execute_task(item, continue_on_error))
    return results

async def run_async(items: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    """Processes tasks concurrently using asyncio.gather."""
    coroutines = [_execute_task(item, continue_on_error) for item in items]
    results = await asyncio.gather(*coroutines)
    return list(results)

async def run_limited(items: list[TaskItem], limit: int, continue_on_error: bool) -> list[TaskResult]:
    """Processes tasks concurrently but limits the number of active tasks using a Semaphore."""
    sem = asyncio.Semaphore(limit)
    coroutines = [_wrapped_limited_task(item, continue_on_error, sem) for item in items]
    results = await asyncio.gather(*coroutines)
    return list(results)