import requests
import pydeck as pdk
from pydeck_poc import application


def deck_example():
    UK_ACCIDENTS_DATA = 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv'
    layer = pdk.Layer(
        'HexagonLayer',  # `type` positional argument is here
        UK_ACCIDENTS_DATA,
        get_position=['lng', 'lat'],
        auto_highlight=True,
        elevation_scale=50,
        pickable=True,
        elevation_range=[0, 3000],
        extruded=True,
        coverage=1)

    # Set the viewport location
    view_state = pdk.ViewState(
        longitude=-1.415,
        latitude=52.2323,
        zoom=6,
        min_zoom=5,
        max_zoom=15,
        pitch=40.5,
        bearing=-27.36)

    # Combined all of it and render a viewport
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, mapbox_key=application.config['MAPBOX_AUTH'])
    return r.to_html(filename=None, as_string=True)
