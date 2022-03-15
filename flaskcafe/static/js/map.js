window.addEventListener('DOMContentLoaded', (event) => {
  const cafes = document.querySelectorAll('.cafe')

  var map = L.map('map').setView([50.2074, -0.1015], 12)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map)

  cafes.forEach((cafe) => {
    split_coordinates = JSON.parse(cafe.dataset.coordinate)
    cafe_name = cafe.dataset.name
    cafe_img = cafe.dataset.url
    L.marker(split_coordinates)
      .addTo(map)
      .bindPopup(
        '<a href="/admin">' +
          '<strong>' +
          cafe_name +
          '</strong><br><img src=' +
          cafe_img +
          ' style="max-width: 270px" class="img-rounded" alt="oppa.." />' +
          '</>'
      )
      .openPopup()
  })
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
marker_52bf37d9345b45c78962ea1a22d3c5fc.setIcon(new_icon)

marker_52bf37d9345b45c78962ea1a22d3c5fc.bindTooltip(
  `<div>
                   click for more
               </div>`,
  { sticky: true }
)
