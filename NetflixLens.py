def NetflixLens():
    import sys



    from Path_finder import Path_finder
    from API_download import API_download
    from DATA_normalization import DATA_normalization
    from DATA_analysis import DATA_analysis
    from DATA_graphs import DATA_graphs
    from Data_presentation import Data_presentation



    print('================================================================================')
    print('================================================================================')
    input('==================   PRESS ENTER TO CONTINUE TO THE MENU   =====================')



    print('================================================================================')
    print('================================================================================')
    print('Code Author: Daniel Sanchez Velasquez - TakuSan.')
    print('Email: daniel.sanchez.velasquez090@gmail.com \n')
    print('================================================================================')
    print('=============================                   ================================')
    print('============================     NetflixLend     ===============================')
    print('=============================                   ================================')
    print('================================================================================')
    print('''NetflixLens takes advantage of the information provided by Netflix through its 
        DataDump, which is shared semi-annually, revealing the popularity of its titles. 
        Based on this dataset, additional key information is gathered using the TMDb API, 
        allowing for a detailed analysis of the retrieved data. Upon completing this 
        two-step process, the user will be able to access a clear and visually friendly 
        presentation of the analysis for the selected year's and semester's DataDump, 
        greatly facilitating the interpretation of popularity trends and patterns.''')
    print('================================================================================')
    print('================================================================================\n')
    print('SELECT ONE OPTION:')
    print('leave blank to exit.\n')
    print('1 == Enter the path where you have the DataDump and its name.')
    print('2 == Download complementary information from TMDb.')
    print('3 == Normalize, analyze, and create the presentation.')
    print('4 == Instructions and Comments.\n')
    answer = input('ENTER THE NUMBER CORRESPONDING TO YOUR CHOICE: ')


    answer = answer.strip()


    if answer == '' :
        print('================================================================================')
        print('================================================================================\n')
        print('The program has closed successfully.\n')
        print('================================================================================')
        print('================================================================================')
        sys.exit()



    elif answer == '1' :
        Path_finder()

        NetflixLens()



    elif answer == '2' :
        API_download()

        NetflixLens()



    elif answer == '3' :
        print('================================================================================')
        print('================================================================================')
        print('''\n
Please note that the process will indicate multiple times that some of the necessary tasks have 
already been completed, but it will not be fully finished until explicitly stated.
This process may take anywhere from a few seconds to a minute.''')
        print('================================================================================')
        input('========================   PRESS ENTER TO CONTINUE   ===========================')
        DATA_normalization()
        DATA_analysis()
        DATA_graphs()
        Data_presentation()

        NetflixLens()



    elif answer == '4' :
        print('================================================================================')
        print('=============================       COMENTS       ==============================')
        print('================================================================================')
        
        
        print('''First, a quick note about the **DataDump** or "What We Watched" dataset:
        Finding the DataDump can be a bit tricky, but if you search for these names on Google,
        you should be able to locate it. Also, I'll provide you with two links below to make things easier:
        - [What We Watched - First Half of 2024](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2024)
        - [What We Watched - Second Half of 2023](https://about.netflix.com/en/news/what-we-watched-the-second-half-of-2023)
        
        Please note that you can only use the DataDump starting from the second semester of 2023. 
        Before that, Netflix used a different format and provided less information. So, make sure to download the appropriate data from those dates or later.''')

        
        print('''Next, we use the **TMDb API**, which is a movie database that provides detailed information about films and TV shows.
        You can check out their website for more details or to create an account to access their API:
        - [TMDb API Website](https://www.themoviedb.org/)
        ''')

        print('================================================================================')
        print('=============================       INSTRUCTIONS       ===========================')
        print('================================================================================')
        print('''Welcome to NetflixLens!

    NetflixLens is a program designed to help you analyze the Netflix DataDump, which is a collection of data Netflix shares semi-annually. This dataset reveals insights into the popularity 
    of its titles, helping to identify viewing trends, most popular genres, and other valuable patterns. NetflixLens not only takes advantage of the DataDump but also enriches the 
    data by pulling additional information from the **TMDb API**. The **TMDb API** is a movie database that provides data about films and TV shows, such as genres, ratings, and 
    release dates. 

    With NetflixLens, you will be able to process and analyze Netflix*s DataDump, visualize trends, and generate a user-friendly presentation that summarizes the analysis.

    Here*s what each option in the program does:

    1. **Enter the path where you have the DataDump and its name**: 
    This is the first step. In this option, you need to input the file path where you have stored the Netflix DataDump. This file contains the data you*ll be analyzing. Without this file, 
    the program cannot proceed with the analysis.

    2. **Download complementary information from the TMDb API**: 
    In this step, the program will gather additional data from the **TMDb API** to enhance the analysis. This data includes information like movie genres, ratings, and other important 
    details. This step is crucial because it adds depth to the basic data from Netflix*s DataDump, allowing for a more comprehensive analysis.

    3. **Normalize, analyze, and create the presentation of the data**: 
    Once the DataDump is ready and the TMDb data is collected, this step processes the data. It normalizes the values, conducts statistical analysis, and generates graphs. Afterward, it 
    produces a presentation that clearly shows trends and patterns, making it easier to interpret the findings. 

    4. **Instructions and Comments (this option)**: 
    This option provides detailed instructions on how to use the program, explaining the steps, what they do, and why each is necessary.

    ### Why is this process necessary in this order?
    - **Step 1** is crucial because the DataDump file is the core source of information. Without specifying its location and name, the program cannot continue.
    - **Step 2** enhances the basic data from the DataDump by adding complementary information, which is necessary for a complete analysis.
    - **Step 3** is the actual data processing, analysis, and presentation generation. Since Step 1 and Step 2 are prerequisites, this step cannot be executed properly unless those are completed first.

    Once all steps are followed in order, you will be able to easily interpret Netflix’s title popularity trends and patterns for the selected semester, helping to draw meaningful 
    conclusions about viewing habits and other insights.

    Thank you for using NetflixLens!''')
        print('================================================================================')

        NetflixLens()

    

