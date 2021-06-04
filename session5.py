""" Session5:Write a function that gives out the average run time per call"""
import time
import math


def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    avg_time = 0
    if not fn: #checks for a valid function
        raise NameError("Function is not defined")
    if repetitions<0: # Repetition should be positive number
        raise ValueError("Repetitions can't be zero!!!!")
    elif repetitions==0: #for zero repetition average time is zero.
        return avg_time
    else:
        start=time.perf_counter()
        for i in range(repetitions):
            fn(*args,**kwargs)
        end=time.perf_counter()
        avg_time=(end-start)/repetitions
    return avg_time


def squared_power_list(number:'non-negative integer less then 10',*args, start=0, end=5, **kwargs):
    """Returns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    if type(number) is not int: #checks if number is integer
        raise TypeError("Only integer type arguments are allowed")
    if start<0 or end<0: #checks if start and end is less than zero
        raise ValueError("Value of start or end can't be negative")
    if end<start: #start should be less than end
        raise ValueError("Value of start should be less than end")
    if number>10: #number should be less than 10
        raise ValueError("Value of number should be less than 10")
    if args: #no more positional arguments required
        raise TypeError("squared_power_list function takes maximum 1 positional arguments, more provided")
    if kwargs: #no more keyword arguments required
        raise TypeError("squared_power_list function take maximum 2 keyword/named arguments, more provided")
    my_list=[]
    for i in range(start,end):my_list.append(number**i)
    return my_list #returns list[number**start to number**end]


def polygon_area(length:'non-negative number', *args, sides = 3, **kwargs):
    """Returns area of a regular polygon with number of sides between
    3 to 6 both inclusive"""
    # Validations
    if type(length) not in [int, float]: #length should be integer or float.
        raise TypeError("Invalid length :integer or float type arguments are allowed")
    if type(sides) is not int: #sides should be integer
        raise TypeError("Invalid sides: Sides should be an integer")
    if sides<3 or sides>6: #this function calculates area of polygon with 3<=sides<=6
        raise ValueError("Sides should be greater than or equal to 3 and less than or equal to 6: 3<=sides<=6.")
    if length<0: #length is non-negative
        raise ValueError("Inappropriate length: length should be greater than 0")
    if args: #no more positional arguments required
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if kwargs: #no more keyword arguments required
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    area= (length**2 *sides)/(4*math.tan(math.radians(180/sides)))
    return area #returns the area of the polygon



def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    if type(temp) not in [int, float]: #temp should be either int or float
        raise TypeError("Invalid temp :integer or float type arguments are allowed")
    if type(temp_given_in) is not str: #temp_given_in should be string
        raise TypeError("Charcater string expected")
    if type(temp_given_in) is str and temp_given_in not in ['c','f','C','F']: #temp_given_in should be 'f' or 'c'
        raise ValueError("Only f or c is allowed")
    if args: #no more positional arguments required
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if kwargs: #no more keyword arguments required
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")
    if temp_given_in in ['c','C']:
        if temp < -273.15:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        else:
            return (temp*1.8+32) #converts celsius to fahrenheit
    if temp_given_in in ['f','F']:
        if temp < -459.67:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin*")
        else:
            return ((temp-32)/1.8) #converts fahrenheit to celsius



def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """
    if type(speed) not in [int, float]: #speed should be int or float
        raise TypeError("Speed can be int or float type only")
    if type(dist) is not str:
        raise TypeError("Charcater string expected for distance unit")
    if type(time) is not str:
        raise TypeError("Charcater string expected")
    if speed>300000: #checks for speed value
        raise ValueError("Speed can't be greater than speed of light")
    if args: #no more positional arguments required
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if kwargs: #no more keyword arguments required
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")
    if type(dist) is str and dist not in ['km','KM','m','M','ft','FT','yrd','YRD']:
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if type(time) is str and time not in ['ms','MS','s','S','min','MIN','hr','HR','day','DAY']:
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    if speed > 0: #converts speed from kmph to desired 'dist'/'time'
        if dist in ['km','KM']:
            speed = speed
        elif dist in ['m','M']:
            speed = speed * 1000
        elif dist in ['ft','FT']:
            speed = speed * 3280.84
        elif dist in ['yrd','YRD']:
            speed = speed * 1093.61
        if time in ['hr','HR']:
            speed = speed
        elif time in ['day','DAY']:
            speed = speed /0.0416667
        elif time in ['min','MIN']:
            speed = speed / 60
        elif time in ['s','S']:
            speed = speed / (60 * 60)
        elif time in ['ms','MS']:
            speed = speed / (60 * 60 * 1000)
        return round(speed) #returns speed in desired 'dist' and 'time'
    else:
        raise ValueError("Speed can't be negative")