import time

def stopwatch():
    print("Press Enter to start the stopwatch and Enter again to stop.")
    input("Press Enter to start...")
    start_time = time.time()
    input("Press Enter to stop...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")

stopwatch()
