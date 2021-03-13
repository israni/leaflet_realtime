var last_updated = new Date().getTime();
var counter = 0;
// var host = "https://wanderdrone.appspot.com/";
var host = "http://localhost:34000/";
var map = L.map("mapid"),
  trail = {
    type: "Feature",
    properties: {
      id: 1,
    },
    geometry: {
      type: "LineString",
      coordinates: [],
    },
  },
  realtime = L.realtime(
    function (success, error) {
      fetch(host)
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          var trailCoords = trail.geometry.coordinates;
          trailCoords.push(data.geometry.coordinates);
          trailCoords.splice(0, Math.max(0, trailCoords.length - 50));
          success({
            type: "FeatureCollection",
            features: [data, trail],
          });
        })
        .catch(error);
    },
    {
      interval: 200,
    }
  ).addTo(map);

L.tileLayer("http://{s}.tile.osm.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

map.on("moveend", function () {
  last_updated = new Date().getTime();
});

realtime.on("update", function () {
  var curr_time = new Date().getTime();
  console.log(curr_time);
  if (counter == 0 || curr_time - last_updated > 10 * 1000) {
    map.fitBounds(realtime.getBounds(), { maxZoom: 10 });
    first = false;
    counter += 1;
  } else {
    counter += 1;
  }
});
