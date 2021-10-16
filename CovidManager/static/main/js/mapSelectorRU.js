

$('path').hover(function(e){


  $('.indicator').html('');
  var id = $(this).attr('id').toUpperCase();
  cases = $(this).attr('cases')
  deaths = $(this).attr('deaths')
  if($(this).attr('name')) {
    var name = $(this).attr('name');
    $('<div><div class="strong">' + name +'</div>' +
    '<div class="d-flex  justify-content-end">' + cases +' случаев</div>' +
    '<div class="d-flex justify-content-end">' + deaths +' умерших</div></div>').appendTo('.indicator');
  }

$("path").click(function(e){
//        alert("button"+ this);
        r = $(this).attr('name')
        window.location.replace("?region="+r);

    });

//  if($(this).attr('flag')) {
//    console.log($(this).attr('flag'));
//    var flag = "map/ru/" + $(this).attr('flag') ;
//    $(' <img class="flag" src="" alt="">').appendTo('.indicator');
//    $('.indicator').find('img').attr('src',flag )
//   // $('<img src='+ flag+ ' >').appendTo('.indicator');
// }

 $('.change').remove();

// var script = document.createElement('script');
//  script.classList.add('change');
// script.src = 'http://api.geonames.org/countryInfoJSON?country='+info[id]+'&username=pixeltest&style=full&callback=update';
//  document.body.appendChild(script);

  $(this).css('fill','#f6e72d');
//  $('path').not(this).css('fill','rgba(0,0,0,0.5)');
  offset = $('svg').offset()
  $('.indicator').css({'top':e.pageY - offset.top ,'left':e.pageX-offset.left+30}).show();



},function(e){
  $('.indicator').html('');
  $('.indicator').hide();
  $(this).css('fill',$(this).attr("color_d"));
  console.log("color_d", $(this).attr("color_d"))

});





