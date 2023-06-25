// var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";

// for (var i = 0; i < positions.length; i++) {

//     var imageSize = new kakao.maps.Size(24, 35);

//     var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
//     var marker = new kakao.maps.Marker({
//         map: map,
//         position: positions[i].latlng,
//         title: positions[i].title,
//         image: markerImage
//     });

//     // 팝업
//     // 닫기 말고 x 버튼으로 추가해야 됨
//     kakao.maps.event.addListener(marker, 'click', function () {
//         var markerTitle = this.getTitle();
//         var markerInfo;
//         var popUp = document.querySelector('#popup');

//         for (var j = 0; j < positions.length; j++) {
//             if (positions[j].title === markerTitle) {
//                 markerInfo = positions[j];
//                 break;
//             }
//         }

//         if (markerInfo) {
//             var content =
//                 '<div class="popup_content">' +
//                 '   <p>' + markerInfo.title + '</p>' +
//                 '   <p>위치: ' + markerInfo.location + '</p>' +
//                 '   <p>운영시간: ' + markerInfo.time + '</p>' +
//                 '</div>';

//             document.querySelector('.info_content').innerHTML = content;
//             popUp.style.display = 'block';
//         }
//     });

//     var closeBtn = document.querySelector('.btn_close');
//     closeBtn.addEventListener('click', function () {
//         this.parentNode.parentNode.style.display = 'none';
//     });
// };