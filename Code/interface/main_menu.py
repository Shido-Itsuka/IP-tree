import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.fonts = {
        'Raleway': '/fonts/Raleway-Regular'
    }

    page.title = 'IP-tree'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(font_family='Raleway')

    page.window_center()

    page.window_width = 800
    page.window_height = 500

    page.add(Row(
        controls=[Text(value='Hello, world!', size=40)],
        alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main,
       assets_dir='resources'
       )
