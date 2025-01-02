def DATA_analysis():

    import sqlite3
    import sys



    try:
        # SE TOMA LA CONEXION CON LA UBICACION DEL ARCHIVO.
        # THE CONNECTION WITH THE FILE LOCATION IS TAKEN.
        path_created = sqlite3.connect('Path_File.sqlite')
        cur_path = path_created.cursor()

        cur_path.execute('''
            SELECT path FROM path_data WHERE id = (?)''', (1, ))
        PATH = cur_path.fetchone()[0]
        if len(PATH) < 20:
            raise
        print(PATH)
        path_created.close()
    except:
        print('==============================================================\n')
        print('======================== ERROR ===============================')
        print('==================== PATH NOT FOUND ==========================')
        print('================= DO  ALL STEPS IN ORDER =====================\n')
        print('==============================================================\n')
        return



    try:
        # CONECCION CON LA BASE DE DATOS NORMALIZADA.
        # DATABASE NORMALIZED CONECTION.
        conn_data = sqlite3.connect(PATH + 'DataBase_normalized.sqlite')
        cur_data = conn_data.cursor()

        cur_data.execute('SELECT * FROM Information LIMIT 1')
        filter = cur_data.fetchall()
        if len(filter) == 0 :
            raise
    except:
        print('==============================================================\n')
        print('======================== ERROR ===============================')
        print('================ NORMALIZED DATA NOT FOUND ===================')
        print('================== DO ALL STEPS IN ORDER =====================\n')
        print('==============================================================\n')
        return



    ####################################################################################################################################### GLOBAL DEFINITION
    ####################################################################################################################################### GLOBAL DEFINITION

    # COMIENZO DE LA DEFINICION DE LA FUNCION 'ANALISIS'.
    # BEGINNING OF THE DEFINITION OF THE 'ANALYSIS' FUNCTION.
    def Analysis(SQLITE_NAME , FORMAT):



        # CONECCION CON EL NUEVO ARCHIVO SQLITE.
        # NEW FILE SQLITE CONECTION.
        conn = sqlite3.connect(PATH + SQLITE_NAME)
        cur = conn.cursor()



        # BORRADO DE LAS TABLAS.
        # TABLES DELET.
        cur.executescript('''
            DROP TABLE IF EXISTS Top3;
            DROP TABLE IF EXISTS Best50;
            DROP TABLE IF EXISTS Worst50;
            DROP TABLE IF EXISTS Best50_Hours;
            DROP TABLE IF EXISTS Worst50_Hours;
            DROP TABLE IF EXISTS Top_Genres;
            DROP TABLE IF EXISTS Top_Countries;
            DROP TABLE IF EXISTS Margin_Of_Error;
            DROP TABLE IF EXISTS Runtime_Popularity;
            DROP TABLE IF EXISTS Large_Runtime_Popularity;  
            DROP TABLE IF EXISTS Totals                              
        ''')



        # CREACION DE LAS TABLAS.
        # TABLES CRATION.
        cur.executescript('''
            CREATE TABLE Top3(
                views INTEGER,
                titles TEXT,
                posters TEXT
            );
            CREATE TABLE Best50(
                views INTEGER,
                titles TEXT,
                runtime TEXT,
                votes REAL,     
                hours_viewed REAL,
                countries TEXT,
                genres TEXT,
                posters TEXT
            );
            CREATE TABLE Worst50(
                views INTEGER,
                titles TEXT,
                runtime TEXT,
                votes REAL,     
                hours_viewed REAL,
                countries TEXT,
                genres TEXT,
                posters TEXT
            );
            CREATE TABLE Best50_Hours(
                views INTEGER,
                titles TEXT,
                runtime TEXT,
                votes REAL,     
                hours_viewed REAL,
                countries TEXT,
                genres TEXT,
                posters TEXT
            );
            CREATE TABLE Worst50_Hours(
                views INTEGER,
                titles TEXT,
                runtime TEXT,
                votes REAL,     
                hours_viewed REAL,
                countries TEXT,
                genres TEXT,
                posters TEXT
            );
            CREATE TABLE Top_Genres(
                genres TEXT,
                views INTEGER      
            );
            CREATE TABLE Top_Countries(
                countries TEXT,
                views INTEGER
            );
            CREATE TABLE Margin_Of_Error(
                null_genres INTEGERS,
                null_countries INTEGER,
                margin_genres INTEGER,
                margin_countries INTEGER
            );
            CREATE TABLE Runtime_Popularity(
                runtime_average TEXT, 
                views_by_average INTEGER 
            );
            CREATE TABLE Large_Runtime_Popularity(
                runtime_average TEXT, 
                views_by_average INTEGER 
            );
            CREATE TABLE Totals(
                views INTEGER,
                hours_viewed INTEGER,
                average_votes INTEGER        
            );                  
        ''')



    ####################################################################################################################################### INDENT DEFINITION FOR ALL TOPS50

        def Format(FORMAT , TYPE , TOP , TABLE):

            # FILTRO PARA USAR VIEWS COMO GUIA DE ORDEN.
            # FILTER TO USE VIEWS AS THE ORDERING GUIDE.  
            if TOP == 'views' :

                # FILTRO PARA USAR ORDEN DESCENDENTE.
                # FILTER TO USE DESCENDING ORDER.  
                if  TYPE == 'best' :

                    cur_data.execute('''
                        SELECT
                            Information.id,
                            Information.views,
                            Information.title,
                            Information.runtime,
                            Information.popularity_votes,
                            Information.hours_viewed,
                            Information.poster 
                                            
                        FROM
                            Information
                            JOIN Format ON Information.format_id = Format.id
                                    
                        WHERE
                            Format.format = ?
                                    
                        ORDER BY
                            Information.views DESC
                                    
                        LIMIT 50            
                    ''' , (FORMAT,))

                    TheFifties = cur_data.fetchall()


                # FILTRO PARA USAR ORDEN ASCENDENTE.
                # FILTER TO USE ASCENDING ORDER.
                if  TYPE == 'worst' :
                
                    cur_data.execute('''
                        SELECT
                            Information.id,
                            Information.views,
                            Information.title,
                            Information.runtime,
                            Information.popularity_votes,
                            Information.hours_viewed,
                            Information.poster 
                                            
                        FROM
                            Information
                            JOIN Format ON Information.format_id = Format.id
                                    
                        WHERE
                            Format.format = ?
                                    
                        ORDER BY
                            Information.views
                                    
                        LIMIT 50            
                    ''' , (FORMAT,))

                    TheFifties = cur_data.fetchall()


            # FILTRO PARA USAR HOURS_VIEWED COMO GUIA DE ORDEN.
            # FILTER TO USE HOURS_VIEWED AS THE ORDERING GUIDE. 
            if TOP == 'hours_viewed' :

                # FILTRO PARA USAR ORDEN DESCENDENTE.
                # FILTER TO USE DESCENDING ORDER.
                if  TYPE == 'best' :

                    cur_data.execute('''
                        SELECT
                            Information.id,
                            Information.views,
                            Information.title,
                            Information.runtime,
                            Information.popularity_votes,
                            Information.hours_viewed,
                            Information.poster 
                                            
                        FROM
                            Information
                            JOIN Format ON Information.format_id = Format.id
                                    
                        WHERE
                            Format.format = ?
                                    
                        ORDER BY
                            Information.hours_viewed DESC
                                    
                        LIMIT 50            
                    ''' , (FORMAT,))

                    TheFifties = cur_data.fetchall()


                # FILTRO PARA USAR ORDEN ASCENDENTE.
                # FILTER TO USE ASCENDING ORDER.
                if  TYPE == 'worst' :
                
                    cur_data.execute('''
                        SELECT
                            Information.id,
                            Information.views,
                            Information.title,
                            Information.runtime,
                            Information.popularity_votes,
                            Information.hours_viewed,
                            Information.poster 
                                            
                        FROM
                            Information
                            JOIN Format ON Information.format_id = Format.id
                                    
                        WHERE
                            Format.format = ?
                                    
                        ORDER BY
                            Information.hours_viewed
                                    
                        LIMIT 50            
                    ''' , (FORMAT,))

                    TheFifties = cur_data.fetchall()



            # DIFURCACION DE VALORES HALLADOS.
            # BRANCHING OF FOUND VALUES.
            for row in TheFifties:
                #print(row)

                id_ = row[0]
                views_ = row[1]
                titles_ = row[2]
                runtime_ = row[3]
                votes_ = row[4]
                hours_viewed_ = row[5]
                posters_ = row[6]


                # OBTENCION DE LOS MULTIPLES VALORES PARA GENRES, CREACION DE LISTA Y GENERADO DE TEXTO A PARTIR DE LA LISTA.
                # OBTAINING MULTIPLE VALUES FOR GENRES, CREATING A LIST, AND GENERATING TEXT FROM THE LIST.
                cur_data.execute('''
                    SELECT
                        Genres.genres
                                
                    FROM
                        Information
                        JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
                        JOIN Genres ON Genres_Encode.genres_id = Genres.id
                    
                    WHERE
                        Information.id = ?
                ''' , (id_,))

                genres_data = cur_data.fetchall()


                genres_list = list()
                for data in genres_data :
                    #print(data,)

                    genres_list.append(data[0])
                
                genres_ = ', '.join(genres_list)
                #print(genres_)


                # OBTENCION DE LOS MULTIPLES VALORES PARA COUNTRIES, CREACION DE LISTA Y GENERADO DE TEXTO A PARTIR DE LA LISTA.
                # OBTAINING MULTIPLE VALUES FOR COUNTRIES, CREATING A LIST, AND GENERATING TEXT FROM THE LIST.
                cur_data.execute('''
                    SELECT
                        Countries.countries
                                
                    FROM
                        Information
                        JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
                        JOIN Countries ON Countries_Encode.countries_id = Countries.id
                                
                    WHERE
                        Information.id = ?
                ''' , (id_,))

                countries_data = cur_data.fetchall()
                

                countries_list = list()
                for data in countries_data :
                    #print(data)

                    countries_list.append(data[0])

                countries_ = ', '.join(countries_list)
                #print(countries_)



                # FILTRO DE GUARDADO POR NOMBRE DE LA TABLA CORRESPONDIENTE.
                # FILTER SAVING BY THE NAME OF THE CORRESPONDING TABLE

                if TABLE == 'Best50':
                    cur.execute('INSERT INTO Best50 (views , titles , runtime , votes , hours_viewed , countries , genres , posters) VALUES (?,?,?,?,?,?,?,?)' ,
                        (views_ , titles_ , runtime_ , votes_ , hours_viewed_ , countries_ , genres_ , posters_) )


                if TABLE == 'Worst50':
                    cur.execute('INSERT INTO Worst50 (views , titles , runtime , votes , hours_viewed , countries , genres , posters) VALUES (?,?,?,?,?,?,?,?)' ,
                        (views_ , titles_ , runtime_ , votes_ , hours_viewed_ , countries_ , genres_ , posters_) )
                    

                if TABLE == 'Best50_Hours':
                    cur.execute('INSERT INTO Best50_Hours (views , titles , runtime , votes , hours_viewed , countries , genres , posters) VALUES (?,?,?,?,?,?,?,?)' ,
                        (views_ , titles_ , runtime_ , votes_ , hours_viewed_ , countries_ , genres_ , posters_) )


                if TABLE == 'Worst50_Hours':
                    cur.execute('INSERT INTO Worst50_Hours (views , titles , runtime , votes , hours_viewed , countries , genres , posters) VALUES (?,?,?,?,?,?,?,?)' ,
                        (views_ , titles_ , runtime_ , votes_ , hours_viewed_ , countries_ , genres_ , posters_) )
                    
                
            
            
            
            conn.commit()



    ####################################################################################################################################### INDENTED DEFINITION FOR ALL TOPS50 END

        # EJECUCION MULTIBLE DE LA DEFINICION INDENTADA, PARA 4 TABLAS DISTINTAS.
        # MULTIPLE EXECUTION OF THE INDENTED DEFINITION FOR 4 DIFFERENT TABLES.

        # Best50
        Format(FORMAT , 'best' , 'views' , 'Best50' )
        # worst50
        Format(FORMAT , 'worst' , 'views' , 'Worst50' )

        # Best50_Hours
        Format(FORMAT , 'best' , 'hours_viewed' , 'Best50_Hours' )
        # Worst50_Hours
        Format(FORMAT , 'worst' , 'hours_viewed' , 'Worst50_Hours' )






        # SELECCION Y GUARDADO DE DATOS PARA LA TABLA - TOP3 -
        # SELECTION AND STORAGE OF DATA FOR THE TABLE - TOP3 -

        cur_data.execute('''
            SELECT
                Information.views,
                Information.title,
                Information.poster
            FROM
                Information
                JOIN Format ON Information.format_id = Format.id
            WHERE
                Format.format = ?
            ORDER BY
                Information.views DESC
            LIMIT 3
        ''' , (FORMAT, ))

        Top3 = cur_data.fetchall()

        for data in Top3:
            views_ = data[0]
            titles_ = data[1]
            posters_ =  data[2]

            cur.execute('INSERT INTO Top3 (views , titles , posters) VALUES(?,?,?)' , (views_ , titles_ , posters_))

        conn.commit()





    ####################################################################################################################################### INDENTED DEFINITION FOR TOP GENRES AND MOVIES
        
        # SELECCION Y GUARDADO DE DATOS PARA LA TABLA - Top_Genres - - Top_Countries -
        # SELECTION AND STORAGE OF DATA FOR THE TABLE - Top_Genres - - Top_Countries -
        def Top_GM(FORMAT , TOP_):
            if TOP_  == 'Genres.genres':
                cur_data.execute('''
                    SELECT
                        Genres.genres
                    FROM
                        Genres
                ''')

            if TOP_ == 'Countries.countries':
                cur_data.execute('''
                    SELECT
                        Countries.countries
                    FROM
                        Countries
                ''')

            group_optain = cur_data.fetchall()
            
            list_obtain = list()
            for row, in group_optain:
                list_obtain.append(row)
            
            data_views_dict = dict()
            for row in list_obtain:

                if TOP_ == 'Genres.genres':
                    cur_data.execute('''
                    SELECT
                        Information.views
                    FROM
                        Information
                        JOIN Format ON Information.format_id = Format.id
                                    
                        JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
                        JOIN Genres ON Genres_Encode.genres_id = Genres.id
                                    
                    WHERE
                        Format.format = ?
                        AND Genres.genres = ?
                    ''' , (FORMAT , row))

                if TOP_ == 'Countries.countries':
                    cur_data.execute('''
                    SELECT
                        Information.views
                    FROM
                        Information
                        JOIN Format ON Information.format_id = Format.id
                                    
                        JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
                        JOIN Countries ON Countries_Encode.countries_id = Countries.id
                                    
                    WHERE
                        Format.format = ?
                        AND Countries.countries = ?
                    ''' , (FORMAT , row))
                
                views_optain = cur_data.fetchall()

                total_sum = 0
                for data, in views_optain:
                    total_sum += data
                
                data_views_dict[total_sum] = row
            
            order_views = dict(sorted(data_views_dict.items() , reverse=True))
            
            if TOP_ == 'Genres.genres':
                for v , k in order_views.items():
                    if v < 1: continue
                    cur.execute('''
                        INSERT INTO Top_Genres (genres , views) VALUES (? , ?)
                    ''' , (k , v))
                
            if TOP_ == 'Countries.countries':
                for v , k in order_views.items():
                    if v < 1: continue
                    cur.execute('''
                        INSERT INTO Top_Countries (countries , views) VALUES (? , ?)
                    ''' , (k , v))

            conn.commit()



    ####################################################################################################################################### INDENTED DEFINITION FOR TOP GENRES AND MOVIES END

        # EJECUCION DE LA FUNCION TOP_GM PARA ANALIZAR Y GUARDAR EL TOP DE LOS GENEROS Y LOS PAISES.
        # EXECUTION OF THE TOP_GM FUNCTION TO ANALYZE AND SAVE THE TOP GENRES AND COUNTRIES.

        # Top_Genres.
        Top_GM(FORMAT , 'Genres.genres')

        #Top_Countries.
        Top_GM(FORMAT , 'Countries.countries')






        # ANALISIS Y GUARDADO PARA LA TABLA - Margin_Of_Error -
        # ANALYSIS AND SAVE FOR TABLE - Margin_Of_Error -
        cur_data.execute('''
            SELECT
                Information.id
            From
                Information
                JOIN Format ON Information.format_id = Format.id
            WHERE
                Format.format = ?
        ''' , (FORMAT,))
        total_ids = cur_data.fetchall()

        count_ids = len(total_ids)


        cur_data.execute('''
            SELECT COUNT(Information.id)
            FROM 
                Information
                JOIN Format ON Information.format_id = Format.id
                    
                LEFT JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
            WHERE 
                Format.format = ?
                AND (Genres_Encode.genres_id IS NULL OR Genres_Encode.title_id IS NULL)
        ''', (FORMAT,))

        null_genres_ = cur_data.fetchone()[0]
        #print(null_genres_)


        cur_data.execute('''
            SELECT COUNT(Information.id)
            FROM
                Information
                JOIN Format ON Information.format_id = Format.id
                
                LEFT JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
            WHERE
                Format.format = ?
                AND (Countries_Encode.countries_id IS NULL OR Countries_Encode.title_id IS NULL)
        ''' , (FORMAT,))

        null_countries_ = cur_data.fetchone()[0]
        #print(null_countries_)


        margin_genres_ = null_genres_ * 100 / count_ids
        margin_countries_ = null_countries_ * 100 / count_ids


        cur.execute('''
            INSERT INTO Margin_Of_Error (null_genres , null_countries , margin_genres , margin_countries)  VALUES (? , ? , ? , ?)
        ''' , (null_genres_ , null_countries_ , margin_genres_ , margin_countries_))


        conn.commit()

        
    ##############################################################################################################################################################################
        def Time_Popularity(CUANTITI , TABLE):
            # ANALISIS Y GUARDADO PARA LA TABLA - Popular_Runtime -
            # ANALYSIS AND SAVE FOR TABLE - Popular_Runtime -
            cur_data.execute('''
                SELECT
                    Information.runtime,
                    Information.views
                FROM
                    Information
                    JOIN Format ON Information.format_id = Format.id
                WHERE
                    Format.format = ?
            ''' , (FORMAT,))
            runtime_vews_raw = cur_data.fetchall()

            all_runtimes_views = dict()
            runtime_list = list()
            extreme_runtime_list = list()
            runtime_sum = 0
            runtime_count = 0
            extreme_count = 0
            for row_runtime , row_views in runtime_vews_raw:
                row_runtime_split = row_runtime.split(':')
                if len(row_runtime_split) != 2: continue

                try:
                    minutes_ = (int(row_runtime_split[0])) * 60 + (int(row_runtime_split[1]))
                except:
                    continue
                # SE GUARDAN POR APARTE LOS TITULO QUE DURAN MAS DE 25 o 5 HORAS, PARA QUE NO AFECTEN EL PROMEDIO GENERAL, Y SE INCLUYEN EN UN PROMEDIO 'EXTREMO'.
                # TITLES THAT LAST MORE THAN 25 or 5 HOURS ARE KEPT SEPARATE SO THEY DON'T AFFECT THE GENERAL AVERAGE, AND THEY ARE INCLUDED IN A 'EXTREME' AVERAGE.
                if FORMAT == 'tv': maximum_filter = 1500
                if FORMAT == 'movie': maximum_filter = 300


                if minutes_ > maximum_filter:
                    extreme_runtime_list.append(minutes_)
                    extreme_count += 1

                else:
                    runtime_sum += minutes_
                    runtime_count += 1
                    runtime_list.append(minutes_)

                all_runtimes_views[minutes_] = row_views


            extreme_runtime = max(extreme_runtime_list)
            max_runtime = max(runtime_list)
            min_runtime = min(runtime_list)
            average_duration = runtime_sum / runtime_count



            # GENERACION EXPONENCIAL DE PROMEDIOS ENTRE LOS PROMEDIOS, LIMITADA A 5.
            # EXPONENTIAL GENERATION OF AVERAGES BETWEEN AVERAGES, LIMITED TO 5
            all_intervals = list()
            all_intervals.append(min_runtime)
            all_intervals.append(average_duration)
            all_intervals.append(max_runtime)

            helper_counter = 0
            while True:
                helper_counter += 1


                new_intervals = list()
                for row in range(len(all_intervals) - 1):
                    average = (all_intervals[row] + all_intervals[row + 1]) /2
                    new_intervals.append(average)
                
                all_intervals += new_intervals
                all_intervals.sort()


                if helper_counter >= CUANTITI :
                    break



            all_intervals.append(extreme_runtime)      
            all_intervals.sort()



            # ANALISIS DE LA CANTIDAD DE VISTAS, POR PROMEDIO.
            # ANALYSIS OF THE NUMBER OF VIEWS, BY AVERAGE.
            averages_total_views = dict()
            for row in all_intervals:
                averages_total_views[row] = 0


            for minu , view in all_runtimes_views.items():
                for row in range(len(all_intervals) - 1):
                    if all_intervals[row] <= minu < all_intervals[row + 1]:
                        averages_total_views[all_intervals[row]] += view
                        break

                if minu > all_intervals[-2]:
                    averages_total_views[all_intervals[-1]] += view
            
            
            # TRADUCIR LOS MINUTOS TOTALES A HORAS Y MINUTOS, PARA HACERLO MÁS FÁCIL DE LEER.
            # CONVERT THE TOTAL MINUTES TO HOURS AND MINUTES, TO MAKE IT EASIER TO READ
            readable_average_total_views = dict()
            for average_ , view_ in averages_total_views.items():
                if average_ < 60:
                    readable_key = '0:' + str(int(average_))
                else:
                    hours = int(average_) // 60
                    minutes = int(average_) % 60
                    if minutes == 0:
                        readable_key = str(hours) + ':00'
                    else:
                        readable_key = str(hours) + ':' + str(minutes)
                
                readable_average_total_views[readable_key] = view_
            

            # GUARDADO DE LOS DATOS.
            # DATA SAVING.
            if TABLE == 'Runtime_Popularity':
                for time , views in readable_average_total_views.items():
                    cur.execute('''
                        INSERT INTO Runtime_Popularity(runtime_average , views_by_average) VALUES (? , ?)
                ''' , (time , views))
                    
            elif TABLE == 'Large_Runtime_Popularity':
                for time , views in readable_average_total_views.items():
                    cur.execute('''
                        INSERT INTO Large_Runtime_Popularity(runtime_average , views_by_average) VALUES (? , ?)
                ''' , (time , views))
                
            conn.commit()



        # USO DE LA DEFINICION RUNTIME_PIPULARIRY.
        # USING THE RUNTIME_PIPULARIRY DEFINITION.
        Time_Popularity(3 , 'Runtime_Popularity')
    
        Time_Popularity(5 , 'Large_Runtime_Popularity')

        

    ##############################################################################################################################################################################
        # RECOPILACION DE VALORES TOTALES POR FORMATO.
        # TOTAL VALUES COMPILATION BY FORMAT.
        cur_data.execute('''
            SELECT
                Information.views,
                Information.hours_viewed,
                Information.popularity_votes
            FROM
                Information
                JOIN Format ON Information.format_id = Format.id
            WHERE
                Format.format = ? OR ? IS NULL
        ''' , (FORMAT, FORMAT )) 

        information_for_totals = cur_data.fetchall()

        total_views = 0
        total_hours = 0
        sum_votes = 0
        count_votes = 0
        for row in information_for_totals:
            total_views += row[0]
            total_hours += row[1]
            try:
                sum_votes += row[2]
                count_votes += 1
            except:
                continue

        average_votes = sum_votes / count_votes


        # GUARDADO DE LOS DATO
        # DATA SAVE
        cur.execute('''
            INSERT INTO Totals (views , hours_viewed , average_votes) VALUES (?,?,?)
        ''' , (total_views , total_hours , average_votes))
        conn.commit()


        conn.close()



    ####################################################################################################################################### GLOBAL DEFINITION END
    ####################################################################################################################################### GLOBAL DEFINITION END








    # EJECUCION DE Analisys PARA ANALIZAR LOS DATOS DE LAS SERIES Y LAS PELICULAS.
    # EXECUTION OF Analysis TO ANALYZE THE DATA OF THE SERIES AND MOVIES.

    Analysis('Analysis_tv.sqlite' , 'tv')

    Analysis('Analysis_movie.sqlite' , 'movie')

    #  Hace falta ponerle un try , except******* a esto. con la firma.



    # COMIENZO DE LA BASE DE DATOS GLOBAL.
    # BEGINNING OF THE GLOBAL DATA BAES.
    conn = sqlite3.connect(PATH + 'Analysis_Global.sqlite')
    cur = conn.cursor()


    # BORRADO DE LAS TABLAS.
    # TABLES DELET.
    cur.executescript('''
        DROP TABLE IF EXISTS Top_50;
        DROP TABLE IF EXISTS Top_Genres;
        DROP TABLE IF EXISTS Top_Countries;
        DROP TABLE IF EXISTS Margin_Of_Error;
    ''')

    # CREACION DE LAS TABLAS.
    # TABLES CRATION.
    cur.executescript('''
        CREATE TABLE Top_50(
            views INTEGER,
            titles TEXT,
            runtime TEXT,
            votes REAL,     
            hours_viewed REAL,
            countries TEXT,
            genres TEXT,
            format TEXT,
            posters TEXT
        );
        CREATE TABLE Top_Genres(
            genres TEXT,
            views INTEGER      
        );
        CREATE TABLE Top_Countries(
            countries TEXT,
            views INTEGER
        );
        CREATE TABLE Margin_Of_Error(
            null_genres INTEGERS,
            null_countries INTEGER,
            margin_genres INTEGER,
            margin_countries INTEGER
        );              
    ''')


    # ANALISIS Y GUARDADO DE DATOS PARA - TOP_50 -
    # ANALYSIS AND STORAGE OF DATA FOR - TOP_50 -
    cur_data.execute('''
    SELECT
        Information.id,
        Information.views,
        Information.title,
        Information.runtime,
        Information.popularity_votes,
        Information.hours_viewed,
        Format.format,
        Information.poster 
                        
    FROM
        Information
        JOIN Format ON Information.format_id = Format.id
            
    ORDER BY
        Information.views DESC
                
    LIMIT 50            
    ''')

    TheFiftie = cur_data.fetchall()



    # DIFURCACION DE VALORES HALLADOS.
    # BRANCHING OF FOUND VALUES.
    for row in TheFiftie:
        #print(row)

        id_ = row[0]
        views_ = row[1]
        titles_ = row[2]
        runtime_ = row[3]
        votes_ = row[4]
        hours_viewed_ = row[5]
        format_ = row[6]
        posters_ = row[7]



        # OBTENCION DE LOS MULTIPLES VALORES PARA GENRES, CREACION DE LISTA Y GENERADO DE TEXTO A PARTIR DE LA LISTA.
        # OBTAINING MULTIPLE VALUES FOR GENRES, CREATING A LIST, AND GENERATING TEXT FROM THE LIST.
        cur_data.execute('''
            SELECT
                Genres.genres
                        
            FROM
                Information
                JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
                JOIN Genres ON Genres_Encode.genres_id = Genres.id
            
            WHERE
                Information.id = ?
        ''' , (id_,))

        genres_data = cur_data.fetchall()


        genres_list = list()
        for data in genres_data :
            #print(data,)

            genres_list.append(data[0])
        
        genres_ = ', '.join(genres_list)



        # OBTENCION DE LOS MULTIPLES VALORES PARA COUNTRIES, CREACION DE LISTA Y GENERADO DE TEXTO A PARTIR DE LA LISTA.
        # OBTAINING MULTIPLE VALUES FOR COUNTRIES, CREATING A LIST, AND GENERATING TEXT FROM THE LIST.
        cur_data.execute('''
            SELECT
                Countries.countries
                        
            FROM
                Information
                JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
                JOIN Countries ON Countries_Encode.countries_id = Countries.id
                        
            WHERE
                Information.id = ?
        ''' , (id_,))

        countries_data = cur_data.fetchall()
        

        countries_list = list()
        for data in countries_data :
            #print(data)

            countries_list.append(data[0])

        countries_ = ', '.join(countries_list)



        # FILTRO DE GUARDADO POR NOMBRE DE LA TABLA CORRESPONDIENTE.
        # FILTER SAVING BY THE NAME OF THE CORRESPONDING TABLE
        cur.execute('INSERT INTO Top_50 (views , titles , runtime , votes , hours_viewed , countries , genres , format , posters) VALUES (?,?,?,?,?,?,?,?,?)' ,
            (views_ , titles_ , runtime_ , votes_ , hours_viewed_ , countries_ , genres_ , format_ , posters_) )

    conn.commit()



    # SELECCION Y GUARDADO DE DATOS PARA LA TABLA - Top_Genres -
    # SELECTION AND STORAGE OF DATA FOR THE TABLE - Top_Genres -
    cur_data.execute('''
        SELECT
            Genres.genres
        FROM
            Genres
    ''')
    genres_loop = cur_data.fetchall()

    gen_list = list()
    for row, in genres_loop:
        gen_list.append(row)

    genres_dict = dict()
    for row in gen_list:
        cur_data.execute('''
            SELECT
                Information.views
            FROM
                Information
                JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
                JOIN Genres ON Genres_Encode.genres_id = Genres.id
            WHERE
                Genres.genres = ?
        ''' , (row, ))
        genres_all_views = cur_data.fetchall()

        gen_sum = 0
        for data, in genres_all_views:
            gen_sum += data

        genres_dict[gen_sum] = row

    genres_dict = dict(sorted(genres_dict.items() , reverse=True))

    for view , genr in genres_dict.items():
        cur.execute('''
            INSERT INTO Top_Genres (genres , views) VALUES (?,?)
        ''' , (genr , view))

    conn.commit()



    # SELECCION Y GUARDADO DE DATOS PARA LA TABLA - Top_Countries -
    # SELECTION AND STORAGE OF DATA FOR THE TABLE - Top_Countries -
    cur_data.execute('''
        SELECT
            Countries.countries
        FROM
        Countries
    ''')
    countries_loop = cur_data.fetchall()

    countries_lis = list()
    for row, in countries_loop:
        countries_list.append(row)

    countries_dict = dict()
    for row in countries_list:
        cur_data.execute('''
            SELECT
                Information.views
            FROM
                Information
                JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
                JOIN Countries ON Countries_Encode.countries_id = countries.id
            WHERE
                Countries.countries = ?
        ''' , (row, ))
        countries_all_views = cur_data.fetchall()

        coun_sum = 0
        for data, in countries_all_views:
            coun_sum += data
        
        countries_dict[coun_sum] = row

    countries_dict = dict(sorted(countries_dict.items() , reverse=True))

    for view , coun in countries_dict.items():
        cur.execute('''
            INSERT INTO Top_Countries (countries , views) VALUES (?,?)
        ''' , (coun , view))

    conn.commit()



    # ANALISIS Y GUARDADO PARA LA TABLA - Margin_Of_Error -
    # ANALYSIS AND SAVE FOR TABLE - Margin_Of_Error -
    cur_data.execute('''
        SELECT COUNT(Information.id)
        FROM
            Information
    ''')

    titles_total_count = cur_data.fetchone()[0]


    cur_data.execute('''
        SELECT COUNT(Information.id)
        FROM
            Information
            LEFT JOIN Genres_Encode ON Information.id = Genres_Encode.title_id
        WHERE
            (Genres_Encode.genres_id IS NULL OR Genres_Encode.title_id IS NULL)
    ''')
    null_genres_count = cur_data.fetchone()[0]


    cur_data.execute('''
        SELECT COUNT(Information.id)
        FROM
            Information
            JOIN Countries_Encode ON Information.id = Countries_Encode.title_id
        WHERE
            (Countries_Encode.countries_id IS NULL OR Countries_Encode.title_id IS NULL)
    ''')
    null_countries_count = cur_data.fetchone()[0]


    genres_error_avarage = null_genres_count * 100 / titles_total_count

    countries_errors_avarage = null_countries_count * 100 / titles_total_count


    cur.execute('''
        INSERT INTO Margin_Of_Error (null_genres , null_countries , margin_genres , margin_countries)  VALUES (? , ? , ? , ?)
    ''' , (null_genres_count , null_countries_count , genres_error_avarage , countries_errors_avarage))

    conn.commit()



    # EL FINAL DEL PROCESO DE ANALISIS DE DATOS.
    # DATA ANALYSIS PROCES END.
    conn.close()
    conn_data.close()

    print('============================== SUCCESSFUL ==============================\n')
    print('======================= ANALYSIS IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('========================================================================\n')
    print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
    print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
    print('https://www.themoviedb.org')
    print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.\n \n')
    print('========================================================================\n')
    print('============================== SUCCESSFUL ==============================\n')
    print('======================= ANALYSIS IS COMPLETE ========================\n')
    print('============================== SUCCESSFUL ==============================\n')
    

    return