############################################################################################################################ FUN.
############################################################################################################################ FUN.
    elif answer == 'RanaCalva':
        print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⡶⣶⣤⡀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⠶⢾⣟⣻⣟⣻⡛⠾⢿⠛⠛⠛⠒⠂⠉⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡏⠦⢘⢿⣿⣿⣿⣿⡿⠄⣈⢲⠀⠀⠀⢀⠀⠀⢿⣆⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢯⡆⠤⠀⠀⠉⠡⠆⠀⡢⢋⠜⠀⠀⠁⠀⢀⠂⠈⣿⡄⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡧⡇⠀⠀⣀⠤⠔⢂⠡⠄⠈⠀⠀⠐⠀⠌⡲⢄⠠⣘⣷⡄⠀⠈⠂⠀⠀⠀⠀⠀⣀⣠⣀⠀⠀⢡⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠀⠂⠀⠀⣿⡗⡇⡂⠭⠐⠂⠉⠀⢶⡄⣈⣴⣾⣶⡶⠞⠃⠈⠉⣽⣿⣿⣄⣀⣠⣤⣴⣶⣾⣿⢟⡟⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠈⠀⠀⠀⣀⣀⣤⣤⣿⣿⣽⣤⣤⣤⡦⠶⠛⠈⢉⠝⣿⣿⢿⣿⣿⠆⣠⣌⠹⣿⣿⣿⣿⣛⣛⣯⣭⣥⠈⠙⢾⣿⠃⠀⢠⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⣀⣴⠾⣛⢫⠭⣉⠳⡐⢆⡚⡍⠭⢭⢛⣛⠶⠾⣿⣮⣿⣯⣾⣿⣿⣾⡿⠿⠟⠛⠛⠉⣉⣉⣤⡴⠞⣋⣤⣾⠟⠁⠀⢀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⣴⢟⡵⣉⠖⣡⠞⡰⢣⡙⠦⡱⢌⡙⢆⠣⢆⡹⢔⡢⣝⢻⡿⢿⠿⡿⠿⡷⢿⠾⣟⢻⠻⣍⣳⣼⣾⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠸⣿⣸⡴⢡⢚⠤⣋⡔⢣⣜⣡⣳⣮⣽⣾⣿⣾⣶⣿⣶⣷⣿⡿⠾⠾⣷⣿⣬⣷⣿⣶⣿⣿⣿⣿⠟⠉⠙⣿⢦⡀⠀⠠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠻⠷⣷⣾⣷⣶⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣀⣤⡤⣤⣄⡉⢿⣿⠿⠿⠛⠛⠛⠛⠛⠓⠒⠾⣶⡇⠀⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢀⡀⠀⠀⠀⠀⠀⣀⣤⣶⣾⢿⣿⣿⡿⠛⣉⣭⡟⢠⣾⣁⡤⢴⣶⣶⡝⢦⠹⠀⠀⠀⠀⠶⠶⠀⠀⠀⠀⠈⠛⢷⣄⠀⠀⠡⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⢀⣤⡶⠟⢋⡭⠞⣡⠞⣡⠏⢠⡾⠉⣼⡃⣿⣿⣿⣧⣴⣿⣿⣷⢸⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀⠀⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣡⠀⠀⠉⠀⠞⠁⠐⠃⠀⣾⢀⣆⢿⣇⣟⠻⣿⣿⣿⣿⡿⢃⠎⠰⠃⠀⠀⠀⠀⠀⢀⣠⣤⣶⣴⡶⠶⣼⡟⠀⠀⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⠛⠁⠸⠏⢠⠇⠀⠀⠀⠀⠀⠀⢠⡇⢸⡿⠘⣿⢮⣳⢬⣭⣭⠭⠗⠉⠀⠀⠀⠀⣀⣤⡶⠾⠛⠉⠁⠀⠀⠀⢠⡿⠁⠀⠠⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠀⠀⠀⣀⣴⠞⠋⠀⠀⠀⣴⠟⢠⠏⠀⠀⠀⠀⠀⠀⠀⡾⢠⠏⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⢀⣠⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⠀⠠⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠊⠀⠀⣠⡾⠋⢠⣴⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢠⠄⠀⠀⠀⠀⢀⣀⣤⠴⠞⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⡾⠋⠀⠀⡐⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠀⠀⣠⡾⠋⡀⠀⠉⣵⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠘⠦⠤⠴⠶⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣖⡿⣿⠟⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⣴⢟⡀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣀⠀⠻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠶⠛⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠣⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣏⢞⣶⣦⣀⠙⠛⠶⠶⠂⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣞⣫⣿⠿⢁⠈⠈⠙⠛⠛⠲⠶⠶⠶⠶⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⠿⠛⠉⢁⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢞⡿⢃⢸⡗⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⣿⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠞⠋⠁⠀⣀⡴⠞⠋⠁⠀⠀⠀⠀⠀⣀⡀⣀⣤⢴⢶⣚⣿⠿⠖⠀⠀⠀⠀⠀⢚⣵⣿⢧⠛⠹⣧⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠄⠀⠁⠀⠀⢀⣾⣿⣉⣉⡙⠻⢦⣄⠀⠀⠀⠀⠀⢰⡟⠁⠀⠀⠘⠶⣭⡀⠀⠀⠀⢀⣠⣴⣶⡿⠿⡝⠳⠾⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⢠⡿⢹⣿⡛⠀⠀⢻⡆⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡐⠀⠀⣠⡴⠶⠛⠛⠁⠀⠀⠉⠻⣦⡀⠻⣷⡀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⢿⣤⣴⡿⣟⡿⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠘⣿⡇⠀⠀⢹⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣏⣤⣤⣤⣀⡀⠀⠀⠀⠀⠈⠁⠀⢿⣿⡀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠈⣿⣧⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣟⣀⣀⣤⣿⡇⠀⠀⢠⣿⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀
