import json
import requests
import re
from flet import Page
import os
import pathlib

from controller.subtitle.vtt_to_srt import ConvertFile
from models.stream_sb_model.stream_sb_model import stream_sb_model_from_dict, StreamSbModel, Sub


class SubtitleController:
    json_str: str

    def setText(self, text):
        self.json_str = text.control.value
        # print(self.json_str)

    def generateSubtileFromStreamSbJson(self, e):
        print(self.json_str)
        sbModel: StreamSbModel = stream_sb_model_from_dict(json.loads(self.json_str))
        print(len(sbModel.stream_data.subs))

        for val in sbModel.stream_data.subs:
            self._createSrtFiles(val,sbModel.stream_data.title)

    def _createSrtFiles(self, sbModel: Sub,title:str):
        r = requests.get(sbModel.file)
        #print(r.text)
        try:
            desktop = pathlib.Path.home() / 'Desktop' / title/"sat"/''
            self._createOrDetectDirectoryExist(str(desktop))
            dir_path=str(desktop)+"-"+title+"-"+sbModel.label+"-"+self.getNameConvention(sbModel.label)+".vtt"

            ff = open(dir_path, mode='wb')
            r.content.replace(b"\n", b"", 1)
            ff.write(r.content.replace(b"chineseanime.co.in",bytes(b"Animekill.com")))
            ff.seek(0)
            ff.flush()
            ff.close()
            convert_file = ConvertFile(dir_path, encoding_format='utf-8')
            dd=convert_file.convert()
            dir_path2 = str(desktop) + "-" + title + "-" + sbModel.label + "-" + self.getNameConvention(
                sbModel.label) + ".srt"
            with open(dir_path2, "r+",encoding="utf-8") as f:
                old = f.read()
                print(old)
                # read everything in the file
                f.seek(0)  # rewind
                f.write(old.replace("\n", "" , 1))# write the new line before
                f.close()


            #convert_file.convert()
            #os.unlink(dir_path)
            # print(data)
        finally:
            print("finaly")

        # print(dd)
    def _createOrDetectDirectoryExist(self,path:str):
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print("The new directory is created!")

    def getNameConvention(self, label:str):
        if str.lower(label)=="arabic":
            return ".ar_AR"
        elif str.lower(label)=="thai":
            return ".th_TH"
        elif str.lower(label)=="hindi":
            return ".hi_IN"
        elif str.lower(label)=="english":
            return ".en_US"
        elif str.lower(label) == "indonesian":
            return ".id_ID"
        elif str.lower(label) == "french":
            return ".fr_FR"
        elif str.lower(label) == "khmer":
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
        else:
            return ""


### donghuaguoman




