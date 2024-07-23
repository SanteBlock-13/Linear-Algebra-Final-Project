import dearpygui.dearpygui as dpg

# Creating context (state where dpg commands can be accessed) of dpg app
dpg.create_context()

# Setting window attributes of app
def source_dtype():
    """ Set data type of matrix values received from user """
    return 'double_value'

with dpg.window(tag = 'pri'):
    # Opening prompt of app
    dpg.add_text('Enter matrix values for solution retrieval where Ax = 0 and Ax = b')

    # Creating columns and rows of matrix value input area
    col_num, row_num = 2
    with dpg.table(header_row = False):
        for i in range(col_num):
            with dpg.table_row():
                for j in range(row_num):
                    dpg.add_input_double()


# Creating window and exceution loop of app
dpg.create_viewport(title = 'Linear algebra app', width = 500, height = 500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('pri', True)
dpg.start_dearpygui()
dpg.destroy_context()