import os
import site
import sys


def get_site_packages() -> list[str]:
    try:
        if hasattr(site, "getsitepackages"):
            return site.getsitepackages()
    except Exception:
        pass
    return []


def is_virtual_environment() -> bool:
    # Detect if Python is running inside a virtual environment.
    # In a venv, sys.prefix is different from sys.base_prefix.
    # We also check VIRTUAL_ENV because many virtual environments
    # define this environment variable when activated.
    return (
        hasattr(sys, "base_prefix")
        and sys.prefix != sys.base_prefix
    ) or ("VIRTUAL_ENV" in os.environ)


def main() -> None:
    try:
        venv_active = is_virtual_environment()
        site_packages = get_site_packages()
        venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")

        if venv_active:
            venv_name = os.path.basename(venv_path.rstrip("/\\"))

            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {venv_path}\n")

            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting", end="")
            print("the global system.\n")
        else:
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")

            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate  # On Unix")
            print("matrix_env\\Scripts\\activate   # On Windows\n")

        print("Package installation path:")
        if site_packages:
            for package_path in site_packages:
                print(package_path)
        else:
            print("Could not determine site-packages location.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
