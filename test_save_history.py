import json
import os

from Main import history_file

history_file = "test_save_history.json"



def test_save_history():
    test_file_path = "test_file.txt"
    test_download_link = "http://file.io/sdfsdfsdvdsd"

    save_history(test_file_path, test_download_link)

    with open("test_save_history.json", "r") as f:
        history = json.load(f)
        assert len(history) == 1
        assert history[0]["file_path"] == test_file_path
        assert history[0]["download_link"] == test_download_link

    os.remove("test_save_history.json")

test_save_history()
