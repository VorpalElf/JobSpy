import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

input_file = "Proxies/proxies_list.txt"
output_file = "Proxies/working_proxies.txt"

with open(input_file) as f:
    proxies = [line.strip() for line in f if line.strip()]

total_proxies = len(proxies)
working = []
success_count = 0
failed_count = 0

max_response_time = 7  # seconds

def check_proxy(proxy):
    try:
        start = time.time()
        resp = requests.get(
            "https://www.linkedin.com",
            proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"},
            timeout=5
        )
        elapsed = time.time() - start
        if resp.status_code == 200 and elapsed <= max_response_time:
            return (proxy, True, elapsed, resp.status_code, None)
        else:
            return (proxy, False, elapsed, resp.status_code, None)
    except Exception as e:
        return (proxy, False, None, None, str(e))

with ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(check_proxy, proxy): proxy for proxy in proxies}
    for idx, future in enumerate(as_completed(futures), 1):
        proxy, success, elapsed, status, error = future.result()
        if success:
            print(f"{proxy}: OK ({elapsed:.2f}s)")
            working.append(proxy)
            success_count += 1
        else:
            if error:
                print(f"{proxy}: Failed ({error})")
            else:
                print(f"{proxy}: Status {status} ({elapsed:.2f}s)")
            failed_count += 1
        print(f"Progress: {idx}/{total_proxies}\n")

with open(output_file, "w") as f:
    for proxy in working:
        f.write(proxy + "\n")

print(f"Working proxies saved to {output_file}")
print(f"Successful proxies: {success_count}/{total_proxies}")
print(f"Failed proxies: {failed_count}/{total_proxies}")