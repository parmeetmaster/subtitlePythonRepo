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

    def generateSubtileFromJson(self, e):
        print(self.json_str)
        sbModel: StreamSbModel = stream_sb_model_from_dict(json.loads(self.json_str))
        print(len(sbModel.stream_data.subs))

        for val in sbModel.stream_data.subs:
            self._createSrtFiles(val,sbModel.stream_data.title)




    def _createSrtFiles(self, sbModel: Sub,title:str):
        r = requests.get(sbModel.file)
        print(r.text)
        try:
            desktop = pathlib.Path.home() / 'Desktop' / title/"sat"/''
            self._createOrDetectDirectoryExist(str(desktop))
            dir_path=str(desktop)+"-"+title+"-"+sbModel.label+".vtt"

            ff = open(dir_path, mode='wb')
            ff.write(r.content.replace(b"chineseanime.co.in",bytes(b"Animekill.com")))
            ff.seek(0)
            ff.flush()
            ff.close()
            convert_file = ConvertFile(dir_path, encoding_format='utf-8')
            convert_file.convert()
            os.unlink(dir_path)
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
