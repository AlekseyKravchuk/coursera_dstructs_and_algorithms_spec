import requests
import json
import os

if __name__ == '__main__':
    dir_path = '/home/kav/PycharmProjects/coursera_dstructs_and_algorithms_spec/00_experiments/sources'
    file_name = 'chicago_crimes_2001_2021.json'
    url = 'https://data.cityofchicago.org/resource/ijzp-q8t2.json'
    target_fname = os.path.join(dir_path, file_name)

    if not os.path.isfile(target_fname):
        try:
            resp = requests.get(url, timeout=7)
            resp.raise_for_status()
            json_data = requests.get(url).json()

            # To actually write the data to the file, we just call the dump() function from json library
            with open(target_fname, 'w') as json_file:
                json.dump(json_data, json_file)
        except requests.exceptions.HTTPError as err_http:
            print("Http Error:", err_http)
        except requests.exceptions.ConnectionError as err_connection:
            print("Error Connecting:", err_connection)
        except requests.exceptions.Timeout as err_timeout:
            print("Timeout Error:", err_timeout)
        except requests.exceptions.RequestException as err:
            print("OOps: Something Else", err)




