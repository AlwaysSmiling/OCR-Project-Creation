function imageload()
{
	document.getElementById("editbox").style.display="block";
}

function showdnld()
{
	document.getElementById("step3").style.display="block";
}

function dropdown() {
  var x = document.getElementById("drpdwn");
  if (x.className.indexOf("w3-show") == -1) { 
    x.className += " w3-show";
  } else {
    x.className = x.className.replace(" w3-show", "");
  }
}