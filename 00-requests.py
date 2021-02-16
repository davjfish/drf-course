import requests

def main():
    payload = {"base":"CAD", "symbols":"USD,GBP,CAD"}
    response = requests.get("https://api.exchangeratesapi.io/latest", params=payload)
    if response.status_code != 200:
        print("status code:", response.status_code)
        raise Exception("There was a bad status code:", response.status_code)
    else:
        print("content-type:", response.headers.get("Content-Type"))

        data = response.json()
        print("json data:", data)

    # print("content:", response.text)

if __name__ == "__main__":
    main()