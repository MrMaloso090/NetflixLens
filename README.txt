NetflixLens marked the beginning of my journey as a data analyst. It challenged me to apply and expand my skills in data processing, API integration, and automated reporting.


## Main Code
The main entry point for the project is [NetflixLens.py], which provides the user interface and handles the main logic.

## Example Presentation.
You can view an example of the final output in the presentation located in the folder [__EXAMPLES](https://github.com/MrMaloso090/NetflixLens/blob/main/__EXAMPLES).

[Example_Presentation_2024-1.pptx](https://github.com/MrMaloso090/NetflixLens/blob/main/__EXAMPLES/Example_Presentation_2024-1.pptx)
This presentation showcases the analysis conducted for the first semester of 2024, presenting the processed data in a clear and structured manner.



# NetflixLens

NetflixLens is a Python-based project designed to analyze and visualize data about Netflix's catalog. It processes Netflix's publicly shared data dumps and enriches the dataset by integrating additional metadata retrieved from an external API. The result is a comprehensive analysis presented through an automatically generated presentation.

## Key Features

- Processes Netflix's catalog data dump.
- Integrates metadata such as genres, countries of origin, and poster images via API.
- Analyzes and normalizes the data for accurate insights.
- Generates various visualizations, including bar charts, pie charts, line graphs, scatter plots, and a global heat map.
- Produces a detailed presentation summarizing findings.

## Data Accuracy

The data analysis ensures a high level of accuracy, with a margin of error of less than 2%. This margin exists because some titles lack metadata (e.g., genres or countries of origin) in the API. Exact margins of error are included in the presentation for transparency.

## Requirements

- Python 3.x  
- Dependencies listed in the `requirements.txt` file  

If you are using the provided executable version, there are no prerequisites. The program runs automatically without requiring any additional setup.

## Installation Instructions

If you'd like to run the code and explore the implementation:

1. Clone the repository:
   ```bash
   git clone https://github.com/MrMaloso090/NetflixLens
   cd NetflixLens
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main program:
   ```bash
   python NetflixLens.py
   ```

## Project Structure

- `NetflixLens.py`: The main script to run the program.
- `Path_finder.py`: Handles file path setups.
- `API_download.py`: Fetches additional metadata via API.
- `DATA_normalization.py`: Cleans and normalizes the data.
- `DATA_analysis.py`: Performs data analysis.
- `DATA_graphs.py`: Creates visualizations.
- `Data_presentation.py`: Generates the final presentation.
- `_data/Map_data/`: Contains essential data for the global heat map.
- `_data/Presentation/`: Includes images and logos used in the presentation.

### Dependencies

- urllib.request
- urllib.parse
- urllib.error
- sqlite3
- ssl
- sys
- time
- json
- os
- matplotlib.pyplot
- pandas
- geopandas
- fiona
- pyproj
- Pillow
- requests
- python-pptx

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the code, provided proper credit is given to the author. For more details, refer to the `LICENSE` file.





Code Author: Daniel Sanchez Velasquez - TakuSan.
Email: daniel.sanchez.velasquez090@gmail.com
