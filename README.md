# Aidetic_Assignment

# PySpark Earthquake Analysis

This PySpark application performs analysis on earthquake data, including filtering earthquakes by magnitude, calculating averages, categorizing earthquakes, and visualizing their geographical distribution on a world map.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)
- [Folium Visualization](#folium-visualization)

## Setup

**Clone the Repository:**

```bash
git clone https://github.com/basu58/Aidetic_Assignment.git
cd Aidetic_Assignment
Install Dependencies:
Ensure you have installed Python, Pandas, Fulium and PySpark. If not, you can install it using:
```

bash
Copy code
pip install pyspark
pip install pandas
pip install fulium

Download Dataset:
Download the earthquake dataset from the provided link and save it in the dataset directory.

## Usage

Run the PySpark application using:
python src/main.py

This will perform the specified PySpark operations, show results, and save the final CSV in the output directory.

## Results

Average depth and magnitude of earthquakes for each earthquake type.
Categorized earthquakes into levels (Low, Moderate, High) based on their magnitudes.
Calculated the distance of each earthquake from a reference location.

## Folium Visualization

To visualize the geographical distribution of earthquakes on a world map, the map will be saved as output/earthquake_map.html. Open this file in a web browser to view the map.
