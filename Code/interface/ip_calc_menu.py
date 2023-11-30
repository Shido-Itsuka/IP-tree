import flet as ft
from flet import TextField, Dropdown, ElevatedButton, Text, Row, Column, Container, Stack, View
from flet_core import View
import sys

sys.path.append('../')
from modules.ip_calculator import IP_Calculator


class IP_Calculator_module(IP_Calculator):

    def __init__(self):
        super().__init__()


theme = ft.Theme(color_scheme_seed='#5a189a')


def clear(e):
    IP_input.value = ""
    IP_input.update()
    Mask_input.value = ""
    Mask_input.update()
    IP_input.focus()


def calculate(e):
    IP_Calculator_module()


body = Row(
    [

        # Контейнер слева
        ft.Container(

            # Строка с контейнерами
            Column(
                controls=[

                    # Кнопка домой + помощь
                    Container(
                        Row(
                            controls=[

                                # Кнопка домой
                                ElevatedButton(
                                    "Home",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=2,
                                    on_click=lambda e: e.page.go("/")
                                ),
                                ft.IconButton(icon=ft.icons.QUESTION_MARK,
                                              tooltip='Руководство',
                                              icon_size=50,
                                              style=ft.ButtonStyle(
                                                  shape=ft.CircleBorder()
                                              )
                                              )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=ft.padding.symmetric(horizontal=40)
                    ),

                    IP_input := TextField(
                        label='Введите IP-адрес',
                        hint_text='127.0.0.1',
                        autofocus=True,
                        text_size=26,
                        max_length=15,
                        input_filter=ft.InputFilter(
                            allow=True,
                            regex_string=r"^[0-9\.]*$",
                            replacement_string='',
                        )

                    ),

                    Mask_input := Dropdown(
                        label='Префикс/Маска',
                        hint_text='Выберите префикс/маску',
                        options=[
                            ft.dropdown.Option(0, "0 - 000.000.000.000"),
                            ft.dropdown.Option(1, "1 - 128.000.000.000"),
                            ft.dropdown.Option(2, "2 - 192.000.000.000"),
                            ft.dropdown.Option(3, "3 - 224.000.000.000"),
                            ft.dropdown.Option(4, "4 - 240.000.000.000"),
                            ft.dropdown.Option(5, "5 - 248.000.000.000"),
                            ft.dropdown.Option(6, "6 - 252.000.000.000"),
                            ft.dropdown.Option(7, "7 - 254.000.000.000"),
                            ft.dropdown.Option(8, "8 - 255.000.000.000"),
                            ft.dropdown.Option(9, "9 - 255.128.000.000"),
                            ft.dropdown.Option(10, "10 - 255.192.000.000"),
                            ft.dropdown.Option(11, "11 - 255.224.000.000"),
                            ft.dropdown.Option(12, "12 - 255.240.000.000"),
                            ft.dropdown.Option(13, "13 - 255.248.000.000"),
                            ft.dropdown.Option(14, "14 - 255.252.000.000"),
                            ft.dropdown.Option(15, "15 - 255.254.000.000"),
                            ft.dropdown.Option(16, "16 - 255.255.000.000"),
                            ft.dropdown.Option(17, "17 - 255.255.128.000"),
                            ft.dropdown.Option(18, "18 - 255.255.192.000"),
                            ft.dropdown.Option(19, "19 - 255.255.224.000"),
                            ft.dropdown.Option(20, "20 - 255.255.240.000"),
                            ft.dropdown.Option(21, "21 - 255.255.248.000"),
                            ft.dropdown.Option(22, "22 - 255.255.252.000"),
                            ft.dropdown.Option(23, "23 - 255.255.254.000"),
                            ft.dropdown.Option(24, "24 - 255.255.255.000"),
                            ft.dropdown.Option(25, "25 - 255.255.255.128"),
                            ft.dropdown.Option(26, "26 - 255.255.255.192"),
                            ft.dropdown.Option(27, "27 - 255.255.255.224"),
                            ft.dropdown.Option(28, "28 - 255.255.255.240"),
                            ft.dropdown.Option(29, "29 - 255.255.255.248"),
                            ft.dropdown.Option(30, "30 - 255.255.255.252"),
                            ft.dropdown.Option(31, "31 - 255.255.255.254"),
                            ft.dropdown.Option(32, "32 - 255.255.255.255")

                        ],
                        text_size=22,

                    ),

                    # Кнопка очистить + подсчитать
                    Container(
                        Row(
                            controls=[
                                ElevatedButton(
                                    "Очистить",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.DELETE,
                                    on_click=clear
                                ),

                                ft.OutlinedButton(
                                    "Подсчитать",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.CHECK,
                                    on_click=calculate
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                        ),
                        padding=ft.padding.symmetric(horizontal=40)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            width=700,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60
        ),

        # Контейнер справа
        Container(
            Column(

            ),
            expand=True,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60
        )

    ],
    expand=True,
    spacing=30
)


def _view_() -> View:
    return View(
        "/ipcalc",
        controls=[
            body
        ],
        padding=30
    )
