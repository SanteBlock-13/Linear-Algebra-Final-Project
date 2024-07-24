import dearpygui.dearpygui as dpg

# Creating context (state where dpg commands can be accessed) of dpg app
dpg.create_context()

# Setting window attributes of app
source_dtype_dou = 'double_value'
source_dtype_int = 'int_value'

with dpg.window(tag = 'pri'):
    # Opening prompt of app
    col_num = 5 # Column number of matrix
    row_num = 5 # Row number of matrix

    dpg.add_text('Enter desired size of matrix')
    
    dpg.add_input_int(label = 'Row number', source = source_dtype_int)
    dpg.add_input_int(label = 'Column number', source = source_dtype_int)
    dpg.add_button(tag = 'rcnum', label = 'Enter')    

    dpg.add_text('Enter matrix values for solution retrieval where Ax = 0 and Ax = b')
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
                    dpg.add_input_double(label = f'r{r + 1}', source = source_dtype_dou)


# Creating window and exceution loop of app
dpg.create_viewport(title = 'Linear algebra app', width = 1000, height = 500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('pri', True)
dpg.start_dearpygui()
dpg.destroy_context()