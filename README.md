# Iron-Skillet Demo Portal
Demo gold template config portal

You must change the hostname and api key variable values using the admin portal web form for this to work properly.  Trying to run it without doing that will make it fail.  Instructions below.  

###### 1. Clone repo
git clone git@github.com:PaloAltoNetworks/iron-skillet-loader.git

###### 2. Change into repo directory
$ cd iron-skillet-loader

###### 3. Create python 3.6 virtualenv 
$ python3.6 -m venv env

###### 4. Active virtualenv
$ source env/bin/activate

###### 5. Download required libraries
$ pip install -r requirements.txt

###### 6. Start the portal
$ python ./iron-skillet-loader.py 

###### 7. Change the hostname and api key variables in the admin portal to match your values
* Ensure the target device is operational with network connectivity from the portal
* Open the portal (http://0.0.0.0:5001)
* Select Admin Portal --> Set API Access
* Submit IP address and credentials
* When complete, api-key.csv is created in the mssp_scripts directory
* This can be updated at any time for new Panorama IP and credentials

###### 8. Load the Day 1 template
For Panorama this configuration adds in shared data such as tags and logging profiles