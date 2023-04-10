import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_number_info(phone_number):
    """
    This function takes a phone number as input and returns a dictionary with information about the number.
    """
    try:
        parsed = phonenumbers.parse(phone_number)
        country_name = geocoder.description_for_number(parsed, "en")
        carrier_name = carrier.name_for_number(parsed, "en")
        timezone_name = timezone.time_zones_for_number(parsed)[0]
        return {'Country': country_name, 'Carrier': carrier_name, 'Timezone': timezone_name}
    except:
        return {'Error': 'Invalid phone number or cannot find information'}

# Example usage
print(get_number_info("+14155552671")) # Replace this with the phone number you want to check