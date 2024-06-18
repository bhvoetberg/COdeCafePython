from pathlib import Path

# current working directory
print(Path.cwd())
path = Path.cwd() / "file_management_pathlib.md"
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.parent.parent)

path = Path.cwd() / "file_management_pathlib.md"
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))
