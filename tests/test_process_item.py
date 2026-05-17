import pytest
from src.async_tool.models import process_item, TaskItem

@pytest.mark.asyncio
async def test_process_item_success() -> None:
    """Test valid input returns correct result."""
    item: TaskItem = {"id": 1, "delay": 0.1, "good": True}
    result = await process_item(item)

    assert result["id"] == 1
    assert result["status"] == "done"

@pytest.mark.asyncio
async def test_process_item_failure() -> None:
    """Test that a bad item raises a ValueError."""
    item: TaskItem = {"id": 2, "delay": 0.1, "good": False}

    with pytest.raises(ValueError, match="Task 2 failed"):
        await process_item(item)

@pytest.mark.asyncio
async def test_process_item_structure() -> None:
    """Test basic correctness of the returned structure."""
    item: TaskItem = {"id": 3, "delay": 0.1, "good": True}
    result = await process_item(item)

    assert isinstance(result, dict)
    assert "id" in result
    assert "status" in result
    assert result["status"] == "done"