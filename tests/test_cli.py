import json
import subprocess
from pathlib import Path
from typing import Any
import pytest

def run_cli(input_file: Path, *args: str) -> subprocess.CompletedProcess[str]:
    """Helper function to execute the CLI tool via subprocess."""
    cmd = ["python", "-m", "src.async_tool", str(input_file)] + list(args)
    return subprocess.run(cmd, capture_output=True, text=True, timeout=5)

@pytest.fixture
def valid_input(tmp_path: Path) -> Path:
    """Fixture to provide a valid temporary JSON input file."""
    file_path = tmp_path / "valid.json"
    data = [
        {"id": 1, "delay": 0.1, "good": True},
        {"id": 2, "delay": 0.1, "good": True}
    ]
    file_path.write_text(json.dumps(data))
    return file_path

@pytest.fixture
def failing_input(tmp_path: Path) -> Path:
    """Fixture to provide a temporary JSON input file with one failing task."""
    file_path = tmp_path / "failing.json"
    data = [
        {"id": 1, "delay": 0.1, "good": True},
        {"id": 2, "delay": 0.1, "good": False},
        {"id": 3, "delay": 0.1, "good": True}
    ]
    file_path.write_text(json.dumps(data))
    return file_path

def test_basic_execution(valid_input: Path) -> None:
    """Test 1: Basic execution with valid input."""
    result = run_cli(valid_input)
    assert result.returncode == 0
    
    output = json.loads(result.stdout)
    assert isinstance(output, list)

def test_mode_behavior(valid_input: Path) -> None:
    """Test 2: Mode behavior using async mode."""
    result = run_cli(valid_input, "--mode", "async")
    assert result.returncode == 0
    
    output = json.loads(result.stdout)
    assert len(output) == 2
    assert output[0]["status"] == "done"
    assert output[1]["status"] == "done"

def test_error_without_flag(failing_input: Path) -> None:
    """Test 3: Error without flag should cause non-zero exit code."""
    result = run_cli(failing_input)
    assert result.returncode != 0

def test_error_with_flag(failing_input: Path) -> None:
    """Test 4: Error with --continue_on_error flag should process the error."""
    # Note: Lab 11 argparse uses --continue_on_error
    result = run_cli(failing_input, "--continue_on_error")
    assert result.returncode == 0
    
    output = json.loads(result.stdout)
    failed_item = next(item for item in output if item["id"] == 2)
    assert failed_item["status"] == "error"
    assert "message" in failed_item

def test_output_structure(valid_input: Path) -> None:
    """Test 5: Output structure preserves order and item counts."""
    result = run_cli(valid_input)
    assert result.returncode == 0
    
    output = json.loads(result.stdout)
    assert isinstance(output, list)
    assert len(output) == 2
    assert output[0]["id"] == 1
    assert output[1]["id"] == 2