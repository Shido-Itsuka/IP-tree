import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control import Control


def main(page: ft.Page) -> None:
    page.fonts = {
        'Raleway': '/fonts/Raleway-Regular'
    }

    page.title = 'IP-tree'

    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(font_family='Raleway')

    page.window_center()

    page.window_width = 800
    page.window_height = 500

    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True
    page.window_resizable = False

    page.add(
        Row(
            [
                ft.WindowDragArea(
                    ft.Container(padding=20, bgcolor=ft.colors.WHITE), expand=True),
                ft.IconButton(ft.icons.ZOOM_IN, on_click=lambda _: page.window_to_front()),
                ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close())
            ]
        )
    )

    page.add(
        Row(
            controls=[Text(value='Hello, world!', size=40)],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='resources'
           )
