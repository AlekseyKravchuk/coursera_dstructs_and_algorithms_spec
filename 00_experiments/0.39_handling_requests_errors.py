import requests

if __name__ == '__main__':
    bad_url = 'https://data.cityofchicago.org/resource/bad_url'
    good_url = 'https://data.cityofchicago.org/resource/ijzp-q8t2.json'

    try:
        r = requests.get(good_url, timeout=3)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print("Http Error:", err_http)
    except requests.exceptions.ConnectionError as err_connection:
        print("Error Connecting:", err_connection)
    except requests.exceptions.Timeout as err_timeout:
        print("Timeout Error:", err_timeout)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)
