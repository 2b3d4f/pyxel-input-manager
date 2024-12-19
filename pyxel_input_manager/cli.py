import sys
from . import demo

def main():
    """CLI entry point."""
    if len(sys.argv) < 2:
        print("Available commands:")
        print("  demo    - Run the input manager demo")
        return

    command = sys.argv[1]
    if command == "demo":
        demo.main()
    else:
        print(f"Unknown command: {command}")
        print("Available commands:")
        print("  demo    - Run the input manager demo")

if __name__ == "__main__":
    main()
