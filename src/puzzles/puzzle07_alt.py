from collections import Counter
from pathlib import Path

data = Path(__file__).with_name("07_input.txt").read_text().splitlines()

file_sizes: dict[str, int] = {}
trace = [""]
for line in data[1:]:
    if line == "$ cd ..":
        trace.pop()
    elif line.startswith("$ cd"):
        trace.append(line[5:])
    elif line[0].isnumeric():
        parts = line.split(" ")
        file_sizes["/".join(trace + [parts[1]])] = int(parts[0])

dir_sizes: dict[str, int] = Counter()
for path, size in file_sizes.items():
    for dir in Path(path).parents:
        dir_sizes[str(dir)] += size

# part 1
print(sum(size for size in dir_sizes.values() if size <= 100000))

# part 2
current_free_space = 70000000 - dir_sizes["/"]
min_deletion_size = 30000000 - current_free_space
print(dir_sizes["/"])
print(current_free_space)
print(min_deletion_size)
print(sorted(dir_sizes.values()))
print(next(size for size in sorted(dir_sizes.values()) if size >= min_deletion_size))