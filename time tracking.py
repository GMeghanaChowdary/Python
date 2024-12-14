import time
def time_tracker():
    start_time = time.time()
    input("Press Enter to start tracking your time...")
    time.sleep(5)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time tracked: {total_time} seconds")
time_tracker()
