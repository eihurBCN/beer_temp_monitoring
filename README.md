# beer_temp_monitoring
Project to monitor the temperature and log it into a db accesible via local area network

## Hardware
The hardware used for this project is:

-Raspberry PI B+

-Temperature sensor Ds1820

-4.7K resistor

## Scripts
There are 3 scripts need for the proper behaviour of the project:

### createtable.py
This script creates a sqlite db table with the columns for temperature and timestamp. It must be run once before starting the other scripts to create the database.

### log_temperature.py
This script reads the temperature from the sensor in the raspberry pi and store it in db along with the timestamp of the measurement.

### html_temp.py
This script read the last available data in the db, and generate a html file with the data. It is generate in local apache.

### execute.sh
This script is a loop that every 60s executes log_temperature.py and html_temp.py
## Configuration
First we must install apache in the raspberry pi as we use it to show the data in local host.

Then we modify the rc.local and add the next line before exit 0:

sudo bash /home/pi/beer_temp_monitoring/execute.sh &
