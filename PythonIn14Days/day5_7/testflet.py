import flet as ft


def main(page: ft.Page):
    count = 0
    def increment(e):
        nonlocal count
        count += 1
        text.value = f"Count: {count}"
        page.update()

    text = ft.Text(value="Count: 0")
    page.add(text, ft.ElevatedButton("Increment", on_click=increment))

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)