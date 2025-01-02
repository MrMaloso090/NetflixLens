def API_download():
    global count_data_save
    global data_download_by_execution
    global data_download_count
    global count_10
    global count_100

    import urllib.request,urllib.parse,urllib.error
    import sqlite3
    import ssl
    import sys
    import time
    import json 
    import os


    # SE TOMA LA CONEXION CON LA UBICACION DEL ARCHIVO.
    # THE CONNECTION WITH THE FILE LOCATION IS TAKEN.
    try:
        conn_path = sqlite3.connect('Path_File.sqlite')
        cur_path = conn_path.cursor()

        cur_path.execute('SELECT path FROM path_data WHERE id = (?)' , (1, ))
        PATH = cur_path.fetchone()[0]
        if len(PATH) < 20:
            raise
        conn_path.close()
        print(PATH)
    except:
        print('============================================================\n')
        print('======================== ERROR ===============================')
        print('==================== PATH NOT FOUND ==========================')
        print('=================== DO STEP ONE FIRST =====================\n')
        print('============================================================\n')
        return



    # CREACION DEL ARCHIVO SQL DE DATOS RAW
    # DATA RAW SQL FILE CREATION
    conn_raw = sqlite3.connect(PATH + 'DataBase_RAW.sqlite')
    cur = conn_raw.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Data_Raw(
            title TEXT,
            format TEXT,
            runtime text,
            hours_viewed INTEGER,
            views INTEGER,
            json TEXT,
            movies_countries TEXT                   
        )
    ''')


    # SSL
    # SSL
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE



    # VARIABLE DE LA API
    # API VARIABLE
    api_tv = 'https://api.themoviedb.org/3/search/tv?api_key=07ad044a4cd934279c3b6591a2750ab2'
    api_movie = 'https://api.themoviedb.org/3/search/movie?api_key=07ad044a4cd934279c3b6591a2750ab2'



    # CUENTA PARA GUARDAR LOS DATOS DESCARGADOS CADA 250 DATOS.
    # COUNT TO SAVE DOWNLOADED DATA EVRY 250 DATAS.
    count_data_save = 0



    # MARCADORES DE NUMERO DE DESCARGAS
    # DOWNLOAD NUMBER MARKERS
    count_10 = 0
    count_100 = 0



    # CANTIDAD DE DATOS DESIGNADA POR EL USUARIO PARA SU DESCARGADOS DURANTE ESTA EJECUCION.
    # USER DESIGNATED AMOUNT OF DATA DOWNLOADED DURING THIS RUN.
    data_download_count = 0

    print('============================================================\n')
    print('DOWNLOAD NOTICE:\n')
    print('The complete download process may take several hours. You have the option to download as many')
    print('titles as you wish and proceed with the analysis using the available data. However, please note that')
    print('incomplete data may lead to unreliable results.')
    print('If preferred, you can also download the data in smaller batches. For the most accurate analysis, it is')
    print('recommended to download all titles.\n')
    print('Please enter the number of titles to download or type  " ALL " to download everything.\n')
    print('============================================================\n')
    print(PATH)
    data_download_by_execution = input('INPUT REQUIRED: ')
    print('============================================================\n')
    if data_download_by_execution.lower().strip() == 'all' :
        data_download_by_execution = 100000000
    try:
        data_download_by_execution = int(data_download_by_execution)
        print('============================== SUCCESSFUL ==============================\n')
        print('Your input has been accepted. The download process will begin shortly.\n')
        print('============================== SUCCESSFUL ==============================\n')
        time.sleep(1)
    except:
        print('============================== ERROR ==============================\n')
        print('Invalid input. Please enter a valid number or type all to proceed.\n')
        print('============================== ERROR ==============================\n')
        return



    ####################################################################################################################################################################################

    # SE DEFINE LA FUNCION BUCLE.
    # THE LOOP FUNCTION IS BE DEFINED.

    def LOOP(SQLITE,TABLE,API,FORMAT,FILTERS):

        global count_data_save
        global data_download_by_execution
        global data_download_count
        global count_10
        global count_100
        


        # ABRIR LA CONCECCION CON DATA_SERIES.SQLITE.
        # OPEN THE CONECTION WHIT DATA_SERIES.SQLITE.
        conn_data = sqlite3.connect(PATH + SQLITE)
        cur_data = conn_data.cursor()
        cur_data.execute('SELECT * FROM ' + TABLE)



        # IGNORAREMOS LAS PRIMERA 5 LINEAS. 
        # IGNOR THE 5 FIRSTS LINES.
        jumps = 0 


        # BUQLE DE DESCARGA DE DATOS.
        # DATA DOWNLOAD LOOP.
        for line in cur_data.fetchall():



            # CANTIDAD DE DATOS DESIGNADA POR EL USUARIO PARA SU DESCARGADOS DURANTE ESTA EJECUCION.
            # USER DESIGNATED AMOUNT OF DATA DOWNLOADED DURING THIS RUN.
            if data_download_count >= data_download_by_execution:
                conn_raw.commit()
                conn_data.close()
                conn_raw.close()

                print('========================================================================\n')
                print('Downloaded Data:' , data_download_count , '\n')
                print('CONTINUE DOWNLOADING UNTIL THE PROGRAM INDICATES THAT IT HAS COMPLETED FULLY.\n')
                print('========================================================================\n')
                print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
                print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
                print('https://www.themoviedb.org')
                print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.' , '\n')
                print('========================================================================\n')
                return



            #IGNORAREMOS LAS PRIMERA 5 LINEAS. 
            # IGNOR THE 5 FIRSTS LINES.
            if jumps < 5:
                jumps = jumps + 1
                continue



            # ASIGNAR VARIABLES A LOS VALORES QUE NOS INTEREZA RECUPERAR DE DATA_SERIES.
            # ASSIGN VARIABLES TO THE VALUES WE ARE INTERESTED IN RECOVERING FROM DATA_SERIES.
            filter_ = (line[1])
            title_ = str(line[1]).strip()
            hours_viewed_ = str(line[4]).strip()
            runtime_ = str(line[5]).strip()
            views_ = str(line[6]).strip()
            format_ = str(FORMAT)



            # FILTRO INTENLIGENTE QUE SALTA LOS DATOS YA ALMACENADOS.
            # SMART FILTER THAT SKIPS DATA ALREADY STORED.
            try:
                cur.execute('SELECT title FROM Data_Raw WHERE title = ?' , (filter_, ))
                filter = cur.fetchone()[0]
                print(' === Data Alredy Saved === ')
                continue
            except:
                pass



            # SE CORTA EL TITULO A SOLO EL NOMBRE ESPESIFICO
            # THE TITLE IS CUT TO ONLY THE SPECIFIC NAME.
            colon = title_.find(':')
            if colon != -1 :
                title_temp = title_[:colon].strip()
            else :
                title_temp = title_
            
            slash = title_temp.find('/')
            if slash != -1 :
                title_temp = title_temp[:slash ].strip()
            year = title_temp.find('(')
            if year != -1 :
                title_temp = title_temp[:year].strip()



            # MEDIO SEGUNDO DE ESPERA PARA SOLO DESCARGAR 2 DATOS POR SEGUNDO Y ASI NO INFRINGIR LAS CONDICIONES CON LA API (SON MAXIMO 4 PETICIONES POR SEGUNDO, PERO MEJOR MANTENER UN MARGEN APMLIO).
            # HALF A SECOND WAIT TO ONLY DOWNLOAD 2 DATA PER SECOND AND THUS NOT VIOLATE THE CONDITIONS WITH THE API (THERE ARE A MAXIMUM OF 4 REQUESTS PER SECOND, BUT IT IS BETTER TO MAINTAIN A PERMILLION MARGIN).
            
            # PORFAVOR NO RETIRAR NI CAMBIAR ESTE TIEMPO. PODRIAMOS TODOS PERDER EL ACCESO A LA API !!!!!!!!!!
            # PLEASE DO NOT THROW AWAY OR CHANGE THIS TIME. WE ALL COULD LOSE API ACCESS !!!!!!!!!!
            
            # SI DESEA CONECTARSE CON LA API, LO PUEDE HACER DE FORMA GRATUITA EN: https://www.themoviedb.org
            # IF YOU WANT TO CONNECT WITH THE API, YOU CAN DO SO FOR FREE AT: https://www.themoviedb.org
            time.sleep(0.25) # NO CAMBIAR, PORFAVOR !! # DO NOT CHENGE IT, PLEASE !!



            # SE ESCOGEN SOLO LOS DATOSTITULOS QUE ENCONTRO LA API.
            # ONLY THE TITLES FOUND BY THE API IS SELECTED.
            if FILTERS == 'yes' :



                # COMIENZAN LAS PETICIONES A LA API.
                # API REQUESTS BEGIN.
                name = dict()
                name['query'] = title_temp

                try:
                    response_url = API + '&' + urllib.parse.urlencode(name)
                    response_encode = urllib.request.urlopen(response_url , context=ctx)
                    response = response_encode.read().decode()
                except:
                    print('x')
                    continue

                try:
                    js = json.loads(response)
                except:
                    print('x')
                    continue



                # SE SELECCIONAN LOS DATOS REQUERIDOS.
                # DATA REQUIRET SELECTION.
                try:
                    js_results = js['results'][0]
                except:
                    print('x')
                    continue
                

                # FILTRO DE DATOS VACIOS.
                # FILTER OF EMPTY DATA.
                if len(js_results) == 0 :
                    print('x')
                    continue


                try:
                    # RECUPERACION POR SEPARADO DE LOS PAISES DE LAS PELICULAS, YA QUE LA API LOS RESPONDE REALIZANDO UNA BUSQUEDA DISTINTA.
                    # SEPARATE RETRIEVAL OF COUNTRIES FOR MOVIES, AS THE API RESPONDS WITH A DIFFERENT SEARCH METHOD.
                    if format_ == 'movie':
                        id_ = js_results['id']

                        id_ = str(id_)

                        API_countris = 'https://api.themoviedb.org/3/movie/'
                        API_key = '?api_key=07ad044a4cd934279c3b6591a2750ab2'

                        url_request_countries = API_countris + id_ + API_key
                        answer_countrise = urllib.request.urlopen(url_request_countries , context=ctx)
                        read_countries = answer_countrise.read().decode()

                        js_countries = json.loads(read_countries)

                        js_countries_list = js_countries['origin_country']

                        countries_list = list()
                        for data in js_countries_list :
                            countries_list.append(data)

                        countries_ = ', '.join(countries_list)
                except:
                    countries_ = None



                # SE ENCAPSULA EL JSON SELECCIONADO Y CODIFICADO DENTRO DE UNA VARIABLE.
                # THE SELECTED AND ENCODED JSON IS ENCLOSED WITHIN A VARIABLE.
                json_ = json.dumps(js_results)
                json_ = json_.encode()



            # SE ASIGNA N/A A LOS TITULOS NO ENCONTRADOS POR LA API.
            # N/A IS ASSIGNED TO THE TITLES NOT FOUND BY THE API.
            else:
                json_ = None


            # SE INSERTAN LOS VALORES DENTRO DEL ARCHIVO DATABASE_RAW.SQLITE.
            # VALUES ARE INSERTED INTO THE DATABASE_RAW.SQLITE FILE.

            if format_ != 'movie' :
                cur.execute('''
                    INSERT OR IGNORE INTO Data_Raw (title , format , runtime , hours_viewed , views , json) VALUES (? , ? , ? , ? , ? , ? )''',
                    (title_ , format_  , runtime_ , hours_viewed_ , views_ , json_))
                
                
            if FILTERS == 'no' :
                countries_ = None

            if format_ == 'movie' :
                cur.execute('''
                    INSERT OR IGNORE INTO Data_Raw (title , format , runtime , hours_viewed , views , json , movies_countries) VALUES (? , ? , ? , ? , ? , ? , ? )''',
                    (title_ , format_  , runtime_ , hours_viewed_ , views_ , json_ , countries_))
            


            # CANTIDAD DE DATOS DESIGNADA POR EL USUARIO PARA SU DESCARGADOS DURANTE ESTA EJECUCION.
            # USER DESIGNATED AMOUNT OF DATA DOWNLOADED DURING THIS RUN.
            data_download_count =  data_download_count + 1



            # MARCADORES DE NUMERO DE DESCARGAS
            # DOWNLOAD NUMBER MARKERS
            print('.')

            count_10 = count_10 + 1
            count_100 = count_100 + 1
            if count_10 >= 10 :
                print('O')
                count_10 = 0
            if count_100 >= 100 :
                print('Downloaded Data:' , data_download_count)
                count_100 = 0



            # CUENTA PARA GUARDAR LOS DATOS DESCARGADOS CADA 250 DATOS.
            # COUNT TO SAVE DOWNLOADED DATA EVRY 250 DATAS.
            count_data_save = count_data_save + 1
            if not count_data_save < 250 :
                conn_raw .commit()
                print('[SAVE]')
                count_data_save = 0
        


        # GURDADO TRAS FINALIZAR EL BUCLE, Y CIERRE LA BASE DE DATOS.
        # SAVED AFTER ENDING THE LOOP, AND CLOSING DATABASE.
        conn_raw.commit()
        conn_data.close()

    ####################################################################################################################################################################################


    try:
        # SE EJECUTA TANTO EL BUCLE DE SERIES COMO EL DE PELIULAS 2 VECES, PARA DARLE OTRA OPORTUNIDAD A LOS ARCHIVOS DE DESCARGARSE CORRECTAMENTE.
        # BOTH THE SERIES LOOP AND THE MOVIES LOOP ARE EXECUTED TWICE TO GIVE THE FILES ANOTHER OPPORTUNITY TO DOWNLOAD CORRECTLY.
        re_try = 0
        while re_try < 2 :
            LOOP( 'Data_Series.sqlite' , 'data_series' , api_tv , 'tv' , 'yes' )

            LOOP( 'Data_Movies.sqlite' , 'data_movies' , api_movie , 'movie' , 'yes' )

            re_try += 1



        # SE EJECUTAN AMBOS BUCLES PARA INCLUIR LA INFORMACION INCOMPLETA, PUES AUN NOS INTEREZA.
        # BOTH LOOPS ARE EXECUTED TO INCLUDE THE INCOMPLETE INFORMATION, AS IT IS STILL OF INTEREST TO US.
        LOOP('Data_Series.sqlite' , 'data_series' , api_tv , 'tv' , 'no')

        LOOP('Data_Movies.sqlite' , 'data_movies' , api_movie , 'movie' , 'no')
    except KeyboardInterrupt:
        conn_raw.commit()
        conn_raw.close()
        try:
            conn_data.close()
            print('')
        except:
            pass

        print('========================================================================\n')
        print('Downloaded Data:' , data_download_count , '\n')
        print('CONTINUE DOWNLOADING UNTIL THE PROGRAM INDICATES THAT IT HAS COMPLETED FULLY.\n')
        print('========================================================================\n')
        print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
        print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
        print('https://www.themoviedb.org')
        print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.' , '\n')
        print('========================================================================\n')
        return



    # CIERRE TRAS FINALIZAR CORRECTAMENTE.
        conn_raw.commit()
        conn_raw.close()

    print('============================== SUCCESSFUL ==============================\n')
    print('====================== THE DOWNLOAD IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('========================================================================\n')
    print('THE PROGRAM HAS SUCCESSFULLY COMPLETED THE FULL DOWNLOAD OF ALL THE RAW FILES.\n')
    print('FEEL FREE TO CONTINUE WITH THE PROCESS.\n')
    print('========================================================================\n \n')
    print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
    print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
    print('https://www.themoviedb.org')
    print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.\n \n')
    print('========================================================================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('====================== THE DOWNLOAD IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')
    return