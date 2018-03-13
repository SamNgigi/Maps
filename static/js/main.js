// GOOGLE MAPS

// This code is not being used. It is here for referal purpose and just in case.

console.log('working');



// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

/*
We initialize the map and the infoWindow vars.

Below we are also storing our views.py variables as javascript vars that we can then pass in as map variables.
*/
var map, infoWindow;
var lat = "{{latitude}}";
latitude = parseFloat(lat)
console.log(latitude)

var lng = "{{longitude}}";
longitude = parseFloat(lng);
console.log(longitude)

/*
The initMap function is responsible for rendering the map. It has a couple of functions within it.

1. We store the map configurations in our map var. i.e the longitude and latitude and we also set the map zoom.
2. We create the addMarker function for creating a marker
3. We also add an event listener so that a marker appears where we click.
*/

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 14
    });

      // Add Marker Function
      function addMarker(props) {
          var marker = new google.maps.Marker({
              position: props.coords,
              map: map,
              //icon:props.iconImage
          });


      }

    // Listen for click on map.
      google.maps.event.addListener(map, 'click', function (event) {
          // Add marker
          addMarker({
              coords: event.latLng
          });
      });

    infoWindow = new google.maps.InfoWindow;

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            infoWindow.setPosition(pos);
            infoWindow.setContent('Location found.');
            infoWindow.open(map);
            map.setCenter(pos);
        }, function () {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
        'Error: The Geolocation service failed.' :
        'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}
