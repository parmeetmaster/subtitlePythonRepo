import json
import urllib
from urllib.parse import urlparse
import urllib.request as req

import requests
import re
from flet import Page
import os
import pathlib
import datetime
from controller.subtitle.vtt_to_srt import ConvertFile
from models.donghua_guo_man.donghuaman_model import DongManModel, dong_man_model_from_dict
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
        current_time = datetime.datetime.now()
        folder_date_time_text:str = str(current_time.date().day)+"-"+str(current_time.date().month)+"-"+str(current_time.date().year)

        #print(r.text)
        try:
            desktop = pathlib.Path.home() / 'Desktop'/folder_date_time_text / title/"sat"/''
            self._createOrDetectDirectoryExist(str(desktop))
            dir_path=str(desktop)+"-"+title+"-"+sbModel.label+"-"+self.getNameConvention(sbModel.label)+".vtt"




            ff = open(dir_path, mode='wb')
            r.content.replace(b"\n", b"", 1)
            ff.write(r.content.replace(b"chineseanime.co.in",bytes(b"Animekill Mobile App At Google Playstore")).replace(b"donghuastream.com",bytes(b"Animekill Mobile App At Google Playstore")).replace(b"anichik.com",bytes(b"Animekill Mobile App At Google Playstore"))
                     .replace(b"Donghuastream.com",bytes(b"Animekill Mobile App At Google Playstore")).replace(b"https:",bytes(b"")))



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
    def replaceSpaces(input:str)->str:
        rep = "%20"
        for i in range(len(input)):
            if (input[i] == ' '):
                input = input.replace(input[i], rep)

        return input
    def generateSubtileFromDonghuaManJson(self, e):
        #print(self.json_str)
        dongModel: DongManModel = dong_man_model_from_dict(json.loads(self.json_str))
        #print(len(dongModel.tracks))
        #complete_url_data=urlparse("https:\/\/www.donghuaplay.com\/subtitle.vtt?url=https%3A%2F%2Fdonghuaplay.com%2Fuploads%2Fsubtitles%2Ftales%20278_English_Persian-vnU-HlsqOr8dJgK.vtt")
        #print(urllib.parse.unquote(complete_url_data.query))
        for val in dongModel.tracks:
            complete_url_data = urlparse(val.file)
            decode_url=urllib.parse.unquote(complete_url_data.query)
            final_url:str=str(decode_url).replace("url=","")
            self._createSrtFiles(Sub(file=final_url,label=val.label),dongModel.title)









