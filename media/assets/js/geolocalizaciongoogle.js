var ejecutar = {
  init: function(){
    var mapa = document.getElementById("mapa");
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(ejecutar.verMapa, ejecutar.displayError);
    }
  },
  displayError: function(error){
    var errorTypes = {
      0: "Unknown error",
      1: "Permission denied by user",
      2: "Position not available",
      3: "Time out"
    };

    var errorMessage = errorTypes[error.code];
    if (error.code == 0 || error.code == 2) {
      errorMessage = errorMessage + " " + error.message;
    }
    mapa.innerHTML = errorMessage;
 },
 verMapa: function(position) {
   var googleLatAndLong = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);

	var longitude = position.coords.longitude;
	var latitude = position.coords.latitude;
	//$.post('http://localhost:8001/home',{'longitude':longitude,'latitude':latitude});
	$.get('http://aloeveraofforever.com/?longitude='+longitude+'&latitude='+latitude, function(data, callback){
	if(callback == 'success'){
		$('#geo').html(data);
	} 
	});

    // map styling
    var styleArray = [
        {
          stylers: [
            { hue: "#a5dc4f" },
            { saturation:100},
            { lightness:50 }
        ]
        },{
          featureType: "road",
          elementType: "geometry",
          stylers: [
            { visibility: "off" }
          ]
        },{
          featureType: "road",
          featureType: "city",
          elementType: "labels",
          stylers: [
            { visibility: "off" }
          ]
        }
    ];

   var mapOptions = {
     zoom: 6,
     styles: styleArray,
     center: googleLatAndLong,
     mapTypeId: google.maps.MapTypeId.ROADMAP
   };

   map = new google.maps.Map(mapa, mapOptions);

   var title = "My Location";
   var content = "I am in: " + position.coords.latitude + " Longitude: " + position.coords.longitude + " and with a certainty of " + position.coords.accuracy;
   ejecutar.addMarker(map, googleLatAndLong, title, content);
 },
 addMarker: function(map, latlong, title, content){
    var markerOptions = {
      position: latlong, map: map, title: title, clickable: true, icon: new google.maps.MarkerImage("http://aloeveraofforever.com/media/assets/img/flp/smallLogo.png"),
    };
    var infoWindowOptions = {
      content: content, position: latlong
    };

    var infoWindow = new google.maps.InfoWindow(infoWindowOptions);

    var marker = new google.maps.Marker(markerOptions);
    google.maps.event.addListener(marker, "click", function(){
      infoWindow.open(map);
    });

 }

};

ejecutar.init()