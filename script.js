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

function previewImageByImg(event){

//	document.getElementById("editbox").style.display="block";
	var reader =  new FileReader();
	var imageField = document.getElementById("image-field")

	reader.onload = function(){
		if(reader.readyState == 2){
			imageField.src = reader.result; 
		}
	}
	reader.readAsDataURL(event.target.files[0]);
}

function previewImageByURL(event){
	var imageurl = document.getElementById("upurl").value
	var img = document.getElementById("image-field")
	img.src = imageurl
}