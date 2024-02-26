# Aidetic_Assignment

# PySpark Earthquake Analysis

This PySpark application performs analysis on earthquake data, including filtering earthquakes by magnitude, calculating averages, categorizing earthquakes, and visualizing their geographical distribution on a world map.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)
- [Folium Visualization](#folium-visualization)
- [Directory Structure](#directory-structure)
- [Submission](#submission)

## Setup

1. **Clone the Repository:**
   ```bash
   git clone <your-github-repo-url>
   cd <repository-directory>
   Install Dependencies:
   Ensure you have installed PySpark. If not, you can install it using:
   ```

bash
Copy code
pip install pyspark
Download Dataset:
Download the earthquake dataset from the provided link and save it in the dataset directory.

Usage
Run the PySpark application using:
python src/main.py

This will perform the specified PySpark operations, show results, and save the final CSV in the output directory.

Results
Average depth and magnitude of earthquakes for each earthquake type.
Categorized earthquakes into levels (Low, Moderate, High) based on their magnitudes.
Calculated the distance of each earthquake from a reference location.
Folium Visualization
To visualize the geographical distribution of earthquakes on a world map:

Open src/main.py.
Replace the earthquake_df.show() line with the provided Folium code.
Run the script again.
The map will be saved as output/earthquake_map.html. Open this file in a web browser to view the map.

Directory Structure:
project_root/
│
├── src/
│ ├── main.py
│ └── utils.py
│
├── dataset/
│ └── earthquake_data.csv
│
├── output/
│ └── earthquake_analysis_result.csv
│ └── earthquake_map.html
│
└── README.md
