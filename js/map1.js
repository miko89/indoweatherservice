

    

        // center of the map
        var center = [8.0, 118.662089];

        // Create the map
        var map = L.map('map', {
            maxZoom: 10,
            minZoom: 4,
        }).setView(center, 4);

        // Set up the OSM layer
        L.tileLayer(
            'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Data © <a href="http://osm.org/copyright">OpenStreetMap</a>',
            maxZoom: 10
        }).addTo(map);

        var imageUrl = '/img/fdrs2.png';
        var size = [28.2, 90];
        imageBounds = [[-12.834076, 145], size];

        L.imageOverlay(imageUrl, imageBounds).addTo(map);

       


