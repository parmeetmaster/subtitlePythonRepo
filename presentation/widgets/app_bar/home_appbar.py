import flet
from flet import Page, icons



class HomeAppBar:
    page: Page

    def __init__(self, page: Page) -> None:
        super().__init__()
        self.page = page

    def button_clicked(self, e):
        print(e.control.data)
        self.page.controls.pop()
        self.page.update()


    def getHomeAppBar(self) -> flet.AppBar:
        return flet.AppBar(
            leading=flet.PopupMenuButton(
                items=[
                    flet.PopupMenuItem(text="Item 1", on_click=self
                                       .button_clicked, data=1),
                    flet.PopupMenuItem(),  # divider
                    flet.PopupMenuItem(text="Item 2", on_click=self.button_clicked, data=2),

                ]
            ),
            leading_width=40,
            title=flet.Text("AppBar Example"),
            center_title=False,
            bgcolor=flet.colors.SURFACE_VARIANT,
        )
