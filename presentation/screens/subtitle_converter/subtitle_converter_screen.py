import flet

from flet import (
    Container,
    Icon,
    Page,
    Text,
    TextField,
    ElevatedButton,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin, FilePicker)

from controller.subtitle.subtitle_controller import SubtitleController
from controller.subtitle.subtitle_controller_chineseAnime import SubtitleControllerChineseAnime
from controller.subtitle.subtitle_controller_dailymotion import SubtitleCotrollerV2
from presentation.widgets.app_bar.home_appbar import HomeAppBar


class SubtitleConverterScreen:
    controller: SubtitleController = SubtitleController()
    controller2: SubtitleCotrollerV2 = SubtitleCotrollerV2()
    chineseAnimeController: SubtitleControllerChineseAnime = SubtitleControllerChineseAnime()
    page: Page

    def handleTextChange(self, e):
        self.controller.setText(e)
        self.controller2.setText(e)
        self.chineseAnimeController.setText(e)

    def handleNameChange(self, e):
        self.controller2.setFileName(e)


    def present_home(self, page: Page):
        self.page = page
        self.pageIndex = 0,
        self.page.appbar = HomeAppBar(self.page).getHomeAppBar()
        self.page.add(flet.Container())

        lv = flet.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(TextField(on_change=self.handleTextChange))
        lv.controls.append(TextField(on_change=self.handleNameChange,hint_text="Label for files dailymotion"))


        lv.controls.append(
            ElevatedButton(text="Submit ChineseAnime",
                           on_click=self.chineseAnimeController.generateSubtileFromChineseAnime))
        lv.controls.append(
            ElevatedButton(text="Submit Donghuaguoman", on_click=self.controller.generateSubtileFromDonghuaManJson))
        lv.controls.append(
            ElevatedButton(text="Submit Dailymotion", on_click=self.controller2.generateSubtileFromDailymotionJsJson))
        lv.controls.append(flet.ElevatedButton(
            "Pick files",
            icon=flet.icons.UPLOAD_FILE,
            on_click=lambda _: self.controller.pick_file_to_convert,
        ), )
        self.page.add(lv)
