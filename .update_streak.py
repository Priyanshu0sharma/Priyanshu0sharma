from datetime import datetime

def log_streak():
    # Get current UTC timestamp
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = f"System check at: {now}\n"

    # Append to hidden streak log file
    with open(".streak_log.txt", "a", encoding="utf-8") as f:
        f.write(entry)

if __name__ == "__main__":
    log_streak()
