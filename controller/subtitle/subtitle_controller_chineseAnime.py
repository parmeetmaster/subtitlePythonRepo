import datetime
import json
import os
import pathlib
import re
import urllib
from urllib.parse import urlparse

import requests
from vtt_to_srt.vtt_to_srt import ConvertFile

from models.dailymotion.dailymotion_model import DailymotionResponseModel, dailymotion_response_model_from_dict
from models.stream_sb_model.stream_sb_model import Sub


class SubtitleControllerChineseAnime:
    input_url: str
    languageArray = ["-es"]

    def setText(self, text):
        self.input_url = text.control.value
        # print(self.json_str)

    def _createSrtFiles(self, sbModel: Sub, title: str):
        r = requests.get(sbModel.file)
        current_time = datetime.datetime.now()
        folder_date_time_text: str = str(current_time.date().day) + "-" + str(current_time.date().month) + "-" + str(
            current_time.date().year)

        # print(r.text)
        try:
            new_title = re.sub(r"[^a-zA-Z0-9 ]", "", title).replace(" ","_")
            desktop = pathlib.Path.home() / 'Desktop' / folder_date_time_text / new_title / "sat" / ''
            self._createOrDetectDirectoryExist(str(desktop))
            dir_path = str(desktop) + "-" + new_title + "-" + sbModel.label + "-" + self.getNameConvention(
                sbModel.label) + ".vtt"
            ff = open(dir_path, mode='wb')
            r.content.replace(b"\n", b"", 1)
            ff.write(r.content.replace(b"Donghua Stream", bytes(b"Animekill Mobile App At Google Playstore")).replace(
                b"donghuastream.com", bytes(b"Animekill Mobile App At Google Playstore")).replace(b"anichik.com", bytes(
                b"Animekill Mobile App At Google Playstore")).replace(b"www", bytes(b""))
            .replace(b"Donghuastream.com", bytes(b"Animekill Mobile App At Google Playstore")).replace(b"https:", bytes(b"")))
            ff.seek(0)
            ff.flush()
            ff.close()
            convert_file = ConvertFile(dir_path, "utf-8")
            dd = convert_file.convert()
            dir_path2 = str(desktop) + "-" + new_title + "-" + sbModel.label + "-" + self.getNameConvention(
                sbModel.label) + ".srt"
            with open(dir_path2, "r+", encoding="utf-8") as f:
                old = f.read()
                print("old is here"+old)
                # read everything in the file
                f.seek(0)  # rewind
                f.write(old.replace("\n", "", 1))  # write the new line before
                f.close()

            # convert_file.convert()
            # os.unlink(dir_path)
            # print(data)
        finally:
            print("finaly")

        # print(dd)

    def _createOrDetectDirectoryExist(self, path: str):
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print("The new directory is created!")

    def getNameConvention(self, label: str):
        if str.lower(label) == "arabic":
            return ".ar_AR"
        elif str.lower(label) == "thai":
            return ".th_TH"
        elif str.lower(label) == "hindi":
            return ".hi_IN"
        elif str.lower(label) == "english":
            return ".en_US"
        elif str.lower(label) == "indonesian":
            return ".id_ID"
        elif str.lower(label) == "french":
            return ".fr_FR"
        elif (str.lower(label) == "khmer") or (str.lower(label) == "cambodian"):
            return ".km_KH"
        elif str.lower(label) == "malay":
            return ".ms_MY"
        elif str.lower(label) == "portuguese":
            return ".pt_PT"
        elif str.lower(label) == "polish":
            return ".pl_PL"
        elif str.lower(label) == "italian":
            return ".it_IT"
        elif str.lower(label) == "persian":
            return ".fa_IR"
        elif str.lower(label) == "vietnamese":
            return ".vi_VN"
        elif str.lower(label) == "turkish":
            return ".tr_TR"
        elif str.lower(label) == "persian":
            return ".fa_IR"
        elif str.lower(label) == "russian":
            return ".ru_RU"
        elif str.lower(label) == "spanish":
            return ".es_MX"
        elif str.lower(label) == "german":
            return ".de_DE"
        elif str.lower(label) == "bengali":
            return ".bn_IN"


        else:
            return ""


    def replace_language_code(self, url, new_code):
        # Define the current language code to replace
        current_code = "-en"

        # Create the regular expression pattern
        pattern = re.compile(re.escape(current_code))

        # Replace the current language code with the new one
        updated_url = pattern.sub(new_code, url)
        pattern = re.compile(r'(?<!https:)//')
        updated_url = pattern.sub('/', updated_url)

        return updated_url

    def generateSubtileFromChineseAnime(self, e):
        # print(self.json_str)
        print(self.input_url)
        original_url = "https://httpcomfast.co.in//xapi/sub/lf/jNI/GB/a4vjo-en.vtt"
        for curruntLanguage in self.languageArray:
            updated_url = self.replace_language_code(original_url, curruntLanguage)
            self._createSrtFiles(Sub(updated_url,"English"),"tos")

        return 0
