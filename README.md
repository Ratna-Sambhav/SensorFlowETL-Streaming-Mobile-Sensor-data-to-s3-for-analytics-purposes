# Streaming-Mobile-Sensor-data-to-s3-for-analytics-purposes
Using docker to deploy a function on severless lambda, that collects streaming sensor data from smartphone applications, processes the data and stores the data in s3 buckets. Data is stored with partitions based on time of event and the user.
Purpose: The purpose of this project is to collect data for training a machine learning model that can perform activity recognition taking data from user's smartphone and give personalized recommendations.
