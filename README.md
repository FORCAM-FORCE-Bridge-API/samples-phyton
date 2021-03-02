# samples-python

Provides sample applications for using the FORCAM FORCE Bridge API with python.
If you have any questions look at https://forcebridge.io/en/qa-portal/

### Useful Links

* Website: https://www.forcebridge.io/ | https://www.forcam.com/
* Documentation: https://forcebridge.io/en/developers/
* API Definition: https://app.swaggerhub.com/apis-docs/FORCAM/FORCEBridgeAPI/
### Usage / Requirements

###### Access to a FORCAM FORCE Bridge API System

_If you need access to a demo system please contact forcebridge@forcam.com._

Please add your URL, user and password of your Bridge API instance to the variables below (contained by all samples).

```Python

String user; // YOUR USER (e.g. GitHub)
String password; // YOUR PASSWORD (e.g. GitHub)
String urlToken = ""; // YOUR URL (e.g. https://forcebridgehackathon.force.eco:24443/ffwebservices/)
```

###### Framework & Tool

* PyCharm: Python IDE runtime (https://www.jetbrains.com/de-de/pycharm/download/)

### Description of the sample applications:

# Authentication

A small PyCharm Python console application wich authenticates to a FORCAM FORCE Bridge API and prints out the token information.

![Image](Assets/AuthenticationGif.gif)

File: "authentication.py".

# Get all available workplaces

A small PyCharm Python console application wich authenticates to a FORCAM FORCE Bridge API, determine all available workplaces and prints them out.

![Image](Assets/GetAvailableWorkplacesGif.gif)

File: "getavailableworkplaces.py".

# Get current operating state of a workplace

A small PyCharm Python console application wich authenticates to a FORCAM FORCE Bridge API, determine the operating state of an workplace and print it.

![Image](Assets/GetOperatingStateOfWorkplaceGif.gif)

File: "getoperatingstateofworkplace.py".

# Get all operating states

A small PyCharm Python console application wich authenticates to a FORCAM FORCE Bridge API, determine all operating states and prints them out.

![Image](Assets/GetOperatingStatesGif.gif)

Folder: "getoperatingstates.py".
