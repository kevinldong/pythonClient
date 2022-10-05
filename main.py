import argparse
import requests
from pathlib import Path
import sys
from bs4 import BeautifulSoup


def die(status_code: int, message: str):
    """ Utility function to print a message and exit"""
    print(message)
    sys.exit(status_code)


def main():
    # Setup argparse
    parser = argparse.ArgumentParser(description="Client for testing the server/ids")
    parser.add_argument('action', type=str, choices=['upload', 'download', 'u', 'd'],
                        help="whether to upload or download a file")
    parser.add_argument('file', type=str, help="the path of the file to download or upload")
    parser.add_argument('-o', '--output', type=str, default="out.png", help="location to save the downloaded file")
    parser.add_argument('url', type=str, help="url to the website being tested")
    args = parser.parse_args()

    # Setup variables
    url = args.url

    # Initialize session
    session = requests.Session()
    if args.action == 'upload' or args.action == 'u':
        # Verify that file exists
        path = Path(args.file)
        if not path.is_file():
            die(1, "ERROR: couldn't find file")

        print(f"[+] Uploading {path.absolute()} to {url}")
        # Get csrf_token
        print("[+] Getting csrf_token")
        homepage = session.get(f"{url}/")
        if homepage.status_code != 200:
            die(1, "ERROR: couldn't retrieve homepage")
        soup = BeautifulSoup(homepage.content, "html.parser")
        csrf_token = soup.find("input", {"name": "csrf_token"})['value']
        print("[+] Uploading file")
        # Upload file
        files = {'file': open(path.absolute(), "rb")}
        r = session.post(url, files=files, data={"csrf_token": csrf_token, "submit": True})
        if r.status_code == 200:
            print("[+] Successfully uploaded file")
        else:
            print("ERROR: failed to upload file")

    if args.action == 'download' or args.action == 'd':
        print(f"[+] Attempting to download {args.file} from {url}")
        r = session.get(f"{url}/{args.file}/")
        if r.status_code != 200:
            print("ERROR: failed to download file")
            print(r.text)
        else:
            print("[+] Got file; saving")
            with open(args.output, "wb") as outfile:
                outfile.write(r.content)


if __name__ == "__main__":
    main()
