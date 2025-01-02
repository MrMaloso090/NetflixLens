def DATA_normalization():

    import urllib.request,urllib.parse,urllib.error
    import ssl
    import json
    import sqlite3
    import sys



    
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


    # CREACION DEL SQL QUE CONTENDRA LA BASE DE DATOS NORMALIZADA.
    # CREATION OF THE SQL THAT WILL CONTAIN THE NORMALIZED DATABASE.
    conn_normalized = sqlite3.connect(PATH + 'DataBase_normalized.sqlite')
    cur = conn_normalized.cursor()



    # CREACION DE LAS TABLAS
    # TABLES CREATION
    cur.executescript('''      
        CREATE TABLE IF NOT EXISTS Information(
            id INTEGER NOT NULL PRIMARY KEY,
            title TEXT UNIQUE,
            format_id INTEGER,
            runtime TEXT,
            hours_viewed INTEGER,
            views INTEGER,
            popularity_votes REAL,
            poster TEXT
        );
        CREATE TABLE IF NOT EXISTS Format(
                id INTEGER NOT NULL PRIMARY KEY,
                format TEXT UNIQUE
        );
        CREATE TABLE IF NOT EXISTS Genres(
            id INTEGER NOT NULL PRIMARY KEY,
            genres TEXT UNIQUE
        );
        CREATE TABLE IF NOT EXISTS Genres_Encode(
            title_id INTEGER,
            genres_id INTEGER, 
            PRIMARY KEY (tiTle_id , genres_id)          
        );
        CREATE TABLE IF NOT EXISTS Countries(
            id INTEGER NOT NULL PRIMARY KEY,
            countries TEXT UNIQUE                                  
        );
        CREATE TABLE IF NOT EXISTS Countries_Encode(
            title_id INTEGER,
            countries_id INTEGER ,
            PRIMARY KEY (title_id , countries_id)                                 
        ); 
    ''')



    # PROTECCION SSL.
    # SSL PROTECTION.
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE



    # GENERAR UN DICCIONARIO ACTUALIZADO DE LOS GENEROS Y PELICULAS DE SERIES Y PELICULAS.
    # GENERATE AN UPDATE DICTIONARY OF GENRES AND COUNTRIES FOR SERIES AND MOVIES.
    try:
        all_genres=dict()

        api_genres_series = 'https://api.themoviedb.org/3/genre/tv/list?api_key=07ad044a4cd934279c3b6591a2750ab2'
        open_genres_series = urllib.request.urlopen (api_genres_series , context=ctx)
        read_genres_series = open_genres_series.read().decode()
        js_genres_series = json.loads(read_genres_series)
        for line in js_genres_series['genres']:
            if line['id'] in all_genres:
                continue
            all_genres[line['id']] = line['name']
            
        api_genres_movies = 'https://api.themoviedb.org/3/genre/movie/list?api_key=07ad044a4cd934279c3b6591a2750ab2'
        open_genres_movies = urllib.request.urlopen(api_genres_movies , context=ctx)
        read_genres_movies = open_genres_movies.read().decode()
        js_genres_movies = json.loads(read_genres_movies)
        for line in js_genres_movies['genres']:
            if line['id'] in all_genres:
                continue
            all_genres[line['id']] = line['name']
    except:
        print('=============================================================\n')
        print('============== GENRES API CONECTION FAILED ==================\n')
        print('=============================================================\n')

    try:
        all_countries = dict()

        api_countries = 'https://api.themoviedb.org/3/configuration/countries?api_key=07ad044a4cd934279c3b6591a2750ab2'
        open_countries = urllib.request.urlopen(api_countries , context=ctx)
        read_countries = open_countries.read().decode()
        js_countries = json.loads(read_countries)

        for line in js_countries:

            all_countries[line['iso_3166_1']] = line['english_name']
        
    except:
        print('=============================================================\n')
        print('============== COUNTRIES API CONECTION FAILED ==================\n')
        print('=============================================================\n')



    try:
        # CONEXION CON LA BASE DE DATOS RAW
        # DATABASE RAW CONNECTION
        conn_raw = sqlite3.connect(PATH + 'DataBase_RAW.sqlite')
        cur_raw = conn_raw.cursor()

        cur_raw.execute('SELECT * FROM Data_Raw')
        RAW = cur_raw.fetchall()
        if len(RAW) == 0:
            raise
    except:
        print('==============================================================\n')
        print('======================== ERROR ===============================')
        print('==================== RAW NOT FOUND ===========================')
        print('================== DO ALL STEPS IN ORDER =====================\n')
        print('==============================================================\n')
        return


    # VARIABLES QUE SERAN DE AYUDA: GUARDADO - CONTEOS.
    # HELPFUL VARIABLES: SAVED - COUNTS.
    data_saver = 0
    all_titles_count = 0
    count_10 = 0
    count_100 = 0



    ####################################################################################################################################################################################
    ####################################################################################################################################################################################
    try:
        
        # COMIENZO DEL BUQLE.
        # LOOP BEGINNING
        for line in RAW :
            


            # ASIGNAR VARIABLES A LOS VALORES QUE NOS INTEREZA RECUPERAR DE DATA_SERIES.
            # ASSIGN VARIABLES TO THE VALUES WE ARE INTERESTED IN RECOVERING FROM DATA_SERIES. 
            title_ = (line[0])
            format_ = (line[1])
            runtime_ = (line[2])
            hours_viewed_ = (line[3])
            views_ = (line[4])

            json_ = (line[5])

            movie_countries_ = (line[6])



            # FILTRO INTENLIGENTE QUE SALTA LOS DATOS YA ALMACENADOS.
            # SMART FILTER THAT SKIPS DATA ALREADY STORED.
            try:
                cur.execute('SELECT title FROM Information WHERE title = ?' , (title_, ))
                filter = cur.fetchone()[0]
                print(' === Data Alredy Saved === \n')
                continue
            except:
                pass



    ####################################################################################################################################################################################

            # SE SELECCIONAN LOS DATOS QUE DESEADOS DEL JSON.
            # THE DESIRED DATA FROM THE JSON IS SELECTED.
            if json_ == 'N/A' :
                json_ = None

            if json_ != None:
                js_ = json_.decode('utf-8')
                js = json.loads(js_)
                


            # BUCLES Y TOMA DE DATOS.
            # LOOPS AND DATA SELECT.
            genres_ = list()
            try:
                for gen in js['genre_ids'] :
                    data = all_genres[gen]
                    genres_.append(data)
                    if len(genres_) == 0:
                        genres_ = None
            except:
                genres_ = None
                print('-')
            

            countries_ = list()
            try:
                if format_ == 'tv':
                    for cou in js['origin_country']:
                        data = all_countries[cou]
                        countries_.append(data)
                    if len(countries_) == 0:
                        countries_ = None
            except:
                countries_ = None
                print('-')
            
            try:
                if format_ == 'movie' :
                    countries_list_ = (movie_countries_).split(', ')
                    print(countries_)
                    for cou in countries_list_ :
                        print(cou)
                        data = all_countries[cou]
                        countries_.append(data)
                    if len(countries_) == 0:
                        countries_ = None
            except:
                countries_ = None
                print('-')

            try:
                poster_ = js['poster_path']
                if len(poster_) == 0:
                    poster_ = None
            except:
                poster_ = None
                print('-')
            

            try:
                popularity_votes_ = js['vote_average']
                if popularity_votes_ == 0:
                    popularity_votes_ = None
            except:
                popularity_votes_ = None
                print('-')

    ####################################################################################################################################################################################
        


            # COMIENZO DEL PROCESO DE NORMALIZACION DE DATOS.
            # SATARTING DATA NORMALIZING PROCES.



            # title_

            # runtime_
            # hours_viewed_
            # views_
            # popularity_votes_
            # poster_

            # format_
            # genres_
            # countries_

            

            # NORMALIZACION MANY TO ONE DEL DATO, FORMATO.
            # DATA NORMALIZATION MANY TO ONE FOR, FOR FORMAT.
            cur.execute('INSERT OR IGNORE INTO Format (format) VALUES (?)' , (format_, ))

            cur.execute('SELECT id FROM Format WHERE format = ?' , (format_, ))
            format_id_ = cur.fetchone()[0]



                # INGRESO DE LOS DATOS QUE NO REQUIEREN SER NORMALIZADO, MAS EL ID DEL FORMATO. 
                # ENTER NOT REQUIRED NORMALIZATION DATA, PLUS FORMAT ID.
            cur.execute('INSERT OR IGNORE INTO Information (title, format_id , runtime , hours_viewed , views , popularity_votes , poster) VALUES (? , ? , ? , ? , ? , ? , ?)' , 
                (title_, format_id_ , runtime_ , hours_viewed_, views_ , popularity_votes_ , poster_))



            # SE TOMA EL ID DEL TITULO
            # GET TITLE ID
            cur.execute('SELECT id FROM Information WHERE title = ?' , (title_, ))
            title_id_ = cur.fetchone()[0]



            # NORMALIZACION MANY TO MANY DE LOS GENEROS.
            # MANY TO MANY NORMALIZATION FOR GENRES.
            if genres_ == None:
                cur.execute('INSERT OR REPLACE INTO Genres_Encode (title_id) VALUES (?)' , (title_id_,))

            if genres_ != None:

                for data in genres_ :
                    cur.execute('INSERT OR IGNORE INTO Genres (genres) VALUES (?)' , (data,))

                    cur.execute('SELECT id FROM Genres WHERE genres = ?' , (data,))
                    genres_id_ = cur.fetchone()[0]

                    cur.execute('INSERT OR REPLACE INTO Genres_Encode (title_id , genres_id) VALUES (? , ?)' ,
                        (title_id_ , genres_id_))



            
            # NURMALIZACION MANNY TO MANY DE LOS PAISES.
            # MANY TO MANY NORMALIZATION FOR COUNTRYS.
            if countries_ == None:
                cur.execute('INSERT OR REPLACE INTO Countries_Encode (title_id) VALUES (?)' , (title_id_,))
            
            if countries_ != None:

                for data in countries_ :
                    cur.execute('INSERT OR IGNORE INTO Countries (countries) VALUES (?)' , (data, ))

                    cur.execute('SELECT id FROM Countries WHERE countries = ?' , (data, ))
                    countries_id_ = cur.fetchone()[0]

                    cur.execute('INSERT OR REPLACE INTO Countries_Encode (title_id , countries_id) VALUES (? , ?)' , 
                        (title_id_ , countries_id_))

            


            # CONTADOR DE GUARDADO DE DATOS.
            # COUNT DATA SAVER.
            data_saver += 1
            if data_saver == 500:
                conn_normalized.commit()
                print('[SAVED]')
                data_saver = 0
            


            # CONTADOR DE TITULOS.
            # TITLES COUNTER.
            all_titles_count += 1
            if not count_10 == 10 or count_100 == 100:
                print('.')



            # CONTADOR DE MARCAS REFERENCIALES.
            # REFERENTIAL MARKS COUNTER.
            count_10 += 1
            if count_10 == 10 :
                if not count_100 == 100 :
                    print('o')
                count_10 = 0
            
            count_100 += 1
            if count_100 == 100 :
                print('TITLES DOWLOADED:' , all_titles_count)
                count_100 = 0



    except KeyboardInterrupt :
            conn_normalized.commit()
            conn_normalized.close()
            conn_raw.close()

            print('========================================================================\n')
            print('TITLES DOWLOADED:' , all_titles_count)
            print('CONTINUE DOWNLOADING UNTIL THE PROGRAM INDICATES IT IS COMPLETE.\n')
            print('========================================================================\n')
            print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
            print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
            print('https://www.themoviedb.org')
            print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.' , '\n')
            print('========================================================================\n')
            return

    ####################################################################################################################################################################################
    ####################################################################################################################################################################################



    # EL FINAL DEL PROCESO DE NORMALIZACION DE DATOS.
    # DATA NORMALIZATION PROCES END.
    conn_normalized.commit()
    conn_normalized.close()
    conn_raw.close()

    print('TITLES DOWLOADED:' , all_titles_count)
    print('============================== SUCCESSFUL ==============================\n')
    print('======================= NORMALIZING IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('========================================================================\n')
    print('THE PROGRAM HAS SUCCESSFULLY COMPLETED THE FULL NORMALIZATION PROCESS\n')
    print('FEEL FREE TO CONTINUE TO THE NEXT STEP.\n')
    print('========================================================================\n \n')
    print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
    print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
    print('https://www.themoviedb.org')
    print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.\n \n')
    print('========================================================================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('======================= NORMALIZING IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')

    
    return