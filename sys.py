import sys

# Example command: python script.py data.txt 42
print(f"Script name: {sys.argv[0]}")

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
    print(f"Second argument: {sys.argv[2]}")
