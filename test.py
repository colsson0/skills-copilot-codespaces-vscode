def convert_distance_to_metric(distance):
    return distance * 0.3048

def convert_distance_to_imperial(distance):
    return distance / 0.3048

def convert_weight_to_metric(weight):
    return weight * 0.453592

def convert_weight_to_imperial(weight):
    return weight / 0.453592

def convert_temperature_to_metric(temperature):
    return (temperature - 32) * 5/9

def convert_temperature_to_imperial(temperature):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    temperature (float): The temperature in Celsius.

    Returns:
    float: The temperature in Fahrenheit.
    """
    return (temperature * 9/5) + 32

def convert_volume_to_metric(volume):
    return volume * 3.78541

def convert_volume_to_imperial(volume):
    return volume / 3.78541
