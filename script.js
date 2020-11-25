var img = new Image();
var c = document.getElementById("imagecanvas");
var ctx = c.getContext("2d");

function PreviewImage(event){
	var reader =  new FileReader();
	reader.onload = function(event){
		if(reader.readyState == 2){
			img.src = reader.result; 
			}
	}
	reader.readAsDataURL(e.target.files[0]);
}

function previewImageByURL(event){
	img.src = document.getElementById("upurl").value;
}

function imageload()
{
	document.getElementById("editbox").style.display="block";
	
}


function showOCRops()
{
	document.getElementById("step3").style.display="block";
}

function showdownload()
{
	document.getElementById("ocrrec").innerHTML = "Please Wait.....";
}

img.onload = function(){
	ctx.drawimage(img,0.5,0.5);
}