var idAarr = ["RU-MOW", "RU-SPE", "RU-NEN", "RU-YAR", "RU-CHE", "RU-ULY", "RU-TYU", "RU-TUL", "RU-SVE", "RU-RYA", "RU-ORL", "RU-OMS", "RU-NGR", "RU-LIP", "RU-KRS", "RU-KGN", "RU-KGD", "RU-IVA", "RU-BRY", "RU-AST", "RU-KHA", "RU-CE", "RU-UD", "RU-SE", "RU-MO", "RU-KR", "RU-KL", "RU-IN", "RU-AL", "RU-BA", "RU-AD", "RU-CR", "RU-SEV", "RU-KO", "RU-KIR", "RU-PNZ", "RU-TAM", "RU-MUR", "RU-LEN", "RU-VLG", "RU-KOS", "RU-PSK", "RU-ARK", "RU-YAN", "RU-CHU", "RU-YEV", "RU-TY", "RU-SAK", "RU-AMU", "RU-BU", "RU-KK", "RU-KEM", "RU-NVS", "RU-ALT", "RU-DA", "RU-STA", "RU-KB", "RU-KC", "RU-KDA", "RU-ROS", "RU-SAM", "RU-TA", "RU-ME", "RU-CU", "RU-NIZ", "RU-VLA", "RU-MOS", "RU-KLU", "RU-BEL", "RU-ZAB", "RU-PRI", "RU-KAM", "RU-MAG", "RU-SA", "RU-KYA", "RU-ORE", "RU-SAR", "RU-VGG", "RU-VOR", "RU-SMO", "RU-TVE", "RU-PER", "RU-KHM", "RU-TOM", "RU-IRK"];
var idAarr2 = new Array(['RU-MOW', 'Москва', 'moscow.gif', '213', '29'], ['RU-CHE', 'Челябинская область', 'chelyabinskaya_flag.png', '11225', '80'], ['RU-ORL', 'Орловская область', '', '10772', '38'], ['RU-OMS', 'Омская область', 'flag_omskoj_oblasti.png', '11318', '36'], ['RU-LIP', 'Липецкая область', 'lipeckya.jpg', '10712', '27'], ['RU-KRS', 'Курская область', 'flag_of_kursk_oblast.png', '10705', '25'], ['RU-RYA', 'Рязанская область', 'ryazan.png', '10776', '62'], ['RU-BRY', 'Брянская область', 'bryanskaya_flag.png', '10650', '5'], ['RU-KIR', 'Кировская область', 'flag_kirovskoy_oblasti.png', '11070', '20'], ['RU-ARK', 'Архангельская область', '', '10842', '2'], ['RU-MUR', 'Мурманская область', '', '10897', '31'], ['RU-SPE', 'Санкт-Петербург', '', '2', '64'], ['RU-YAR', 'Ярославская область', '', '10841', '85'], ['RU-ULY', 'Ульяновская область', '', '11153', '77'], ['RU-NVS', 'Новосибирская область', '', '11316', '35'], ['RU-TYU', 'Тюменская область', '', '11176', '75'], ['RU-SVE', 'Свердловская область', '', '11162', '67'], ['RU-NGR', 'Новгородская область', '', '10904', '34'], ['RU-KGN', 'Курганская область', '', '11158', '24'], ['RU-KGD', 'Калининградская область', '', '10857', '15'], ['RU-IVA', 'Ивановская область', '', '10687', '12'], ['RU-AST', 'Астраханская область', '', '10946', '3'], ['RU-KHA', 'Хабаровский край', '', '11457', '78'], ['RU-CE', 'Чеченская Республика', '', '11024', '81'], ['RU-UD', 'Удмуртская Республика', '', '11148', '76'], ['RU-SE', 'Республика Северная Осетия — Алания', '', '11021', '56'], ['RU-MO', 'Республика Мордовия', '', '11117', '54'], ['RU-KR', 'Республика Карелия', '', '10933', '50'], ['RU-KL', 'Республика Калмыкия', '', '11015', '49'], ['RU-IN', 'Республика Ингушетия', '', '11012', '48'], ['RU-AL', 'Республика Алтай', '', '10231', '44'], ['RU-BA', 'Республика Башкортостан', '', '11111', '45'], ['RU-AD', 'Республика Адыгея', '', '11004', '43'], ['RU-CR', 'Республика Крым', '', '977', '52'], ['RU-SEV', 'Севастополь', '', '959', '68'], ['RU-KO', 'Республика Коми', '', '10939', '51'], ['RU-PNZ', 'Пензенская область', '', '11095', '39'], ['RU-TAM', 'Тамбовская область', '', '10802', '71'], ['RU-LEN', 'Ленинградская область', '', '10174', '26'], ['RU-VLG', 'Вологодская область', '', '10853', '8'], ['RU-KOS', 'Костромская область', '', '10699', '21'], ['RU-PSK', 'Псковская область', '', '10926', '42'], ['RU-YAN', 'Ямало-Ненецкий автономный округ', '', '11232', '84'], ['RU-CHU', 'Чукотский автономный округ', '', '10251', '83'], ['RU-YEV', 'Еврейская автономная область', '', '10243', '10'], ['RU-TY', 'Республика Тыва', '', '10233', '58'], ['RU-SAK', 'Сахалинская область', '', '11450', '66'], ['RU-AMU', 'Амурская область', '', '11375', '1'], ['RU-BU', 'Республика Бурятия', '', '11330', '46'], ['RU-KK', 'Республика Хакасия', '', '11340', '59'], ['RU-KEM', 'Кемеровская область', '', '11282', '19'], ['RU-ALT', 'Алтайский край', '', '11235', '0'], ['RU-DA', 'Республика Дагестан', '', '11010', '47'], ['RU-KB', 'Кабардино-Балкарская Республика', '', '11013', '14'], ['RU-KC', 'Карачаево-Черкесская Республика', '', '11020', '18'], ['RU-KDA', 'Краснодарский край', '', '10995', '22'], ['RU-ROS', 'Ростовская область', '', '11029', '61'], ['RU-SAM', 'Самарская область', '', '11131', '63'], ['RU-TA', 'Республика Татарстан', '', '11119', '57'], ['RU-ME', 'Республика Марий Эл', '', '11077', '53'], ['RU-CU', 'Чувашская Республика', '', '11156', '82'], ['RU-NIZ', 'Нижегородская область', '', '11079', '33'], ['RU-VLA', 'Владимирская область', '', '10658', '6'], ['RU-MOS', 'Московская область', '', '1', '30'], ['RU-KLU', 'Калужская область', '', '10693', '16'], ['RU-BEL', 'Белгородская область', '', '10645', '4'], ['RU-ZAB', 'Забайкальский край', '', '21949', '11'], ['RU-PRI', 'Приморский край', '', '11409', '41'], ['RU-KAM', 'Камчатский край', '', '11398', '17'], ['RU-MAG', 'Магаданская область', '', '11403', '28'], ['RU-SA', 'Республика Саха (Якутия)', '', '11443', '55'], ['RU-KYA', 'Красноярский край', '', '11309', '23'], ['RU-ORE', 'Оренбургская область', '', '11084', '37'], ['RU-SAR', 'Саратовская область', '', '11146', '65'], ['RU-VGG', 'Волгоградская область', '', '10950', '7'], ['RU-VOR', 'Ставропольский край', '', '11069', '70'], ['RU-SMO', 'Смоленская область', '', '10795', '69'], ['RU-TVE', 'Тверская область', '', '10819', '72'], ['RU-PER', 'Пермский край', '', '11108', '40'], ['RU-KHM', 'Ханты-Мансийский автономный округ — Югра', '', '11193', '79'], ['RU-KHM', 'Ханты-Мансийский автономный округ — Югра', '', '11193', '79'], ['RU-TOM', 'Томская область', '', '11353', '73'], ['RU-IRK', 'Иркутская область', '', '11266', '13'], ['RU-NEN', 'Ямало-Ненецкий автономный округ', '', '11232', '84'], ['RU-STA', 'Ставропольский край', '', '11069', '70'], ['RU-TUL', 'Тульская область', 'tulskaya_flag.png', '10832', '74']);

