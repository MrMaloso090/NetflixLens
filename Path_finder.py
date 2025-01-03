def Path_finder():

    import sqlite3
    import pandas as pd
    import sys
    import os


    
    # INDICACIONES.
    # INDICATION.
    print('================================================================================')
    print('================================================================================\n')
    print('Enter the path containing the .xlsx file known as Data Dump or What We Watch')
    print('obtained from Netflix.')
    print('After that, add the full name of the file, including the .xlsx extension.\n')
    print('================================================================================')
    print('================================================================================')
    print('''The program requires this path throughout the entire process. It can be changed
            to perform an alternate process if desired, but it is essential to save the 
            correct path before starting or continuing any process.
            Keep in mind that if you enter an incorrect path, the program will notify you and 
            clear this information, so please ensure the path is entered correctly.''')
    print('================================================================================\n')


    # INGRESO DEL USUARIO DE LA RUTA Y EL NOMBRE DEL ARCHIVO.
    # USER INPUT FOR THE PATH AND FILE NAME.
    rout_folder = input('ENTER FILE PATH: ').strip()
    name_excel = input('ENTER FILE NAME: ').strip()



    # SE COLOCA EL SLASH AL FINAL DE LA RUTA.
    # ADDING A SLASH AT THE END OF THE PATH.
    if not rout_folder.endswith(os.sep):
        rout_folder += os.sep



    # CREACION DEL SQL QUE CONTENDRA LA RUTA.
    # CREATION OF THE SQL THAT WILL CONTAIN THE PATH.
    rout_created = sqlite3.connect('Path_File.sqlite')
    cur_rout = rout_created.cursor()

    cur_rout.execute(''' 
        DROP TABLE IF EXISTS path_data
    ''')

    cur_rout.execute('''
        CREATE TABLE path_data(
            id INTEGER PRIMARY KEY,
            path TEXT
        )
    ''')
        
        
        
    # CREACION DE LA CARPETA QUE CONTENDRA LOS ARCHIVOS.
    # CREATION OF THE FOLDER THAT WILL CONTAIN THE FILES.
    if not os.path.exists (rout_folder + 'system_files'):
        os.mkdir(rout_folder + 'system_files')

    FOLDER_PATH = (rout_folder + 'system_files' + '//')



    # GUARDADO DE LA RUTA.
    # PATH SAVE.
    cur_rout.execute('''
        INSERT INTO path_data(path) VALUES (?)''' , (FOLDER_PATH,))
        
    cur_rout.execute('''
        INSERT INTO path_data(path) VALUES (?)''' , (name_excel,))

    rout_created.commit()



    # CONVERSION DEL ARCHIVO EXCEL 'NETFLIXdata_dump.xlsx' EN DOS BASES DE DATOS SQLITE DISTIMTAS, SERIES Y PELICULAS. 
    # CONVERTION OF EXCEL FILE 'NETFLIXdata_dump.xlsx' IN TO TWO DIFFERENT DATA BASES SQLITE, SERIES ANS MOVIES.
    try:
        excel_file = rout_folder + name_excel

        excel_sheet_series = 0
        excel_series = pd.read_excel(excel_file , sheet_name = excel_sheet_series)
        series_created = sqlite3.connect(FOLDER_PATH + 'Data_Series.sqlite')
        excel_series.to_sql('data_series' , series_created , if_exists = 'replace' , index = False)
        series_created.commit()
        series_created.close()

        excel_sheet_movies = 1
        excel_movies = pd.read_excel(excel_file , sheet_name = excel_sheet_movies)
        movies_created = sqlite3.connect(FOLDER_PATH + 'Data_Movies.sqlite')
        excel_movies.to_sql('data_movies' , movies_created , if_exists = 'replace' , index = False)
        movies_created.commit()
        movies_created.close()
    except:
        print('============================================================ \n')
        print('=============== EXCEL DATA NOT FOUND ===============\n')
        print('============================================================ \n')
        return
    





    print('============================================================ \n')
    print('=============== EXCEL DATA CORRECT FOUND ===============\n')
    print('================== YOU CAN CONTINUE ==================\n')
    print('============================================================ \n')
    rout_created.close()
    return




Path_finder()