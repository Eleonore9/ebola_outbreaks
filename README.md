##Humanitarian data analysis - Ebola outbreaks


####Data source:

CSV of Ebola outbreaks before 2014 from the humanitarian data exchange (HDX).
See [here](https://data.hdx.rwlabs.org/dataset/ebola-outbreaks-before-2014)


####Cleaning:

* Get the date range into a start date and en date.
See [notebook](https://github.com/Eleonore9/ebola_outbreaks/blob/master/1_format_dates_add_duration.ipynb)

* Get countries 2 letters ISO code.
See [notebook](https://github.com/Eleonore9/ebola_outbreaks/blob/master/2_add_iso_countries_codes.ipynb)


####Adding data:

* Add coordinates.
See [notebook](https://github.com/Eleonore9/ebola_outbreaks/blob/master/3_add_coordinates.ipynb)

* Add geometry.
See [notebook](https://github.com/Eleonore9/ebola_outbreaks/blob/master/4_add_geometry.ipynb)


####Analysis:
* Geocoding + plotting with GeoPy and Geoplotlib.
See [notebook](https://github.com/Eleonore9/ebola_outbreaks/blob/master/test_geopy_geoplotlib.ipynb)


####Visualisation:
[Cartodb map](https://eleo.cartodb.com/viz/eb27aace-9475-11e5-b6d6-0ecd1babdde5/public_map)


![map-ebola-subtypes](img/ebola_outbreaks_before_2014_1_by_eleonore_11_28_2015.png)
