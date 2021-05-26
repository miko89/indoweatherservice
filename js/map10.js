
// center of the map
var center = [8.0, 118.662089];

// Create the map
var map = L.map('mapid', {
    maxZoom: 10,
    minZoom: 4,
}).setView(center, 4);

// Set up the OSM layer
L.tileLayer(
    'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Data © <a href="http://osm.org/copyright">OpenStreetMap</a>',
    maxZoom: 10
}).addTo(map);


var geojsonLayer = new L.GeoJSON.AJAX("/radardata/Kecamatan_DKI.json", {
    style: {
        fillColor: "#ff7800",
        fillOpacity: 0.7,
        color: "white",
        weight: 1,
        opacity: 0.7
    }
});
geojsonLayer.addTo(map);

document.getElementById("dataid1").addEventListener("change", function () {
    if (document.getElementById(this.id).checked == true) {
        geojsonLayer.addTo(map);
    } else {
        geojsonLayer.remove(map);
    }
});






