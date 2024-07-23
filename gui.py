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
    col_num = 5
    row_num = 5

    with dpg.table(
        header_row = True, 
        row_background = True,

        borders_innerH = True, 
        borders_innerV = True, 
        borders_outerH = True, 
        borders_outerV = True, 

        #resizable = True,
        #policy = mvTable_SizingFixedFit
    ):
        for i in range(col_num):
            dpg.add_table_column(label = f'c{i + 1}')

        for r in range(row_num):
            with dpg.table_row():
                for c in range(col_num):
                    dpg.add_input_double(label = f'r{r + 1}', source = source_dtype())


# Creating window and exceution loop of app
dpg.create_viewport(title = 'Linear algebra app', width = 1000, height = 500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('pri', True)
dpg.start_dearpygui()
dpg.destroy_context()