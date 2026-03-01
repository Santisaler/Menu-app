

def set_classes(ui):
    widget = ui.container_title
    
    widget.setProperty("class", "main_title")
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    widget.update()