import sys
from importlib import import_module
from typing import Dict


def check_dependencies() -> Dict[str, str]:
    """
    Check whether the required modules are installed.
    Return a dictionary containing the detected versions.
    """
    required = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    found_versions = {}
    missing = []

    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    for package, description in required.items():
        try:
            module = import_module(package)
            version = getattr(module, "__version__", "Unknown version")
            found_versions[package] = version
            print(f"[OK] {package} ({version}) - {description}")
        except ModuleNotFoundError:
            print(f"[MISSING] {package} - {description}")
            missing.append(package)

    if missing:
        print("\n[ERROR] Incomplete upload. Missing programs detected.\n")
        print("Install the required packages with one of these commands:")
        print("pip install -r requirements.txt")
        print("poetry install")
        sys.exit(1)

    return found_versions


def analyze_matrix_data() -> None:
    """
    Simulate Matrix data analysis and generate a simple plot.
    """
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data_points = 1000
    print(f"Processing {data_points} data points...")

    time = np.linspace(0, 10, data_points)
    signal = np.sin(time) + np.random.normal(0, 0.2, data_points)

    data_frame = pd.DataFrame({
        "Time": time,
        "Signal": signal,
    })

    plt.figure(figsize=(10, 5))
    plt.plot(data_frame["Time"], data_frame["Signal"])
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal Strength")

    output_file = "analysis.png"

    print("Generating visualization...")
    plt.savefig(output_file)

    print("\nAnalysis complete!")
    print(f"Results saved to: ./{output_file}")


def show_comparison() -> None:
    """
    Display a short comparison between pip and Poetry.
    """
    print("\n" + "=" * 50)
    print("DEP-MAN COMPARISON: pip vs Poetry")
    print("=" * 50)
    print("pip (requirements.txt):")
    print(" - Common and simple dependency installation method.")
    print(" - Often used with a manually created virtual environment.")
    print("\nPoetry (pyproject.toml):")
    print(" - Modern dependency manager.")
    print(" - Can manage dependencies and virtual environments together.")
    print(" - Uses a lock file for more reproducible installations.")
    print("=" * 50)


def main() -> None:
    check_dependencies()
    analyze_matrix_data()
    show_comparison()


if __name__ == "__main__":
    main()
