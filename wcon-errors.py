import requests
import time

def make_request(url):
    response = requests.get(url)
    return response.status_code

def main():
    url = input("Enter the URL of the website: ")
    interval = float(input("Enter the interval time (in seconds): "))

    errors = []
    while True:
        status_code = make_request(url)

        if status_code >= 400 and status_code <= 599:
            errors.append(status_code)

        if errors:
            print("The following errors have been found:", errors)

        time.sleep(interval)

if __name__ == "__main__":
    main()