⠠⠀⠀⣠⡶⠟⠛⠛⠛⠛⠛⠛⠓⠂⠀⠀⠀⠀⠀⣿⣯⠇⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⢠⣿⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡝⢀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣯⣟⣿⣿⣿⣛⣉⠉⠁⢠⣤⣿⣀⠀⠀⠀⠂⠄⢀⡀⠀⠀
⢀⠀⠀⢻⣎⠳⢶⣤⣄⣀⣀⣀⣀⣀⣤⣴⣾⣿⣿⡟⠀⠈⣧⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⣀⣠⣤⣶⣿⣿⣿⣿⣿⠟⣿⠟⠛⠛⢛⣉⣉⣠⠀⠀⠉⠙⠛⠷⣦⣄⣀⠀⠀⠈⠀⡀
⠀⠀⠀⠀⠙⢷⣄⡈⠻⣟⠛⠿⢿⣿⣿⣿⣿⣿⡿⠷⣄⣠⣸⣦⣤⣄⠀⠀⠈⢿⣆⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠉⠁⠀⠈⠻⣶⠾⠟⠛⢿⣿⡟⢀⣄⠀⢳⣶⣤⣄⣉⠉⠻⣦⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠙⠻⣦⣝⣶⣦⣤⣌⣙⡛⠿⣿⣿⣶⣤⣤⣾⠿⠟⠻⠛⠛⠛⠞⠿⣦⡀⠀⠀⠀⠀⠈⠉⡙⠛⠛⠛⠛⠻⠟⠻⠟⠶⢾⣦⣤⣤⡀⠀⠀⠀⣿⣉⣠⡿⠻⣷⡈⢿⡍⠙⠛⠻⠟⠋⠀⠀⠄
⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣽⠟⠛⠛⠻⢷⣄⣤⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣦⣄⣀⠀⠀⠻⢦⡘⢿⣟⣻⡿⠿⠿⠟⠿⢶⣤⡾⠃⠀⠀⠀⠈⠉⠉⠀⠀⠘⠛⠛⠁⠀⠀⠀⠀⠀⠄⠊⠀
⠀⠀⠀⠀⠀⠀⠈⠀⠀⠈⠉⠁⠀⠀⢀⠀⠀⠉⠉⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⣶⣄⠙⢷⣄⠉⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠀⠀⠐⠂⠤⠄⠠⠤⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠒⠂⠁⠀⠁⠐⠒⠂⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠠⠀⡀⠀⠈⠛⠿⠛⠙⠛⠋⠁⠀⡸⠈⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠂⠄⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')
        NetflixLens()
############################################################################################################################ FUN.
############################################################################################################################ FUN.



    else:
        print('================================================================================')
        print('================================== ERROR =======================================\n')
        print('========================    ENTER A VALID VALUE    =============================\n')
        print('================================== ERROR =======================================')
        print('================================================================================')
        
        NetflixLens()



##################################################################################################################################### PROGRAM EXECUTION.


NetflixLens()

##################################################################################################################################### PROGRAM EXECUTION END.