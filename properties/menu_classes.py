

def set_classes(ui):

    secondary_titles=[
        ui.postres_title,
        ui.promo_title,
        ui.licuados_title,
        ui.gaseosas_title,
        ui.cafeteria_title,
        ui.minutas_title,
        ui.ensaladas_title,
        ui.fria_title,
        ui.caliente_title,
        ui.pastas_title,
    ]

    for label in secondary_titles:  # label is an iterable --> different widgets (labels) 
        label.setProperty("class","container_titles")  
        label.style().unpolish(label)
        label.style().polish(label) #undo and do again the appearence
        label.update()

    #main_title = "bar_name"
    ui.bar_name.setProperty("class","main_title")  
    ui.bar_name.style().unpolish(label)
    ui.bar_name.style().polish(label) #undo and do again the appearence
    ui.bar_name.update()


    #ui.postres_title.setProperty("class", "container_titles")
    #ui.promo_title.setProperty("class", "container_titles")
    #ui.licuados_title.setProperty("class", "container_titles")    
