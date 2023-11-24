import pandas as pd
import zipfile
import os

# Step 1: Read CSV

csv_files = [os.getenv("FILE_NAME") + str(i) + '.csv' for i in range(1, os.getenv("NUMBER"))]

for csv_file in csv_files:
    df = pd.read_csv(csv_file)

    # Step 2: Create KML Content
    kml_content = '''<?xml version="1.0" encoding="UTF-8"?>
    <kml xmlns="http://www.opengis.net/kml/2.2">
    <Document>
        <name>Emergency Locations</name>
        <Style id="icon-1">...</Style>  # Define your styles here
    '''

    for index, row in df.iterrows():
        kml_content += f'''
        <Placemark>
        <name>{row['CODIGOEMERGENCIA']}</name>
        <Point>
            <coordinates>{row['LONGITUD']},{row['LATITUD']},0</coordinates>
        </Point>
        </Placemark>
        '''

    kml_content += '</Document></kml>'

    # Step 3: Save as KML
    kml_file = csv_file.split(".")[0] + '.kml'
    with open(kml_file, 'w') as file:
        file.write(kml_content)

    # Step 4: Convert KML to KMZ
    kmz_file = csv_file.split(".")[0] + '.kmz'
    with zipfile.ZipFile(kmz_file, 'w') as zipf:
        zipf.write(kml_file, os.path.basename(kml_file))

    # Clean up (optional)
    os.remove(kml_file)