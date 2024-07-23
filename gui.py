import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.window(tag = 'pri'):
    dpg.add_text('Enter matrix values for solution retrieval where Ax = 0 and Ax = b')

dpg.create_viewport(title = 'Linear algebra app', width = 500, height = 500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('pri', True)
dpg.start_dearpygui()
dpg.destroy_context()