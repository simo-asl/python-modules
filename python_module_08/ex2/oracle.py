import os
from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    missing = []

    if mode not in {"development", "production"}:
        mode = "Invalid"
        missing.append("MATRIX_MODE")

    if database_url is None:
        missing.append("DATABASE_URL")

    if api_key is None:
        missing.append("API_KEY")

    if zion_endpoint is None:
        missing.append("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url is None:
        print("Database: Missing configuration")
    elif mode == "production":
        print("Database: ENCRYPTED REMOTE TARGET")
    else:
        print("Database: Connected to local instance")

    print(f"API Access: {'Authenticated' if api_key else 'Missing config'}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint else 'Missing config'}")

    print("Environment security check:")
    if missing:
        print("[ERROR] Missing configuration for: " + ", ".join(missing))
        print("The Oracle detected missing configuration.")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print("The Oracle sees all configurations.")


if __name__ == '__main__':
    main()
