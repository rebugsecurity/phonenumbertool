# phonenumbertool
Here, we are using the phonenumbers library to parse the input phone number and extract information about it. We then define a function get_number_info which takes a phone number as input, uses the geocoder, carrier, and timezone methods of the phonenumbers library to retrieve information about the number, and returns a dictionary with the country name, carrier name, and timezone.

You can replace the example phone number ('+14155552671') with any phone number you want to check. If the phone number is valid and information is found, the function will return a dictionary with the number information. If the phone number is invalid or information cannot be found, the function will return a dictionary with an error message.

# installing requirements.
``sudo pip3 install -r requirements.txt``

# usage
``python3 phonelocate.py``
