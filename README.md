# Internet Speed Test

A small Python CLI utility that measures download speed from the current computer.

The program:

1. accepts a URL from the command line;
2. performs 10 HTTP requests **sequentially**;
3. waits until each response is fully downloaded;
4. measures the time of every request;
5. calculates the average request time;
6. calculates the total amount of downloaded data;
7. calculates aggregate download speed in MB/s.

No external Python packages are required.

## Requirements

- Python 3.9+
- Internet access

## Usage

```bash
python speed_test.py "https://example.com/large-file.jpg"
```

Optional request timeout:

```bash
python speed_test.py "https://example.com/large-file.jpg" --timeout 60
```

Use a reasonably large static file for a meaningful measurement. A small image can make network latency dominate the result.

## Example output

```text
URL: https://example.com/large-file.jpg
Requests: 10

Request  1:     5.20 MB,   0.842 s,    6.18 MB/s
Request  2:     5.20 MB,   0.801 s,    6.49 MB/s
...
Request 10:     5.20 MB,   0.817 s,    6.36 MB/s

Results
----------------------------------------
Successful requests: 10/10
Average request time: 0.823 s
Downloaded data:       52.00 MB
Average speed:         6.32 MB/s
```

## How the speed is calculated

The final speed is calculated from all successfully downloaded bytes divided by the total time spent downloading them:

```text
speed = total_downloaded_bytes / total_download_time
```

The result is converted from bytes/second to decimal MB/s by dividing by 1,000,000.

This is a **download throughput test**, not a full internet benchmark. The result depends on the selected server, file size, routing, latency, server limits, and current network conditions.

## Why requests are sequential

The task requires the 10 requests to run sequentially. The next request starts only after the previous response has been completely read.

## Error handling

A failed request is reported and does not contribute to the final calculation. If all 10 requests fail, the program exits with an error.

## Project structure

```text
internet-speed-test/
├── speed_test.py
├── README.md
└── .gitignore
```

## Upload to GitHub

Create an empty repository on GitHub, then run:

```bash
git init
git add speed_test.py README.md .gitignore
git commit -m "Add internet speed test"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/internet-speed-test.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.
