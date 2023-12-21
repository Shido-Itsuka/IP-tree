import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column, Container, Stack
from flet_core.control import Control
import os

from ip_calc_menu import _view_ as ipcalc_view
from ip_tree_menu import _view_ as iptree_view


def main(page: ft.Page) -> None:
    page.title = 'IP-tree'
    page.theme = ft.Theme(color_scheme_seed='#5a189a',
                          color_scheme=ft.ColorScheme(
                              background='#0f0f0f',
                              primary_container='#272727'

                          ))
    page.padding = 0

    page.window_center()

    page.window_maximized = True

    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.window_title_bar_hidden = False
    page.window_title_bar_buttons_hidden = False
    page.window_resizable = False

    # -----------------------------------------------------------------

    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        shape=ft.RoundedRectangleBorder(radius=10),
        modal=True,
        title=ft.Text("Подтвердите Выход"),
        content=ft.Text("Вы уверены, что хотите выйти?"),
        actions=[
            ft.ElevatedButton("Да",
                              on_click=yes_click,
                              style=ft.ButtonStyle(
                                  shape=ft.RoundedRectangleBorder(radius=10)
                              ),
                              ),
            ft.OutlinedButton("Нет",
                              on_click=no_click,
                              style=ft.ButtonStyle(
                                  shape=ft.RoundedRectangleBorder(radius=10)
                              ),
                              ),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    # -----------------------------------------------------------------

    def change_background(e):
        filenames = os.listdir(os.path.join('assets', 'images'))
        background.src = 'images/' + filenames[background_button.data]
        if background_button.data == len(filenames) - 1:
            background_button.data = 0
        else:
            background_button.data += 1
        page.update(background)

    body = Container(
        Stack([
            background := ft.Image(
                src='images/bgpic4.png'
            ),
            Container(
                Row(
                    controls=[
                        Container(
                            Row(
                                controls=[background_button := ft.IconButton(icon=ft.icons.WALLPAPER,
                                                                             tooltip='Смена обоев',
                                                                             icon_size=30,
                                                                             on_click=change_background,
                                                                             data=0
                                                                             )
                                          ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=62.5,
                            height=60,
                            border_radius=10,
                            blur=ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
                            border=ft.border.all(1),
                            alignment=ft.alignment.center,
                        ),
                        Container(
                            Row(
                                controls=[ft.IconButton(icon=ft.icons.SETTINGS,
                                                        tooltip='Настройки',
                                                        icon_size=30,
                                                        ),
                                          ft.IconButton(icon=ft.icons.QUESTION_MARK,
                                                        tooltip='Помощь',
                                                        icon_size=30,
                                                        ),
                                          ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=125,
                            height=60,
                            border_radius=10,
                            blur=ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
                            border=ft.border.all(1),
                            alignment=ft.alignment.center,

                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                alignment=ft.alignment.top_right,
                margin=ft.padding.all(15)
            ),
            Container(
                Container(
                    Row(
                        controls=[
                            ElevatedButton(
                                "IP-Calc",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5)
                                ),
                                scale=2,
                                on_click=lambda _: page.go("/ipcalc")
                            ),
                            ElevatedButton(
                                "IP-Tree",
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=5)
                                ),
                                scale=2,
                                on_click=lambda _: page.go("/iptree")
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    width=500,
                    height=150,
                    border_radius=10,
                    blur=ft.Blur(10, 12, ft.BlurTileMode.MIRROR),
                    border=ft.border.all(1),
                    alignment=ft.alignment.center
                ),
                alignment=ft.alignment.top_center,
                margin=ft.margin.only(top=375),  # 434
            )

        ]),
        alignment=ft.alignment.center,

    )

    page.add(
        body
    )
    page.update()

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    body
                ],
                padding=0
            )
        )
        page.title = 'Main Menu'

        if page.route == "/ipcalc":
            page.views.append(ipcalc_view()),
            page.title = 'IP Calculator'
        page.update()

        if page.route == "/iptree":
            page.views.append(iptree_view())
            page.title = 'IP Tree Calculator'

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main,
           assets_dir='assets'
           )