$('path').each(function() {

  var regId = $(this).attr('id');
  var flag = '';
  var name = '';
  console.log("regId: " + regId)
  for (var j = 0; j < idAarr2.length; j++) {


    if (regId == idAarr2[j][0]) {
      name = idAarr2[j][1];
      console.log(regId, j, idAarr2[j])
      flag =  'flags/'+ idAarr2[j][2];
      yid = idAarr2[j][3]
      aid = idAarr2[j][4]
      cases = regions[aid][1]
      deaths = regions[aid][3]
      color_d = 'rgba(252, 135, 135, '+ (deaths / 7000  + 0.3) +')'
      console.log(color_d)
      $(this).css('fill',color_d);
      $(this).attr('color_d', color_d);
      $(this).attr('name', name);
      $(this).attr('flag', flag);
      $(this).attr('yid', yid);
      $(this).attr('cases', cases);
      $(this).attr('deaths', deaths);
    }
  }


  var regIdDiv = '<div class="reg" >'+ '[' + '<span>'+  regId +'</span>' + ']' +' '+ name +'</div>'
  $(regIdDiv).appendTo('.regs');


// var idArrMin = [regId, '_'];
// idAarr2.push(idArrMin);


})


// for (var j = 0; j < idAarr2.length; j++) {
//   if (regId == idAarr2[j][0]) {
//     name = cyr2latChars[j][1];

//   }
// }

//revertFill();


$('.reg').hover(function(e) {


  var id = $(this).find('span').text();

  idHover = '#' + id;

  $(idHover).css('fill','#f6e72d');
 // $('path').not(this).css('fill','rgba(0,0,0,0.5)');
 // $('.indicator').css({'top':e.pageY,'left':e.pageX+30}).show();

},function(){
  $('.indicator').html('');
  $('.indicator').hide();
  $('path').css('fill','rgba(0,0,0,0.2)');
});

//} // revertFill
