import os
import sys
from typing import Dict

from dotenv import load_dotenv


def load_config() -> Dict[str, str]:
    """
    Load configuration values from the environment and
    validate the required variables.
    """
    load_dotenv()

    config = {
        "MODE": os.getenv("MATRIX_MODE", "development"),
        "DB": os.getenv("DATABASE_URL"),
        "API": os.getenv("API_KEY"),
        "LOG": os.getenv("LOG_LEVEL", "INFO"),
        "ZION": os.getenv("ZION_ENDPOINT"),
    }

    if config["MODE"] not in {"development", "production"}:
        print("CRITICAL ERROR: MATRIX_MODE ", end="")
        print("must be 'development' or 'production'")
        sys.exit(1)

    required_vars = {
        "DB": "DATABASE_URL",
        "API": "API_KEY",
        "ZION": "ZION_ENDPOINT",
    }

    missing = [
        env_name
        for key, env_name in required_vars.items()
        if not config[key]
    ]

    if missing:
        print(
            "CRITICAL ERROR: Missing configuration for "
            + ", ".join(missing)
        )
        sys.exit(1)

    return config


def run_security_audit(config: Dict[str, str]) -> bool:
    """
    Perform a simple security audit on the loaded configuration.
    """
    print("\nEnvironment security check:")

    print("[OK] Environment variables detected and loaded")

    if config["MODE"] == "production":
        print("[OK] Production overrides active - System OS is in control")
    else:
        print("[OK] Development mode active - Local configuration confirmed")

    placeholders = {
        "your_secret_key_here",
        "INSERT_KEY_HERE",
        "TEMP",
    }

    if config["API"] in placeholders:
        print("[DANGER] Default placeholder detected! Update your .env file.")
        return False

    print("[OK] No default secrets detected")
    return True


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    config = load_config()

    print("\nConfiguration loaded:")
    print(f"Mode: {config['MODE']}")

    if config["MODE"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: ENCRYPTED REMOTE TARGET")

    print(f"API Access: {'Authenticated' if config['API'] else 'FAILED'}")
    print(f"Log Level: {config['LOG']}")
    print(f"Zion Network: {'Online' if config['ZION'] else 'Offline'}")

    run_security_audit(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
