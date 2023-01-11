# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import flet

from presentation.screens.home.home_screen import HomeScreen
from presentation.screens.subtitle_converter.subtitle_converter_screen import SubtitleConverterScreen

flet.app(target=SubtitleConverterScreen().present_home)