class TemperatureConverter(object):
    @classmethod
    def get_conversion(self, value, desired_unit):
        """
        Perform conversion of the value to the desired unit
        :param value: Temperature value
        :param desired_unit: Desired unit
        :return: float: Temperature in desired unit
        """
        if desired_unit == "C":
            return self.to_celsius(float(value))
        else:
            return self.to_fahrenheit(float(value))

    @staticmethod
    def to_fahrenheit(value):
        """
        Convert from Celsius to Fahrenheit
        :param value: Temperature in Celsius
        :return: float: Temperature in Fahrenheit
        """
        return (value * 9/5) + 32

    @staticmethod
    def to_celsius(value):
        """
        Convert from Fahrenheit to Celsius
        :param value: Temperature in Fahrenheit
        :return: float: Temperature in Celsius
        """
        return (value - 32) * 5/9