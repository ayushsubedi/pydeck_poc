
from flask import render_template
from pydeck_poc import application
from pydeck_poc import basic_auth
from pydeck_poc.helper import deck_example1, deck_example2
import random
import keplergl
import pandas as pd
import geopandas

@application.route('/')
def index():
    random_plot = [deck_example1(), deck_example2()]
    return render_template('poc.html',
                            first = random.choice(random_plot))


@application.route('/kepler')
def kepler():
    df = pd.DataFrame(
        {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
         'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
         'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
         'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})
    point_gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
    w1 = keplergl.KeplerGl(height=500)
    w1.add_data(data=point_gdf, name="cities")
    return str(w1)

