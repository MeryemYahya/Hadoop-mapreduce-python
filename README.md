# NYC Taxi Trip Analysis

## Overview
The  project focuses on analyzing NYC yellow and green taxi trip records using Hadoop and MapReduce. The dataset includes various fields such as pick-up/drop-off dates, locations, trip distances, fares, payment types, and driver-reported passenger counts. The data is sourced from the NYC Taxi and Limousine Commission (TLC), collected by authorized technology providers under the Taxicab & Livery Passenger Enhancement Programs (TPEP/LPEP). 

## Data Source
The trip data can be downloaded from the NYC TLC [Trip Record Data page](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page).

## Project Requirements
1. Download all the data of yellow and green taxi trip records since 2019.
2. Store the CSV data in HDFS using Hadoop.
3. Implement MapReduce Python scripts to perform the following analyses:
   - Find the preferred payment type of yellow taxis.
   - Find the preferred payment type of green taxis.
   - Calculate the average trip distance per year.
   - Determine the average trip duration by destination.
   - Calculate the average tip amount of New Yorkers.

## Technologies Used
- **Hadoop**: For storing and processing large datasets in HDFS.
- **MapReduce**: For distributed data processing.
- **Python**: For writing MapReduce scripts.
- **PowerPoint**: For presentation of findings and installation steps.

## MapReduce Scripts
### 1. Preferred Payment Type of Yellow/Green Taxis
- **Script**: `scripts/Preferred_payment_type_mapper.py` `scripts/Preferred_payment_type_reducer.py`
- **Description**: Analyzes the payment types in yellow taxi trips.

### 2. Average Trip Distance Per Year
- **Script**: `scripts/Average_trip_distance_per_year_mapper.py` `scripts/Average_trip_distance_per_year_reducer.py`
- **Description**: Calculates the average trip distance by year.

### 3. Average Trip Duration by Destination
- **Script**: `scripts/Average_trip_duration_by_destination_mapper.py` `scripts/Average_trip_duration_by_destination_reducer.py`
- **Description**: Calculates average trip duration based on destinations.

### 4. Average Tip Amount of New Yorkers
- **Script**: `scripts/Average_tip_amount_mapper.py` `scripts/Average_tip_amount_reducer.py`
- **Description**: Computes the average tip amount based on trip records.

## PowerPoint Presentation
A PowerPoint presentation `project_hadoop.pptx` has been prepared to explain:
- The steps for installing Hadoop.
- Manipulating HDFS.
- Creating and executing MapReduce Python scripts.

## Conclusion
This project demonstrates how to leverage Hadoop and MapReduce to analyze large datasets effectively. The findings from the analysis provide insights into taxi trip patterns and preferences in New York City.
