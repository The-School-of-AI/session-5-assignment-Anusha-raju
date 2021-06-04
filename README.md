# Session5 Assignment



##### The following topics were covered: *Functional Parameters*
- Argument vs Parameter
- Positional and keyword Arguments
- Unpacking Iterables 
- Extended Unpacking 
- _*args_ 
- Keyword Arguments
- _**kwags_
- Args and Kwargs together
- DocStrings and Annotations

### ASSIGNMENT:
Write a function that gives out the average run time per call, such that its definition is:

def time_it(fn, *args, repetitions= 1, **kwargs) : {your code comes here.}

***We should be able to call it like this***:

- time_it(print, 1, 2, 3, sep='-', end= ' ***\n'. repetitons=5)
- time_it(squared_power_list, 2, start=0, end=5, repetitons=5) *2 is the number you are calculating power of, [1, 2, 4, 8, 16, 32]*
- time_it(polygon_area, 15, sides = 3, repetitons=10) *15 is the side length. This polygon supports area calculations of upto a hexagon*
- time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100) *100 is the base temperature given to be converted*
- time_it(speed_converter, 100, dist='km', time='min', repetitons=200) *dist can be km/m/ft/yrd, time can be ms/s/m/hr/day, speed given by user is in kmph*





##  SOLUTION:

The session5.py file has the following functions:

