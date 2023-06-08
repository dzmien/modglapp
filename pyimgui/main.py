import dearpygui.dearpygui as dpg


dpg.create_context()
dpg.create_viewport(title='(floatwong)', width=600, height=300)


with dpg.window(tag="Primary Window", label="Example Window"):
    t0 = dpg.add_text("Hello, world")
    b0 = dpg.add_button(label="Save")
    it0 = dpg.add_input_text(label="string", default_value="Quick brown fox")
    sf0 = dpg.add_slider_float(label="float", default_value=0.273, max_value=1)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
