#!/usr/bin/env python3
"""Simple sequential internet speed tester."""

import argparse
import time
import urllib.request
from statistics import mean


REQUESTS_COUNT = 10
DEFAULT_TIMEOUT = 30


def download(url: str, timeout: int) -> tuple[float, int]:
    """Download the complete response and return (elapsed_seconds, bytes)."""
    started = time.perf_counter()

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "internet-speed-test/1.0"},
    )

    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = response.read()

    elapsed = time.perf_counter() - started
    return elapsed, len(data)


def format_mb(value: float) -> float:
    """Convert bytes to decimal megabytes."""
    return value / 1_000_000


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure download speed using 10 sequential HTTP requests."
    )
    parser.add_argument(
        "url",
        help="URL of a large file/image to download, e.g. https://example.com/file.jpg",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT}).",
    )
    args = parser.parse_args()

    times = []
    total_bytes = 0

    print(f"URL: {args.url}")
    print(f"Requests: {REQUESTS_COUNT}")
    print()

    for number in range(1, REQUESTS_COUNT + 1):
        try:
            elapsed, bytes_downloaded = download(args.url, args.timeout)
        except Exception as exc:
            print(f"Request {number:2d}: ERROR - {exc}")
            continue

        times.append(elapsed)
        total_bytes += bytes_downloaded

        speed_mb_s = bytes_downloaded / elapsed / 1_000_000
        print(
            f"Request {number:2d}: "
            f"{format_mb(bytes_downloaded):8.2f} MB, "
            f"{elapsed:7.3f} s, "
            f"{speed_mb_s:7.2f} MB/s"
        )

    if not times:
        raise SystemExit("All requests failed.")

    total_time = sum(times)
    average_time = mean(times)
    average_speed_mb_s = total_bytes / total_time / 1_000_000

    print()
    print("Results")
    print("-" * 40)
    print(f"Successful requests: {len(times)}/{REQUESTS_COUNT}")
    print(f"Average request time: {average_time:.3f} s")
    print(f"Downloaded data:       {format_mb(total_bytes):.2f} MB")
    print(f"Average speed:         {average_speed_mb_s:.2f} MB/s")


if __name__ == "__main__":
    main()
