def print_header(letter: str, name: str) -> None:
    full_name = f"Task {letter}: {name}"
    print("=" * 50)
    cnt = 50 - len(full_name) - 6
    print(f"{"=" * ((cnt + 1) // 2)}   {full_name}   {"=" * (cnt // 2)}")
    print("=" * 50)