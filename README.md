Data.gov.ie CKAN extensions
===========================

Repository listing of CKAN Extensions developed for the Data.gov.ie Open Data platform

**CKAN-feedback**

This extension provides a simple feedback form for submitting data requests through the CKAN System.
The administrator receives an email for processing the request. The administrator email can be set in the CKAN config file development.ini/production.ini. The config variable is 'ckan.feedback.request_email'. The system email which would send this request information could be defined in the same config file using the config variable 'ckan.feedback.sender_email'. If these values are not defined, the extension uses the default values defined in controller.py.

**CKAN-irish_theme**

This extension renders a custom mobile-friendly template designed for Data.gov.ie.

This is my first attempt to write CKAN extensions and code in Python. These extensions could be refactored in a better way.
They can be installed by running 

python setup.py develop

in the extension directory.
