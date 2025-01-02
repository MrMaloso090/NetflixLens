def DATA_graphs():

    import matplotlib.pyplot as plt
    import sqlite3
    import sys
    import os
    import pandas
    import geopandas

    import fiona
    import pyproj



    # SE TOMA LA CONEXION CON LA UBICACION DEL ARCHIVO.
    # THE CONNECTION WITH THE FILE LOCATION IS TAKEN.
    try:
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



    # CONECCION CON LAS BASE DE DATOS SQL : ANALYSIS -TV- -MOVIE- -GLOBAL-
    # CONNECTION WITH THE SQL DATABASES: ANALYSIS -TV- -MOVIE- -GLOBAL-
    try:
        conn_tv = sqlite3.connect(PATH + 'Analysis_tv.sqlite')
        cur_tv = conn_tv.cursor()


        conn_movie = sqlite3.connect(PATH + 'Analysis_movie.sqlite')
        cur_movie = conn_movie.cursor()


        conn_global = sqlite3.connect(PATH + 'Analysis_Global.sqlite')
        cur_global = conn_global.cursor()
    except:
        print('==============================================================\n')
        print('======================== ERROR ===============================')
        print('================== ANALYSIS NOT FOUND ========================')
        print('================= DO  ALL STEPS IN ORDER =====================\n')
        print('==============================================================\n')
        return






    # AVISO DE POSIBLE DEMORA.
    # POSSIBLE DELAY NOTICE.
    print('========================================================================\n')
    print('================== THIS PROCESS MAY TAKE A FEW SECONDS.=================\n')
    print('========================= PLEASE WAIT A MOMENT. ========================\n')
    print('================== THIS PROCESS MAY TAKE A FEW SECONDS.=================\n')
    print('========================================================================\n')



    ################################################################################################################################################## DEFINITION ALL_GRAPHS, FOR TV AND MOVIES.
    ################################################################################################################################################## DEFINITION ALL_GRAPHS, FOR TV AND MOVIES.



    ################################################################################################################################################## GENRESGRAPHS.
    ################################################################################################################################################## GENRESGRAPHS.
    # DEFICION DE LA FUNCION - GENRES_GRAPHS - QUE RELAIZARA LOS GRAFICO DE -TV- Y -MOVIE-
    # DEFINITION OF THE FUNCTION - GENRES_GRAPHS - THAT WILL CREATE THE GENRES_GRAPHS FOR -TV- AND -MOVIE-
    def All_GRAPHS(CUR_ANY , NAME_PNG):



        # CREACION DE LA CARPETA QUE CONTENDRA LOS GRAFICOS.
        # CREATION OF THE FOLDER THAT WILL CONTAIN THE GENRES_GRAPHS.
        if not os.path.exists (PATH + NAME_PNG):
            os.mkdir(PATH + NAME_PNG)

        FOLDER_PATH = (PATH + NAME_PNG + '//')



        # IMPORTACION DE DATOS DE LOS GENEROS.
        # IMPORT OF GENRE DATA.
        CUR_ANY.execute('''
            SELECT
                Top_Genres.genres,
                Top_Genres.views
            FROM
                Top_Genres
        ''')
        genre_full_data = CUR_ANY.fetchall()

        all_genres_list = list()
        all_views_list = list()
        for row in genre_full_data:
            all_genres_list.append(row[0])
            all_views_list.append(row[1])

        
        # SE OPTIENEN LOS PORSENTAGES DE TODOS LOS VALORES. 
        # THE PERCENTAGES OF ALL THE VALUES ARE OBTAINED.
        all_genres_list_perecentege = list()
        the_whole_sume = sum(all_views_list)
        for row in genre_full_data:
            percentage = (row[1] / the_whole_sume * 100)
            percentage = round(percentage, 3)
            percentage = row[0] + ' ' + str(percentage) + '%'
            all_genres_list_perecentege.append(percentage)



        # REACCINACION DE VARIABLES, POR COMODIDAD. (ESTOY APRENDIENDO A USAR LA LIBRERIA MATPLOTLIP, Y ME COMPLIQUE UN POCO)
        # VARIABLE REACTION, FOR CONVENIENCE. (I'M LEARNING TO USE THE MATPLOTLIB LIBRARY, AND I GOT A BIT CONFUSED)
        categories = all_genres_list
        values = all_views_list
        categories_percentage = all_genres_list_perecentege

    ######################################################################################### SELECTED THEME
        
        # SELECCION PERSONAL DE UN TEMA DE COLORES.
        # PERSONAL SELECTION OF A COLOR THEME.
        #print(plt.style.available)
        plt.style.use('ggplot')


    ######################################################################################### BAR GRAPH

        # BUCLE QUE ASIGNA QUE ASIGNA DE FORMA INTERMITENTE UN PAR DE COLORES, PARA HACER MAS FACIL DE DIFERENCIAR LAS COLUMNAS.
        # LOOP THAT ASSIGNS A PAIR OF COLORS INTERMITTENTLY, TO MAKE IT EASIER TO DIFFERENTIATE THE COLUMNS.
        colors_list = list()
        helper_count = 0
        count_bar_colors = len(categories)
        while True:
            helper_count += 1

            if helper_count % 2 == 0:
                colors_list.append('darkgray')
            else:
                colors_list.append('silver')
            
            if count_bar_colors < helper_count:
                break
        
        # OBTENCION DE LOS VALORES DE FORMA MAS LEGIBLE.  EJEM  =  1000000  ----->  1,000,000
        # OBTAINING THE VALUES IN A MORE LEGIBLE FORMAT. EXAMPLE = 1000000 -----> 1,000,000
        formatted_values = list()
        formatted_cat_val = list()
        for row , data in zip(values , categories):
            formatted = f'{abs(row):,}'
            formatted_values.append(formatted)

            cat_val = data + ' ' + formatted
            formatted_cat_val.append(cat_val)


        
        # CREACION DEL DIAGRAMA DE BARRAS.
        # CREATION OF THE BAR CHART.
        plt.figure(figsize=(13.33 , 7.5))
        bar = plt.bar(categories , values , color=colors_list , edgecolor = 'white')
        
        plt.xticks(ticks=categories , labels=categories , rotation=54)
        plt.yticks(ticks=values , labels=formatted_values)

        for cat , val in zip(bar,formatted_cat_val):
            cat.set_label(val)

        plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1.25))
        

        plt.savefig(FOLDER_PATH + NAME_PNG + '_genres_bar.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ######################################################################################### PIE GRAPH

        # CREACION DEL DIAGRAMA DE TORTA.
        # CREATION OF THE PIE CHART.
        plt.figure(figsize=(6.66 , 7.5))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90 , textprops={'color': 'white'})        
        plt.legend(categories_percentage , title='TOTAL PERCENTAGE \n' , loc="upper left" , bbox_to_anchor=(-0.5 , 1))
        

        plt.savefig(FOLDER_PATH + NAME_PNG + '_genres_full_pie.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ######################################################################################### SPLIT PIE GRAPH IN TWO HALF

        # SE DIVIDE EL LISTADO DE GENEROS PARA DIVIDIRLOS EN DOS SIAGRAMAS DE TORTA MAS, PARA HACER LA INFORMACION MAS LEGIBLE.
        # THE LIST OF GENDERS IS DIVIDED TO SPLIT THEM INTO TWO ADDITIONAL PIE CHARTS, TO MAKE THE INFORMATION MORE LEGIBLE.
        half_one_catogiries = list()
        half_one_values = list()
        half_two_categories = list()
        half_two_values = list()

        total_count_data = len(values)
        half_count_data = total_count_data // 2
        helper_count = 0

        for cat , val in zip(categories , values):
            helper_count += 1

            if helper_count <= half_count_data:
                half_one_catogiries.append(cat)
                half_one_values.append(val)
            else:
                half_two_categories.append(cat)
                half_two_values.append(val)

        
        legend_labels_half_one = list()
        legend_labels_half_tow = list()

        helper_count = 0

        for row in categories_percentage:
            helper_count += 1

            if helper_count <= half_count_data:
                legend_labels_half_one.append(row)
            else:
                legend_labels_half_tow.append(row)



    ######################################################################################### PIE GRAPH HALF 1

        # CREACION DEL DIAGRAMA DE TORTA. HALF ONE
        # CREATION OF THE PIE CHART. HALF ONE
        plt.figure(figsize=(6.66 , 7))
        plt.pie(half_one_values, labels=half_one_catogiries, startangle=90 , textprops={'color': 'white'})
        plt.legend(legend_labels_half_one , title='TOTAL PERCENTAGE \nHALF ONE' , loc="upper left" , bbox_to_anchor=(1 , 1))


        plt.savefig(FOLDER_PATH + NAME_PNG + '_genres_pie_h1.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()


    ######################################################################################### PIE GRAPH HALF 2

        # CREACION DEL DIAGRAMA DE TORTA. HALF TWO
        # CREATION OF THE PIE CHART. HALF TWO
        plt.figure(figsize=(6.66 , 7))
        plt.pie(half_two_values , labels=half_two_categories , startangle=90 , textprops={'color': 'white'})
        plt.legend(legend_labels_half_tow , title='TOTAL PERCENTAGE \nHALF TWO' , loc="upper left" , bbox_to_anchor=(1 , 1))
        

        plt.savefig(FOLDER_PATH + NAME_PNG + '_genres_pie_h2.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ################################################################################################################################################## GENRES GRAPHS END.
    ################################################################################################################################################## GENRES GRAPHS END.



    ################################################################################################################################################## COUNTRIES GRAPHS.
    ################################################################################################################################################## COUNTRIES GRAPHS.

        # RECUPERACION DE LOS DATOS PREVIAMENTE ANALIZADOS.
        # RECOVERY OF THE PREVIOUSLY ANALYZED DATA.
        CUR_ANY.execute('''
            SELECT 
                Top_Countries.countries,
                Top_Countries.views
            FROM
                Top_Countries
    ''')
        countries_analysis = CUR_ANY.fetchall()

        # ASIGNACION DE VARIABLES PARA CADA DATO.
        # ASSIGNMENT OF VARIABLES FOR EACH DATA POINT.
        categories_countries_list = list()
        values_views_list = list()
        
        for row in countries_analysis:
            categories_countries_list.append(row[0])
            values_views_list.append(row[1])
        

        # OBTENCION DE UNA STRING QUE AGRUPA EL PAIS CON SU VALOR DE VISUALIZACIONES DE FORMA MAS LEGIBLE.
        # OBTAINING A STRING THAT GROUPS THE COUNTRY WITH ITS VIEW COUNT IN A MORE LEGIBLE FORMAT.
        formatted_list = list()

        for cat , val in zip(categories_countries_list , values_views_list):
            formatted = f'{abs(val):,}'
            formatted = str(formatted)
            formatted_list.append(formatted)

        
        # OBTENCION DE UNA STRING QUE AGRUPA APISES CON SU RESPECTIVO PORSENTAJE.
        # OBTAINING A STRING THAT GROUPS COUNTRIES WITH THEIR RESPECTIVE PERCENTAGE.

        all_values_sum = sum(values_views_list)
        percentage_label_list = list()
        for cat , val in zip(categories_countries_list , values_views_list):
            percentage = val / all_values_sum * 100
            percentage = round(percentage , 3)
            percentage = str(cat + ' ' + str(percentage) + '%')
            percentage_label_list.append(percentage)



        #categories_countries_list
        #values_views_list
        #formatted_list
        #percentage_label_list



    ######################################################################################### SELECTED THEME
        
        # SELECCION PERSONAL DE UN TEMA DE COLORES.
        # PERSONAL SELECTION OF A COLOR THEME.
        #print(plt.style.available)
        plt.style.use('ggplot')


    ######################################################################################### BAR GRAPH

        # BUCLE QUE ASIGNA QUE ASIGNA DE FORMA INTERMITENTE UN PAR DE COLORES, PARA HACER MAS FACIL DE DIFERENCIAR LAS COLUMNAS.
        # LOOP THAT ASSIGNS A PAIR OF COLORS INTERMITTENTLY, TO MAKE IT EASIER TO DIFFERENTIATE THE COLUMNS.

        total_data_count = len(values_views_list)
        helper_count = 0

        alternated_colors = list()
        while True:
            helper_count += 1

            if helper_count % 2 == 0:
                alternated_colors.append('darkgray')
            else:
                alternated_colors.append('silver')


            if total_data_count < helper_count:
                break

        

        ######################################## FRAGMENTACIÓN DE DATOS POR AGRUPACIONES DE 10 PAÍSES CADA UNO.
        ######################################## DATA FRAGMENTATION INTO GROUPS OF 10 COUNTRIES EACH.

        categories_fragmentated = list()
        values_fragmentated = list()
        formatted_fragmentated = list()
        percentage_fragmentated = list()
        colors_fragmentated = list()
        labels_for_bar = list()
        
        helper_count = 0
        namer_counter = 0

        for categoires , values , formatted , percentage, colors in zip(categories_countries_list , values_views_list , formatted_list , percentage_label_list , alternated_colors):
            helper_count += 1


            categories_fragmentated.append(categoires)

            values_fragmentated.append(values)

            formatted_fragmentated.append(formatted)

            percentage_fragmentated.append(percentage)

            colors_fragmentated.append(colors)

            labels_for_bar.append(categoires + ' ' + formatted)


            if helper_count >= 10:
                namer_counter += 1


                categories_fragmentated = categories_fragmentated[::-1]
                values_fragmentated = values_fragmentated[::-1]
                formatted_fragmentated = formatted_fragmentated[::-1]
                colors_fragmentated = colors_fragmentated[::-1]

                percentage_fragmentated = percentage_fragmentated
                labels_for_bar = labels_for_bar



                # CREACION DE LOS DIAGRAMAS DE BARRAS DE LOS PAISES, POR GRUPOS DE 10.
                # CREATION OF THE BARS CHARTS OF THE COUNTRIES, IN GROUPS OF 10.

                plt.figure(figsize=(13.33, 7.5))
                bar_ = plt.barh(categories_fragmentated , values_fragmentated , color=colors_fragmentated , edgecolor='white')

                plt.xticks(ticks=values_fragmentated , labels=formatted_fragmentated , rotation=45)


                for bar , information in zip( bar_ , labels_for_bar):
                    bar.set_label(information + '\n')

                plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1))


                plt.savefig( FOLDER_PATH + NAME_PNG + '_countries_bars' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
                plt.close()



                # CREACION DE LOS DIAGRAMAS DE TORTA DE LOS PAISES, POR GRUPOS DE 10.
                # CREATION OF THE PIE CHARTS OF THE COUNTRIES, IN GROUPS OF 10.
                categories_fragmentated = categories_fragmentated[::-1]
                values_fragmentated = values_fragmentated[::-1]


                plt.figure(figsize=(3.33 , 3.25))
                plt.pie(values_fragmentated , labels=categories_fragmentated , startangle=90 , textprops={'color': 'white'})

                plt.legend(percentage_fragmentated , title='TOTAL PERCENTAGE \n' , loc='upper left' , bbox_to_anchor=(1.02 , 1))

                plt.savefig(FOLDER_PATH + NAME_PNG + '_countries_pies' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
                plt.close()



                categories_fragmentated = list()
                values_fragmentated = list()
                formatted_fragmentated = list()
                percentage_fragmentated = list()
                colors_fragmentated = list()
                labels_for_bar = list()
                
                helper_count = 0



        ########## CREACION DE LOS DIAGRAMAS DEL FRAGMENTO MENOR DE 10, SI LO HAY.
        ########## CREATION OF THE DIAGRAMS FOR THE FRAGMENT OF LESS THAN 10, IF ANY.
        if 0 < len(values_fragmentated):
            namer_counter += 1


            categories_fragmentated = categories_fragmentated[::-1]
            values_fragmentated = values_fragmentated[::-1]
            formatted_fragmentated = formatted_fragmentated[::-1]
            colors_fragmentated = colors_fragmentated[::-1]

            percentage_fragmentated = percentage_fragmentated
            labels_for_bar = labels_for_bar
    


            # CREACION DE LOS DIAGRAMAS DE BARRAS DE LOS PAISES, POR EL GRUPO MENOR DE 10.
            # CREATION OF THE BARS CHARTS OF THE COUNTRIES, IN GROUPS OF LEES THAN 10.

            plt.figure(figsize=(13.33, 7.5))
            bar_ = plt.barh(categories_fragmentated , values_fragmentated , color=colors_fragmentated , edgecolor='white')

            plt.xticks(ticks=values_fragmentated , labels=formatted_fragmentated , rotation=45)


            for bar , information in zip( bar_ , labels_for_bar):
                bar.set_label(information + '\n')

            plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1))


            plt.savefig( FOLDER_PATH + NAME_PNG + '_countries_bars' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
            plt.close()



            # CREACION DE LOS DIAGRAMAS DE TORTA DE LOS PAISES, POR EL GRUPO MENOR DE 10.
            # CREATION OF THE PIE CHARTS OF THE COUNTRIES, IN GROUPS OF LEES THAN 10.
            categories_fragmentated = categories_fragmentated[::-1]
            values_fragmentated = values_fragmentated[::-1]


            plt.figure(figsize=(3.33 , 3.25))
            plt.pie(values_fragmentated , labels=categories_fragmentated , startangle=90 , textprops={'color': 'white'})

            plt.legend(percentage_fragmentated , title='TOTAL PERCENTAGE \n' , loc='upper left' , bbox_to_anchor=(1.02 , 1))

            plt.savefig(FOLDER_PATH + NAME_PNG + '_countries_pies' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
            plt.close()

    ################################################################################################################################################## COUNTRIES GRAPHS END.
    ################################################################################################################################################## COUNTRIES GRAPHS END.



    ################################################################################################################################################## RUNTIME POPILARITY GRAPHS.
    ################################################################################################################################################## RUNTIME POPILARITY GRAPHS.

        # RECUPERACION DE LOS DATODS DESDE LA BASE DE DATOS DE ANALISIS.
        # RECOVERY OF DATA FROM THE ANALYSIS DATABASE.
        CUR_ANY.execute('''
            SELECT 
                Runtime_Popularity.runtime_average,
                Runtime_Popularity.views_by_average
            FROM
                Runtime_Popularity
    ''')
        popular_raw = CUR_ANY.fetchall()

        popular_raw.pop()

        durations_list = list()
        views_list = list()
        durations_labels_list = list()
        views_labels_list = list()
        for row in popular_raw:
            
            runtime_split = row[0].split(':')
            minutes = (int(runtime_split[0]) * 60) + int(runtime_split[1])

            views_label = f'{abs(row[1]):,}'

            durations_list.append(minutes)
            durations_labels_list.append(row[0])
            views_list.append(row[1])
            views_labels_list.append(views_label)
        


        # CREACION DE LOS GRAFICOS DE LINEAS.
        # LINE GRAPS CREATION.
        plt.figure(figsize=(13.33 , 7.5))


        for duration , views , duration_label , views_label in zip(durations_list , views_list , durations_labels_list , views_labels_list):
            leyend_label = duration_label + ' - ' + views_label
            plt.plot(duration , views , marker='.' , color='w' , linestyle='' , markersize=6 , label=leyend_label)

            plt.text(duration , views , views_label , fontsize=9 , ha='center' , va='bottom' , rotation=45 , color='white')

        plt.plot(durations_list , views_list , color='w' , linestyle='-' , linewidth=1)

        plt.fill_between(durations_list , views_list , color='gray' , alpha=0.5)

        plt.xlabel('Durations by Hours/Minutes')
        plt.ylabel('Views')

        plt.xticks(ticks=durations_list , labels=durations_labels_list , rotation=45)
        plt.yticks(ticks=views_list , labels='')


        plt.grid(True , axis='x')
        plt.grid(False , axis='y')

        plt.legend(loc='upper left' , bbox_to_anchor=(1.02 , 1))

        plt.savefig(FOLDER_PATH + NAME_PNG + '_popularity_lines' + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



        # CREACION DEL GRAFICO DE DISPERCION.
        # CREATION OF THE SCATTER PLOT.


        # RECUPERACION DE LOS DATODS DESDE LA BASE DE DATOS DE ANALISIS.
        # RECOVERY OF DATA FROM THE ANALYSIS DATABASE.
        CUR_ANY.execute('''
            SELECT 
                Large_Runtime_Popularity.runtime_average,
                Large_Runtime_Popularity.views_by_average
            FROM
                Large_Runtime_Popularity
    ''')
        popular_raw = CUR_ANY.fetchall()

        popular_raw.pop()

        durations_list = list()
        views_list = list()
        durations_labels_list = list()
        views_labels_list = list()
        for row in popular_raw:
            
            runtime_split = row[0].split(':')
            minutes = (int(runtime_split[0]) * 60) + int(runtime_split[1])

            views_label = f'{abs(row[1]):,}'

            durations_list.append(minutes)
            durations_labels_list.append(row[0])
            views_list.append(row[1])
            views_labels_list.append(views_label)
        

        # CREACION DEL GRAFICO DE DISPERCION.
        # CREATION OF THE SCATTER PLOT.
        plt.figure(figsize=(20 , 7.5))

        plt.scatter(durations_list , views_list , color='w' , marker='.' , s=100)

        plt.xlabel('Durations by Hours/Minutes')
        plt.ylabel('Views')

        plt.xticks(ticks=durations_list , labels=durations_labels_list , rotation=90)
        plt.yticks(ticks=views_list , labels=views_labels_list , rotation=45)

        plt.grid(True , axis='x')
        plt.grid(False , axis='y')


        plt.savefig(FOLDER_PATH + NAME_PNG + '_popularity_scatter' + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ################################################################################################################################################## RUNTIME POPILARITY GRAPHS END.
    ################################################################################################################################################## RUNTIME POPILARITY GRAPHS END.



    ##################################################################################################################################################DEFINITION ALL_GRAPHS, FOR TV AND MOVIES END.
    ##################################################################################################################################################DEFINITION ALL_GRAPHS, FOR TV AND MOVIES END.


    try:
        All_GRAPHS(cur_movie , 'Movie_Graphs')


        All_GRAPHS(cur_tv , 'Tv_Graphs')



        ################################################################################################################################################## GLOBAL GRAPHS.
        ################################################################################################################################################## GLOBAL GRAPHS.



        ################################################################################################################################################## GENRES GRAPHS.
        ################################################################################################################################################## GENRES GRAPHS.



        # CREACION DE LA CARPETA QUE CONTENDRA LOS GRAFICOS.
        # CREATION OF THE FOLDER THAT WILL CONTAIN THE GENRES_GRAPHS.
        if not os.path.exists (PATH + 'Global_Graphs'):
            os.mkdir(PATH + 'Global_Graphs')

        FOLDER_PATH = (PATH + 'Global_Graphs' + '//')



        # IMPORTACION DE DATOS DE LOS GENEROS.
        # IMPORT OF GENRE DATA.
        cur_global.execute('''
            SELECT
                Top_Genres.genres,
                Top_Genres.views
            FROM
                Top_Genres
        ''')
        genre_full_data = cur_global.fetchall()

        all_genres_list = list()
        all_views_list = list()
        for row in genre_full_data:
            all_genres_list.append(row[0])
            all_views_list.append(row[1])


        # SE OPTIENEN LOS PORSENTAGES DE TODOS LOS VALORES. 
        # THE PERCENTAGES OF ALL THE VALUES ARE OBTAINED.
        all_genres_list_perecentege = list()
        the_whole_sume = sum(all_views_list)
        for row in genre_full_data:
            percentage = (row[1] / the_whole_sume * 100)
            percentage = round(percentage, 3)
            percentage = row[0] + ' ' + str(percentage) + '%'
            all_genres_list_perecentege.append(percentage)



        # REACCINACION DE VARIABLES, POR COMODIDAD. (ESTOY APRENDIENDO A USAR LA LIBRERIA MATPLOTLIP, Y ME COMPLIQUE UN POCO)
        # VARIABLE REACTION, FOR CONVENIENCE. (I'M LEARNING TO USE THE MATPLOTLIB LIBRARY, AND I GOT A BIT CONFUSED)
        categories = all_genres_list
        values = all_views_list
        categories_percentage = all_genres_list_perecentege

        ######################################################################################### SELECTED THEME

        # SELECCION PERSONAL DE UN TEMA DE COLORES.
        # PERSONAL SELECTION OF A COLOR THEME.
        #print(plt.style.available)
        plt.style.use('ggplot')


        ######################################################################################### BAR GRAPH

        # BUCLE QUE ASIGNA QUE ASIGNA DE FORMA INTERMITENTE UN PAR DE COLORES, PARA HACER MAS FACIL DE DIFERENCIAR LAS COLUMNAS.
        # LOOP THAT ASSIGNS A PAIR OF COLORS INTERMITTENTLY, TO MAKE IT EASIER TO DIFFERENTIATE THE COLUMNS.
        colors_list = list()
        helper_count = 0
        count_bar_colors = len(categories)
        while True:
            helper_count += 1

            if helper_count % 2 == 0:
                colors_list.append('darkgray')
            else:
                colors_list.append('silver')
            
            if count_bar_colors < helper_count:
                break

        # OBTENCION DE LOS VALORES DE FORMA MAS LEGIBLE.  EJEM  =  1000000  ----->  1,000,000
        # OBTAINING THE VALUES IN A MORE LEGIBLE FORMAT. EXAMPLE = 1000000 -----> 1,000,000
        formatted_values = list()
        formatted_cat_val = list()
        for row , data in zip(values , categories):
            formatted = f'{abs(row):,}'
            formatted_values.append(formatted)

            cat_val = data + ' ' + formatted
            formatted_cat_val.append(cat_val)



        # CREACION DEL DIAGRAMA DE BARRAS.
        # CREATION OF THE BAR CHART.
        plt.figure(figsize=(13.33 , 7.5))
        bar = plt.bar(categories , values , color=colors_list , edgecolor = 'white')

        plt.xticks(ticks=categories , labels=categories , rotation=45)
        plt.yticks(ticks=values , labels=formatted_values)

        for cat , val in zip(bar,formatted_cat_val):
            cat.set_label(val)

        plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1.25))


        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_genres_bar.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()


        ######################################################################################### PIE GRAPH

        # CREACION DEL DIAGRAMA DE TORTA.
        # CREATION OF THE PIE CHART.
        plt.figure(figsize=(6.66 , 7.5))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90 , textprops={'color': 'white'})        
        plt.legend(categories_percentage , title='TOTAL PERCENTAGE \n' , loc="upper left" , bbox_to_anchor=(-0.5 , 1))
        

        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_genres_full_pie.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ######################################################################################### SPLIT PIE GRAPH IN TWO HALF

        # SE DIVIDE EL LISTADO DE GENEROS PARA DIVIDIRLOS EN DOS SIAGRAMAS DE TORTA MAS, PARA HACER LA INFORMACION MAS LEGIBLE.
        # THE LIST OF GENDERS IS DIVIDED TO SPLIT THEM INTO TWO ADDITIONAL PIE CHARTS, TO MAKE THE INFORMATION MORE LEGIBLE.
        half_one_catogiries = list()
        half_one_values = list()
        half_two_categories = list()
        half_two_values = list()

        total_count_data = len(values)
        half_count_data = total_count_data // 2
        helper_count = 0

        for cat , val in zip(categories , values):
            helper_count += 1

            if helper_count <= half_count_data:
                half_one_catogiries.append(cat)
                half_one_values.append(val)
            else:
                half_two_categories.append(cat)
                half_two_values.append(val)

        
        legend_labels_half_one = list()
        legend_labels_half_tow = list()

        helper_count = 0

        for row in categories_percentage:
            helper_count += 1

            if helper_count <= half_count_data:
                legend_labels_half_one.append(row)
            else:
                legend_labels_half_tow.append(row)



    ######################################################################################### PIE GRAPH HALF 1

        # CREACION DEL DIAGRAMA DE TORTA. HALF ONE
        # CREATION OF THE PIE CHART. HALF ONE
        plt.figure(figsize=(6.66 , 7))
        plt.pie(half_one_values, labels=half_one_catogiries, startangle=90 , textprops={'color': 'white'})
        plt.legend(legend_labels_half_one , title='TOTAL PERCENTAGE \nHALF ONE' , loc="upper left" , bbox_to_anchor=( 1 , 1))


        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_genres_pie_h1.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()


    ######################################################################################### PIE GRAPH HALF 2

        # CREACION DEL DIAGRAMA DE TORTA. HALF TWO
        # CREATION OF THE PIE CHART. HALF TWO
        plt.figure(figsize=(6.66 , 7))
        plt.pie(half_two_values , labels=half_two_categories , startangle=90 , textprops={'color': 'white'})
        plt.legend(legend_labels_half_tow , title='TOTAL PERCENTAGE \nHALF TWO' , loc="upper left" , bbox_to_anchor=(1 , 1))
        

        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_genres_pie_h2.png', bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



    ################################################################################################################################################## GENRES GRAPHS END.
    ################################################################################################################################################## GENRES GRAPHS END.



        ################################################################################################################################################## COUNTRIES GRAPHS.
        ################################################################################################################################################## COUNTRIES GRAPHS.



        # RECUPERACION DE LOS DATOS PREVIAMENTE ANALIZADOS.
        # RECOVERY OF THE PREVIOUSLY ANALYZED DATA.
        cur_global.execute('''
            SELECT 
                Top_Countries.countries,
                Top_Countries.views
            FROM
                Top_Countries
        ''')
        countries_analysis = cur_global.fetchall()

        # ASIGNACION DE VARIABLES PARA CADA DATO.
        # ASSIGNMENT OF VARIABLES FOR EACH DATA POINT.
        categories_countries_list = list()
        values_views_list = list()

        for row in countries_analysis:
            categories_countries_list.append(row[0])
            values_views_list.append(row[1])


        # OBTENCION DE UNA STRING QUE AGRUPA EL PAIS CON SU VALOR DE VISUALIZACIONES DE FORMA MAS LEGIBLE.
        # OBTAINING A STRING THAT GROUPS THE COUNTRY WITH ITS VIEW COUNT IN A MORE LEGIBLE FORMAT.
        formatted_list = list()

        for cat , val in zip(categories_countries_list , values_views_list):
            formatted = f'{abs(val):,}'
            formatted = str(formatted)
            formatted_list.append(formatted)


        # OBTENCION DE UNA STRING QUE AGRUPA APISES CON SU RESPECTIVO PORSENTAJE.
        # OBTAINING A STRING THAT GROUPS COUNTRIES WITH THEIR RESPECTIVE PERCENTAGE.

        all_values_sum = sum(values_views_list)
        percentage_label_list = list()
        for cat , val in zip(categories_countries_list , values_views_list):
            percentage = val / all_values_sum * 100
            percentage = round(percentage , 3)
            percentage = str(cat + ' ' + str(percentage) + '%')
            percentage_label_list.append(percentage)



        #categories_countries_list
        #values_views_list
        #formatted_list
        #percentage_label_list



        ######################################################################################### SELECTED THEME

        # SELECCION PERSONAL DE UN TEMA DE COLORES.
        # PERSONAL SELECTION OF A COLOR THEME.
        #print(plt.style.available)
        plt.style.use('ggplot')


        ######################################################################################### BAR GRAPH

        # BUCLE QUE ASIGNA QUE ASIGNA DE FORMA INTERMITENTE UN PAR DE COLORES, PARA HACER MAS FACIL DE DIFERENCIAR LAS COLUMNAS.
        # LOOP THAT ASSIGNS A PAIR OF COLORS INTERMITTENTLY, TO MAKE IT EASIER TO DIFFERENTIATE THE COLUMNS.

        total_data_count = len(values_views_list)
        helper_count = 0

        alternated_colors = list()
        while True:
            helper_count += 1

            if helper_count % 2 == 0:
                alternated_colors.append('darkgray')
            else:
                alternated_colors.append('silver')


            if total_data_count < helper_count:
                break



        ######################################## FRAGMENTACIÓN DE DATOS POR AGRUPACIONES DE 10 PAÍSES CADA UNO.
        ######################################## DATA FRAGMENTATION INTO GROUPS OF 10 COUNTRIES EACH.

        categories_fragmentated = list()
        values_fragmentated = list()
        formatted_fragmentated = list()
        percentage_fragmentated = list()
        colors_fragmentated = list()
        labels_for_bar = list()

        helper_count = 0
        namer_counter = 0

        for categoires , values , formatted , percentage, colors in zip(categories_countries_list , values_views_list , formatted_list , percentage_label_list , alternated_colors):
            helper_count += 1


            categories_fragmentated.append(categoires)

            values_fragmentated.append(values)

            formatted_fragmentated.append(formatted)

            percentage_fragmentated.append(percentage)

            colors_fragmentated.append(colors)

            labels_for_bar.append(categoires + ' ' + formatted)


            if helper_count >= 10:
                namer_counter += 1


                categories_fragmentated = categories_fragmentated[::-1]
                values_fragmentated = values_fragmentated[::-1]
                formatted_fragmentated = formatted_fragmentated[::-1]
                colors_fragmentated = colors_fragmentated[::-1]

                percentage_fragmentated = percentage_fragmentated
                labels_for_bar = labels_for_bar



                # CREACION DE LOS DIAGRAMAS DE BARRAS DE LOS PAISES, POR GRUPOS DE 10.
                # CREATION OF THE BARS CHARTS OF THE COUNTRIES, IN GROUPS OF 10.

                plt.figure(figsize=(13.33, 7.5))
                bar_ = plt.barh(categories_fragmentated , values_fragmentated , color=colors_fragmentated , edgecolor='white')

                plt.xticks(ticks=values_fragmentated , labels=formatted_fragmentated , rotation=45)


                for bar , information in zip( bar_ , labels_for_bar):
                    bar.set_label(information + '\n')

                plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1))


                plt.savefig( FOLDER_PATH + 'Global_Graphs' + '_countries_bars' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
                plt.close()



                # CREACION DE LOS DIAGRAMAS DE TORTA DE LOS PAISES, POR GRUPOS DE 10.
                # CREATION OF THE PIE CHARTS OF THE COUNTRIES, IN GROUPS OF 10.
                categories_fragmentated = categories_fragmentated[::-1]
                values_fragmentated = values_fragmentated[::-1]
        

                plt.figure(figsize=(3.33 , 3.25))
                plt.pie(values_fragmentated , labels=categories_fragmentated , startangle=90 , textprops={'color': 'white'})

                plt.legend(percentage_fragmentated , title='TOTAL PERCENTAGE \n' , loc='upper left' , bbox_to_anchor=(1.02 , 1))

                plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_countries_pies' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
                plt.close()



                categories_fragmentated = list()
                values_fragmentated = list()
                formatted_fragmentated = list()
                percentage_fragmentated = list()
                colors_fragmentated = list()
                labels_for_bar = list()
                
                helper_count = 0



        ########## CREACION DE LOS DIAGRAMAS DEL FRAGMENTO MENOR DE 10, SI LO HAY.
        ########## CREATION OF THE DIAGRAMS FOR THE FRAGMENT OF LESS THAN 10, IF ANY.
        if 0 < len(values_fragmentated):
            namer_counter += 1


            categories_fragmentated = categories_fragmentated[::-1]
            values_fragmentated = values_fragmentated[::-1]
            formatted_fragmentated = formatted_fragmentated[::-1]
            colors_fragmentated = colors_fragmentated[::-1]

            percentage_fragmentated = percentage_fragmentated
            labels_for_bar = labels_for_bar



            # CREACION DE LOS DIAGRAMAS DE BARRAS DE LOS PAISES, POR EL GRUPO MENOR DE 10.
            # CREATION OF THE BARS CHARTS OF THE COUNTRIES, IN GROUPS OF LEES THAN 10.

            plt.figure(figsize=(13.33, 7.5))
            bar_ = plt.barh(categories_fragmentated , values_fragmentated , color=colors_fragmentated , edgecolor='white')

            plt.xticks(ticks=values_fragmentated , labels=formatted_fragmentated , rotation=45)


            for bar , information in zip( bar_ , labels_for_bar):
                bar.set_label(information + '\n')

            plt.legend(loc='upper left' , bbox_to_anchor=(1 , 1))


            plt.savefig( FOLDER_PATH + 'Global_Graphs' + '_countries_bars' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
            plt.close()



            # CREACION DE LOS DIAGRAMAS DE TORTA DE LOS PAISES, POR EL GRUPO MENOR DE 10.
            # CREATION OF THE PIE CHARTS OF THE COUNTRIES, IN GROUPS OF LEES THAN 10.
            categories_fragmentated = categories_fragmentated[::-1]
            values_fragmentated = values_fragmentated[::-1]


            plt.figure(figsize=(3.33 , 3.25))
            plt.pie(values_fragmentated , labels=categories_fragmentated , startangle=90 , textprops={'color': 'white'})

            plt.legend(percentage_fragmentated , title='TOTAL PERCENTAGE \n' , loc='upper left' , bbox_to_anchor=(1.02 , 1))

            plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_countries_pies' + str(namer_counter) + '.png' , bbox_inches='tight' , transparent=True , dpi=300)
            plt.close()



        # CREACION DEL MAPA GEOLOGICO DE CALOR.
        # CREATION OF THE GEOLOGICAL HEAT MAP.
        views_labels = list()

        view_maximun = max(values_views_list)
        view_minimun = min(values_views_list)
        views_labels.append(view_maximun)
        views_labels.append(view_minimun)

        helper_counter = 0
        while helper_counter < 3:
            helper_counter += 1

            tempora_list = list()
            for row in range(len(views_labels) - 1):
                temporal_number = int((views_labels[row] + views_labels[row +1]) / 2)
                tempora_list.append(temporal_number)
            views_labels += tempora_list
            views_labels.sort




        countries_views = {'countries': categories_countries_list , 'views': values_views_list}
        countries_views_df = pandas.DataFrame(countries_views)


        mapamundi = '_data//Map_data//ne_110m_admin_0_countries.shp' 
        world_map = geopandas.read_file(mapamundi)


        world_map = world_map.merge(countries_views_df , left_on='ADMIN' , right_on='countries' , how='left')

        fig , ax = plt.subplots(figsize=(13.33 , 7.5))
        world_map.plot(column='views', cmap="YlOrRd" , legend=True , ax=ax , missing_kwds={"color": "lightgrey", "label": "Views by country"} , legend_kwds={'ticks': views_labels})
        
        plt.xticks([])
        plt.yticks([])



        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_countries_map'+ '.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



        # CREACION DEL MAPA GEOLOGICO DE CALOR. NUMERO 2(SIN EL PRIMERO)
        # CREATION OF THE GEOLOGICAL HEAT MAP. NUMBER 2 (WITH NO NUMBER 1)
            
        values_views_list_no_first = values_views_list[10: ]
        categories_countries_list_no_first = categories_countries_list[10: ]



        views_labels = list()
        view_maximun = max(values_views_list_no_first)
        view_minimun = min(values_views_list_no_first)
        views_labels.append(view_maximun)
        views_labels.append(view_minimun)

        helper_counter = 0
        while helper_counter < 3:
            helper_counter += 1

            tempora_list = list()
            for row in range(len(views_labels) - 1):
                temporal_number = int((views_labels[row] + views_labels[row +1]) / 2)
                tempora_list.append(temporal_number)
            views_labels += tempora_list
            views_labels.sort




        countries_views = {'countries': categories_countries_list_no_first , 'views': values_views_list_no_first}
        countries_views_df = pandas.DataFrame(countries_views)


        mapamundi = '_data//Map_data//ne_110m_admin_0_countries.shp' 
        world_map = geopandas.read_file(mapamundi)


        world_map = world_map.merge(countries_views_df , left_on='ADMIN' , right_on='countries' , how='left')

        fig , ax = plt.subplots(figsize=(13.33 , 7.5))
        world_map.plot(column='views', cmap="YlOrRd" , legend=True , ax=ax , missing_kwds={"color": "lightgrey", "label": "Views by country"} , legend_kwds={'ticks': views_labels})
        
        plt.xticks([])
        plt.yticks([])



        plt.savefig(FOLDER_PATH + 'Global_Graphs' + '_countries_map_no_top10'+ '.png' , bbox_inches='tight' , transparent=True , dpi=300)
        plt.close()



        # EL FINAL DEL PROCESO DE ANALISIS DE DATOS.
        # DATA ANALYSIS PROCES END.
        conn_global.close()
        conn_movie.close()
        conn_tv.close()


        print('============================== SUCCESSFUL ==============================\n')
        print('==================== GRAPHICATION PROCESS IS COMPLETE ==================\n')
        print('============================== SUCCESSFUL ==============================\n')
        print('========================================================================\n')
        print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
        print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
        print('https://www.themoviedb.org')
        print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.\n \n')
        print('========================================================================\n')
        print('============================== SUCCESSFUL ==============================\n')
        print('==================== GRAPHICATION PROCESS IS COMPLETE ==================\n')
        print('============================== SUCCESSFUL ==============================\n')

        
        return

    except KeyboardInterrupt :
        conn_global.close()
        conn_movie.close()
        conn_tv.close()


        print('========================================================================\n')
        print('========================================================================\n')
        print('============SOMETHING WENT WRONG WITH THE PLOTTING PROCESS.=============\n')
        print('PLEASE CONFIRM THAT YOU FOLLOWED ALL THE STEPS CORRECTLY AND TRY AGAIN.=\n')
        print('========================================================================\n')
        print('========================================================================\n')
        print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
        print('Email: daniel.sanchez.velasquez090@gmail.com' , '\n')
        print('https://www.themoviedb.org')
        print('This service uses TMDB and the TMDB APIs but is not endorsed or certified by TMDB.' , '\n')
        print('========================================================================\n')
        print('========================================================================\n')


        return