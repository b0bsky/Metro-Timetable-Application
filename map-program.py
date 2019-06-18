import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView

sys.argv.append("--disable-web-security")
app = QApplication(sys.argv)

transport = "TRANSIT"
origin = input("Please enter latitude and longitude coordinates for your current location, separated by a comma: ")
destination = input("Please enter latitude and longitude coordinates for where you want to go, separated by a comma: ")
origin_lat, origin_lng = origin.split(",")
destination_lat, destination_lng = destination.split(",")
raw_html = f'''
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Travel Modes in Directions</title>
    <style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {{
        height: 100%;
      }}
      /* Optional: Makes the sample page fill the window. */
      html, body {{
        height: 100%;
        margin: 0;
        padding: 0;
      }}
      #floating-panel {{
        position: absolute;
        top: 10px;
        left: 25%;
        z-index: 5;
        background-color: #fff;
        padding: 5px;
        border: 1px solid #999;
        text-align: center;
        font-family: 'Roboto','sans-serif';
        line-height: 30px;
        padding-left: 10px;
      }}
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      function initMap() {{
        var directionsDisplay = new google.maps.DirectionsRenderer;
        var directionsService = new google.maps.DirectionsService;
        var map = new google.maps.Map(document.getElementById('map'), {{
          zoom: 14,
          center: {{lat: -43.53425805, lng: 172.6370746}}
        }});
        directionsDisplay.setMap(map);

        calculateAndDisplayRoute(directionsService, directionsDisplay);

      }}
      function calculateAndDisplayRoute(directionsService, directionsDisplay) {{
        directionsService.route({{
          origin: {{lat: {origin_lat}, lng: {origin_lng}}},  // Lincoln University.
          destination: {{lat: {destination_lat}, lng: {destination_lng}}},  // Bus Interchange.
          // Note that Javascript allows us to access the constant
          // using square brackets and a string value as its
          // "property."
          travelMode: google.maps.TravelMode['{transport}']
        }}, function(response, status) {{
          if (status == 'OK') {{
            directionsDisplay.setDirections(response);
          }} else {{
            window.alert('Directions request failed due to ' + status);
          }}
        }});
      }}
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=REDACTED">
    </script>
  </body>
</html>
'''

view=QWebEngineView()
view.setHtml(raw_html)
view.show()

sys.exit(app.exec_())