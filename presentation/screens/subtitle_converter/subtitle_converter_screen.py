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
from presentation.widgets.app_bar.home_appbar import HomeAppBar


class SubtitleConverterScreen:
    controller: SubtitleController = SubtitleController()
    page: Page



    def present_home(self, page: Page):
        self.page = page
        self.pageIndex = 0,
        self.page.appbar = HomeAppBar(self.page).getHomeAppBar()
        self.page.add(flet.Container())

        lv = flet.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        lv.controls.append(TextField(on_change=self.controller.setText))

        lv.controls.append(ElevatedButton(text="Submit StreamSb", on_click=self.controller.generateSubtileFromStreamSbJson))
        lv.controls.append(ElevatedButton(text="Submit Donghuaguoman", on_click=self.controller.generateSubtileFromDonghuaManJson))
        lv.controls.append(flet.ElevatedButton(
            "Pick files",
            icon=flet.icons.UPLOAD_FILE,
            on_click=lambda _: self.controller.pick_file_to_convert,
        ), )
        self.page.add(lv)
