import flet as ft
from flet import (TextField, Dropdown, ElevatedButton, Text, Row, Column, Container, Stack, View, TextButton, DataCell,
                  DataTable, DataRow, DataColumn)
from flet_core import View, ControlEvent
import sys

sys.path.append('../')

# noinspection PyUnresolvedReferences
from modules.ip_calculator import IP_Calculator

# noinspection PyUnresolvedReferences
from modules.ip_tree_calculator import IP_Tree_Calculator

theme = ft.Theme(color_scheme_seed='#5a189a',
                 color_scheme=ft.ColorScheme(
                     background='#0f0f0f',
                     primary_container='#272727'

                 ))


def validate(e: ControlEvent) -> None:
    if all([IP_input.value, Nodes_input.value]):
        calc_button.disabled = False
    else:
        calc_button.disabled = True
    calc_button.update()


def clear(e):
    IP_input.value = ""
    IP_input.error_text = ""
    IP_input.update()

    Mask_input.value = ""
    Mask_input.update()

    IP_input.focus()
    calc_button.disabled = True
    calc_button.update()


def calculate(e):
    try:
        out = IP_Calculator(IP_input.value, int(Mask_input.value)).main()
        print('\n\n', '-'*55, sep='')
        [print(*x, sep=' | ', end='\n') for x in out]
        print('-'*55, end='\n\n')

    except ValueError as e:
        print(e)
        IP_input.error_text = e
        IP_input.update()
    else:
        IP_input.error_text = ""
        IP_input.update()


def error_clear(e: ControlEvent) -> None:
    if IP_input.error_text:
        IP_input.error_text = ""
        IP_input.update()


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
                        ),
                        border_color=ft.colors.WHITE54,
                        focused_border_color='#dbb8ff',
                        on_change=validate
                    ),

                    Nodes_input := TextField(
                        label='Введите подсети, разделяя их Enter\'ом',
                        hint_text='500',
                        autofocus=True,
                        text_size=26,
                        multiline=True,
                        border_color=ft.colors.WHITE54,
                        focused_border_color='#dbb8ff',
                        on_change=validate
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

                                calc_button := ft.OutlinedButton(
                                    "Подсчитать",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=5)
                                    ),
                                    scale=1.5,
                                    icon=ft.icons.CHECK,
                                    on_click=calculate,
                                    disabled=True
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
            width=600,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60
        ),

        # Контейнер справа
        Container(
            Column(
                controls=[

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            expand=True,
            bgcolor=ft.colors.BLACK45,
            border_radius=10,
            padding=60,
            alignment=ft.alignment.center
        )

    ],
    expand=True,
    spacing=30,

)


def _view_() -> View:
    return View(
        "/iptree",
        controls=[
            body
        ],
        padding=30
    )
