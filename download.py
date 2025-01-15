import urllib.request
import json
import logging
import constants

def download(url):
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
    except urllib.error.URLError as e:
        logging.error(f"Error accessing the URL: {e}")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")

    return data

def download_and_save(url, path):
    data = download(url)

    try:
        f = open(path, 'xb')
        f.append(data)
        f.close()
    except Exception as e:
        logging.error("Unable to write file to disk")
        f.close()

    return data

def sat_data_download():
    return download(constants.SAT_DATA_URL)

def sat_data_download_save(path):
    return download_and_save(constants.SAT_DATA_URL, path)