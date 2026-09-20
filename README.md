# Internet Speed Test

A simple Python CLI utility for measuring download speed over HTTP.

The script performs **10 sequential HTTP requests** to the specified URL, waits for each response to be completely downloaded, and calculates:

* request time for each request;
* downloaded data size;
* average request time;
* total downloaded data;
* average download speed in **MB/s**.

## Requirements

* Python 3.9+
* Internet connection
* No external Python packages required

The project uses only Python's standard library.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/internet-speed-test.git
cd internet-speed-test
```

## Usage

Run the script and provide a URL as a command-line argument:

```bash
python speed_test.py "https://speed.cloudflare.com/__down?bytes=10000000"
```

On Windows, you can also use:

```powershell
py speed_test.py "https://speed.cloudflare.com/__down?bytes=10000000"
```

or:

```powershell
py -m speed_test "https://speed.cloudflare.com/__down?bytes=10000000"
```

### Test URL

The following public Cloudflare endpoint can be used for testing:

```text
https://speed.cloudflare.com/__down?bytes=10000000
```

The `bytes=10000000` parameter requests approximately **10 MB of data**.

For a larger test, you can increase the requested size:

```powershell
py speed_test.py "https://speed.cloudflare.com/__down?bytes=50000000"
```

## Example Output

```text
URL: https://speed.cloudflare.com/__down?bytes=10000000
Requests: 10

Request  1:    10.00 MB,   0.842 s,   11.88 MB/s
Request  2:    10.00 MB,   0.801 s,   12.48 MB/s
Request  3:    10.00 MB,   0.917 s,   10.91 MB/s
Request  4:    10.00 MB,   0.856 s,   11.68 MB/s
Request  5:    10.00 MB,   0.824 s,   12.14 MB/s
Request  6:    10.00 MB,   0.891 s,   11.22 MB/s
Request  7:    10.00 MB,   0.803 s,   12.45 MB/s
Request  8:    10.00 MB,   0.879 s,   11.38 MB/s
Request  9:    10.00 MB,   0.846 s,   11.82 MB/s
Request 10:    10.00 MB,   0.831 s,   12.03 MB/s

Results
----------------------------------------
Successful requests: 10/10
Average request time: 0.849 s
Downloaded data:       100.00 MB
Average speed:         11.80 MB/s
```

The actual values will depend on the network connection, routing, server location, and current network conditions.

## How It Works

The requests are executed **sequentially**:

```text
Request 1
   ↓
Wait for complete response
   ↓
Measure time and downloaded bytes
   ↓
Request 2
   ↓
...
   ↓
Request 10
```

For every successful request, the download speed is calculated as:

```text
speed = downloaded_bytes / request_time
```

The result is converted from bytes per second to decimal megabytes per second:

```text
MB/s = bytes/s / 1,000,000
```

The final average speed is calculated using the total amount of successfully downloaded data and the total download time:

```text
average_speed = total_downloaded_bytes / total_download_time
```

## Error Handling

If an individual request fails, the error is printed and the script continues with the remaining requests.

For example:

```text
Request  3: ERROR - HTTP Error 404: Not Found
```

Failed requests are excluded from the final calculations.

If all requests fail, the program exits with:

```text
All requests failed.
```

## Timeout

The default timeout for each HTTP request is **30 seconds**.

It can be changed using the `--timeout` option:

```powershell
py speed_test.py "https://speed.cloudflare.com/__down?bytes=10000000" --timeout 60
```

## Project Structure

```text
internet-speed-test/
├── speed_test.py
├── README.md
└── .gitignore
```

## Technical Details

* Python 3
* `urllib.request` for HTTP requests
* `time.perf_counter()` for high-resolution timing
* `statistics.mean()` for calculating average request time
* Sequential request execution
* Complete response body is read before starting the next request
* No external dependencies

## Limitations

This script measures **HTTP download throughput to a specific server**. It is not intended to be a full replacement for services such as Speedtest.

The measured speed can be affected by:

* distance to the server;
* network latency;
* routing;
* server load;
* ISP bandwidth;
* Wi-Fi or Ethernet conditions;
* VPN or proxy usage;
* network congestion.

Therefore, the result may differ from the speed reported by other speed-testing services.

## License

This project is provided for educational and testing purposes.
