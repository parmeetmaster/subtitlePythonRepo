import flet
from flet import Page, icons

from presentation.screens.subtitle_converter.subtitle_converter_screen import SubtitleConverterScreen
from presentation.widgets.app_bar.home_appbar import HomeAppBar


class HomeScreen:
    page: Page

    def open_subtitle(self):
       flet.app(target=SubtitleConverterScreen().present_home)



    def present_home(self, page: Page):
        self.page = page
        self.pageIndex=0,
        self.page.add(flet.ElevatedButton(on_click= self.open_subtitle))
