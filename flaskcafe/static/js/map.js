window.addEventListener('DOMContentLoaded', (event) => {
  const cafes = document.querySelectorAll('.cafe')

  var map = L.map('map').setView([50.2074, -0.1015], 12)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map)
  var redIcon = new L.Icon({
    iconUrl:
      'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl:
      'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  })

  var newIcon = new L.Icon({
    iconUrl:
      'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl:
      'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [35, 50],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  })

  cafes.forEach((cafe) => {
    const split_coordinates = JSON.parse(cafe.dataset.coordinate)
    const cafe_name = cafe.dataset.name
    const cafe_img = cafe.dataset.url

    L.marker(split_coordinates, { icon: redIcon })
      .addTo(map)
      .bindPopup(
        '<strong>' +
          cafe_name +
          '</strong><br><img src=' +
          cafe_img +
          ' style="max-width: 270px" class="img-rounded" alt="oppa.." />' +
          '</>'
      )
      .openPopup()
  })

  const cafeCards = document.getElementsByClassName('cafe')
  for (cafeCard of cafeCards) {
    cafeCard.addEventListener('mouseenter', (event) => {
      const coordinates = JSON.parse(event.currentTarget.dataset.coordinate)
      map.eachLayer((layer) => {
        if (layer instanceof L.Marker) {
          if (
            layer.getLatLng()['lat'].toString() == coordinates[0] &&
            layer.getLatLng()['lng'].toString() == coordinates[1]
          ) {
            console.log('layer')
            console.log(layer)
            layer.setIcon(newIcon)
            console.log(layer.getIcon())
            layer.openPopup()
            return
          }
        }
      })
    })
    cafeCard.addEventListener('mouseleave', (event) => {
      const coordinates = JSON.parse(event.currentTarget.dataset.coordinate)
      map.eachLayer((layer) => {
        if (layer instanceof L.Marker) {
          if (
            layer.getLatLng()['lat'].toString() == coordinates[0] &&
            layer.getLatLng()['lng'].toString() == coordinates[1]
          ) {
            console.log('layer')
            console.log(layer)
            layer.setIcon(redIcon)
            console.log(layer.getIcon())
            layer.openPopup()
            return
          }
        }
      })
    })
  }
})
document.addEventListener('DOMContentLoaded', function () {
  // add padding top to show content behind navbar
  navbar_height = document.querySelector('.navbar').offsetHeight
  document.body.style.paddingTop = navbar_height + 'px'
})

var new_icon = L.AwesomeMarkers.icon({
  extraClasses: 'fa-rotate-0',
  icon: 'link',
  iconColor: 'white',
  markerColor: 'orange',
  prefix: 'glyphicon',
})
