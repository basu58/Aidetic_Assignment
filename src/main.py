import folium
from folium.plugins import MarkerCluster
from utils import create_spark_session, load_dataset, convert_to_timestamp, filter_magnitude, calculate_avg_depth_magnitude, add_magnitude_category, calculate_distance_from_reference

def main():
    # Initialize Spark session
    spark = create_spark_session()

    # Load dataset
    file_path = "/home/basu/app/assignments/database.csv"
    earthquake_df = load_dataset(spark, file_path)

    # Transformations
    earthquake_df = convert_to_timestamp(earthquake_df)
    earthquake_df = filter_magnitude(earthquake_df, 5.0)
    avg_depth_magnitude_df = calculate_avg_depth_magnitude(earthquake_df)
    earthquake_df = add_magnitude_category(earthquake_df)
    earthquake_df = calculate_distance_from_reference(earthquake_df)

    # Output results
    avg_depth_magnitude_df.show()
    earthquake_df.show()

    # Save final CSV
    final_csv_path = "/home/basu/app/assignments/output/earthquake_analysis_result.csv"
    earthquake_df.coalesce(1).write.mode('overwrite').option("header", "true").csv(final_csv_path)

    # Visualize geographical distribution using Folium
    visualize_earthquakes(earthquake_df)

def visualize_earthquakes(df):
    # Create a Folium Map centered at (0, 0)
    m = folium.Map(location=[0, 0], zoom_start=2)

    # Create a MarkerCluster for better visualization of multiple points
    marker_cluster = MarkerCluster().add_to(m)

    # Add markers for each earthquake
    for index, row in df.toPandas().iterrows():
        folium.Marker([row['Latitude'], row['Longitude']],
                      popup=f"Type: {row['Type']}, Magnitude: {row['Magnitude']}",
                      icon=None).add_to(marker_cluster)

    # Save the map as an HTML file
    map_path = "/home/basu/app/assignments/output/earthquake_map.html"
    m.save(map_path)
    print(f"Map saved to {map_path}")

if __name__ == "__main__":
    main()
