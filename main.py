import flet as ft
# from flet import MaterialStateProperty


def main(page: ft.Page):
    # page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    page.title = "Calculator"
    page.update()
    txt_result = ft.TextField(text_align="right", expand=True)

    def btn_click(e):
        # print(btn.text)
        if e.control.text == "C":
            txt_result.value = ""
        elif e.control.text == "=":
            try:
                txt_result.value = str(eval(txt_result.value.replace('^', '**')))
            except:
                txt_result.value = "Error"
        else:
            txt_result.value += e.control.text
        txt_result.update()
    buttons = [['7', '8', '9', '+', 'C'], ['4', '5', '6', '-', '^'], ['1', '2', '3', '*', '/'], ['0', '.', '=', '%', '//']]
    for row in buttons:
        print(row)
        row_buttons = []
        for btn_txt in row:
            print(btn_txt)
            btn_style = ft.ButtonStyle(
                            color={
                            ft.MaterialState.HOVERED: ft.colors.BLUE,
                            ft.MaterialState.FOCUSED: ft.colors.GREEN_300,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK87,},
                            bgcolor={ft.MaterialState.FOCUSED: ft.colors.PINK_200, "": ft.colors.WHITE},
                            padding={ft.MaterialState.HOVERED: 20},
                            overlay_color=ft.colors.TRANSPARENT,
                            elevation={"pressed": 0, "": 1},
                            animation_duration=500,
                            side={
                                ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.BLUE),
                                ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.BLUE),
                            },
                            shape={
                                ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=20),
                                ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=2),
                            },
                            )
            btn = ft.TextButton(text=btn_txt, on_click=btn_click, expand=True , icon_color="white" , style=btn_style)
            row_buttons.append(btn)
        page.add(ft.Row(row_buttons, expand=True))
    page.add(txt_result)

ft.app(main)