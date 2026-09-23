import sys

params = sys.argv[1:]

if not params:
    print("none")
else:
    print(f"parameters: {len(params)}")
    for param in params:
        print(f"{param}: {len(param)}")