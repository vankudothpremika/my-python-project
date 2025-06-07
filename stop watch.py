import time

def stopwatch():
    print("Press ENTER to start the stopwatch. Press CTRL+C to stop.")
    input()  # Wait for user to press Enter
    start_time = time.time()  # Record start time
    print("Stopwatch started...")

    try:
        while True:
            elapsed_time = time.time() - start_time
            print(f"\rElapsed Time: {elapsed_time:.2f} seconds", end="")
            time.sleep(0.1)  # Update every 0.1 seconds
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        print(f"Total Time: {elapsed_time:.2f} seconds")

stopwatch()
