from pathlib import Path

# Print the pickup line from entry.txt (path resolved via this file).
print(Path(__file__).with_name("entry.txt").read_text().strip())
