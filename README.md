# EvilSeeker 🔭

Tool for searching with google dorking in a faster and specific way with proxies or without proxies.

## Installation 📂

```bash
git clone https://github.com/j4f3th/evilSeeker 
cd evilSeeker
pip install -r requirements.txt
chmod +x evilSeeker.py
```

## Usage 📖

```bash
options:
  -h, --help            show this help message and exit
  -d DORK, --dork DORK  The google dork. Example: inurl:"index.php"
  -n NUMBERESULT, --numberesult NUMBERESULT
                        Number of results. Example: 5
  -l LANGUAGE, --language LANGUAGE
                        Language of pages. Example: 'en'
  -r REGION, --region REGION
                        Region of pages. Example: us (Check: https://developers.google.com/custom-search/docs/json_api_reference#countryCodes)),
  -s SLEEP, --sleep SLEEP
                        Time interval in seconds. Example: 10
  -p PROXY, --proxy PROXY
                        Proxy to use. Example: "127.0.0.1:9050"
```

## Example 🔎

~~~bash
./evilSeeker.py -d 'inurl:index.php?id=' -n 5 -l 'en' -r 'us' -s 3 -p 127.0.0.1:9050
~~~

## DISCLAIMER ⚠️

This tool is for educational use only. The author is not responsible for illegal use. Unauthorized access is a crime in most countries and may carry legal penalties. Use responsibly and only with proper permission.
---
