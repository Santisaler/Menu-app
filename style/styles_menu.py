
# Recordar que el gradiente en este caso tiene dirección vertical

style_menu = '''
    QMainWindow {
        background-color: #5D99F0;
        background: qlineargradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:0 #5D99F0,
        stop:1 grey
        );
    }

    QLineEdit{
        background-color: white;
        color: black;
        font-size: 20px;
    }
    

    #minutas_container, #ensaladas_container, #postres_container, #gaseosas_container, #promo_container, 
    #licuados_container, #cafe_container, #pastas_container,#sand_fria_container,#sand_caliente_container{
        border: 4px solid grey;
        border-radius: 15px;
        background-color: black;
        color: black;
    }

    QTabWidget{
        background-color: #FFF2E5;
    }

   
   QLabel[class="container_titles"] {
        font-weight: bold;
        font-size: 20px;
        background-color: #5D99F0;
    }


    QLabel[class="main_title"]{
        font-size: 30px;
        text-align: center;
        color: white;
        font-weight: bold;
    }

    QPushButton{
        border: 2px solid black;
        border-radius: 10px;
        padding: 5px;
        font-size: 20px;
        background-color: grey;    
    }

    QPushButton:hover{
        background-color: #ABCEFF;
        font-weight: bold;
    }

'''