- [time_it](#time_it)
- [squared_power_list](#squared_power_list)
- [polygon_area](#polygon_area)
- [temp_converter](#temp_converter)
- [speed_converter](#speed_converter)





# time_it 

This is a generalized function to call any function user specified number of times and return the average time taken for calls. Takes 1 positional argument ***fn***: *function* and 1 keyword argument ***repetitions***.



***Tests for time_it function:***

|              TEST FUNCTIONS              |                     DESCRIPTION                      |
| :--------------------------------------: | :--------------------------------------------------: |
|       test_session5_time_it_print        |          Tests time_it with print function           |
| test_session5_time_it_squared_power_list |      Tests  time_it with squared_power function      |
|    test_session5_time_it_polygon_area    |       Tests time_it with polygon_area function       |
|   test_session5_time_it_temp_converter   |      Tests time_it with temp_converter function      |
|  test_session5_time_it_speed_converter   |     Tests time_it with speed_converter function      |
|      test_session5_time_it_no_args       |           Tests time_it with no arguments            |
| test_session5_time_it_incorrect_pos_args | Tests time_it with non existing positional arguments |
|      test_session5_time_it_zero_rep      |          Tests time_it with zero repetation          |





# squared_power_list

Returns list by raising number to power from start to end. Takes 2 keyword arguments ***start*** and ***end*** & 1 positional argument ***number***.

|                    TEST FUNCTIONS                     |                         DESCRIPTION                          |
| :---------------------------------------------------: | :----------------------------------------------------------: |
|       test_session5_squared_power_list_no_args        | Tests squared_power function for no mandatory positional arguments |
|  test_session5_squared_power_list_incorrect_pos_args  | Tests squared_power_list function for incorrect values for positional arguments |
| test_session5_squared_power_list_incorrect_start__end | Tests squared_power_list function for incorrect value to start and end keyword arguments |
|     test_session5_squared_power_list_start_gt_end     | Tests  squared_power_list function for start value greater than end |
|     test_session5_squared_power_list_number_gt_10     | Tests  squared_power_list function for number value greater than 10 |
|    test_session5_squared_power_list_unwanted_args     | Tests  squared_power_list function for unwanted positional/keyword arguments |
|        test_session5_squared_power_list_output        | Tests  squared_power_list function for output with multiple inputs |







# polygon_area

Returns area of a regular polygon with number of sides between 3 to 6 both inclusive. Takes 1 positional argument ***length***  and 1 keyword argument ***sides***.







|              TEST FUNCTIONS              |                         DESCRIPTION                          |
| :--------------------------------------: | :----------------------------------------------------------: |
|        test_session5_polygon_area        | Tests polygon_area function for no mandatory positional arguments |
|    test_session5_polygon_area_length     | Tests polygon_area function for incorrect values for positional argument length |
|     test_session5_polygon_area_sides     | Tests polygon_area function for incorrect value to sides keyword argument |
| test_session5_polygon_area_sides_values  | Tests polygon_area function for permissible values for sides |
| test_session5_polygon_area_length_values | Tests polygon_area function for permissible values for length(len > 0) |
| test_session5_polygon_area_unwanted_args | Tests  polygon_area function for unwanted positional/keyword arguments |
|    test_session5_polygon_area_output     | Tests polygon_area  function for output with multiple inputs |





# temp_converter

Converts temperature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius. Takes 1 positional argument ***temp*** and 1 keyword argument ***temp_given_in***.





|                     TEST FUNCTIONS                     |                         DESCRIPTION                          |
| :----------------------------------------------------: | :----------------------------------------------------------: |
|              test_session5_temp_converter              | Tests temp_converter function for no mandatory positional arguments |
|           test_session5_temp_converter_temp            | Tests temp_converter function for incorrect values for positional argument temp |
|       test_session5_temp_converter_temp_given_in       | Tests temp_converter function for incorrect value to temp_given_in keyword argument |
|  test_session5_temp_converter_temp_values_in_celsius   | Tests temp_converter function for permissible values for temprature in celsius |
| test_session5_temp_converter_temp_values_in_fahrenheit | Tests temp_converter function for permissible values for temprature in fahrenheit |
|       test_session5_temp_converter_unwanted_args       | Tests temp_converter function for unwanted positional/keyword arguments |
|   test_session5_temp_converter_output_in_fahrenheit    | Tests  temp_converter function for output with multiple inputs in fahrenheit |
|     test_session5_temp_converter_output_in_celsius     | Tests temp_converter function for output with multiple inputs in celsius |





# speed_converter

Converts speed from kmph (provided by user as input) to different units ***dist*** can be km/m/ft/yrd ***time*** can be ms/s/min/hr/day. Takes 1 positional argument ***speed*** and 2 keyword argument *dist* and *time* .







|                   TEST FUNCTIONS                   |                         DESCRIPTION                          |
| :------------------------------------------------: | :----------------------------------------------------------: |
|           test_session5_speed_converter            | Tests speed_converter function for no mandatory positional arguments |
|        test_session5_speed_converter_speed         | Tests speed_converter function for incorrect values for positional argument temp |
|         test_session5_speed_converter_dist         | Tests speed_converter function for incorrect type of value for dist keyword argument |
|         test_session5_speed_converter_time         | Tests speed_converter function for incorrect type of value for time keyword argument |
| test_session5_speed_converter_speed_allowed_values | Tests speed_converter function for permissible value for speed argument |
| test_session5_speed_converter_time_allowed_values  | Tests speed_converter function for permissible value for time keyword argument |
| test_session5_speed_converter_dist_allowed_values  | Tests speed_converter function for permissible value for dist keyword argument |
|    test_session5_speed_converter_unwanted_args     | Tests speed_converter function for unwanted positional/keyword arguments |
|     test_session5_speed_converter_output_km_to     | Tests speed_converter function for output with multiple inputs from km/(x), x can be ms/s/min/hr/day |
|     test_session5_speed_converter_output_m_to      | Tests speed_converter function for output with multiple inputs from m/(x), x can be ms/s/min/hr/day |
|     test_session5_speed_converter_output_ft_to     | Tests speed_converter function for output with multiple inputs from ft/(x), x can be ms/s/min/hr/day |
|    test_session5_speed_converter_output_yrd_to     | Tests speed_converter function for output with multiple inputs from yrd/(x), x can be ms/s/min/hr/day |







### Session5.py file formatting test cases:

|                  TEST FUNCTIONS                   |                         DESCRIPTION                          |
| :-----------------------------------------------: | :----------------------------------------------------------: |
|            test_session5_readme_exists            |                  Checks if README.md exists                  |
|          test_session5_readme_500_words           |        Checks if README.md file has atleast 500 words        |
|      test_session5_readme_proper_description      | Checks for proper description of all the functions/classes in README.md file |
| test_session5_readme_file_for_more_than_10_hashes |         Checks if README.md file has proper headings         |
|            test_session5_indentations             |     Checks if session5.py file has significant indenting     |
|    test_session5_function_name_had_cap_letter     |    Checks if Capital letter(s) are used in function names    |

