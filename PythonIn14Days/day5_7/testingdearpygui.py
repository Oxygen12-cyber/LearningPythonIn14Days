import dearpygui.dearpygui as dpg

def on_click():
    dpg.log("Clicked")

dpg.create_context()
dpg.create_viewport(title='Example', width=400, height=200)

with dpg.window(label="Example"):
    dpg.add_text("Hello Beautiful UI!")
    dpg.add_button(label="Click me", callback=on_click)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
