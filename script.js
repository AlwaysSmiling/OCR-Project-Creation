var img = new Image();
var canvas = document.getElementById("imagecanvas");
var ctx = canvas.getContext("2d");


var l = document.getElementById("lan");
var t = document.getElementById("typ");


function PreviewImage(event){
	var inj = event.target;
	var reader =  new FileReader();
	
	reader.onload = function(){
		var dataURL = reader.result;
		img.src = dataURL; 
	}
	reader.readAsDataURL(inj.files[0]);
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

img.onload = function(){
	if(img.naturalWidth < canvas.width && img.naturalHeight < canvas.height){
		var xpos = (canvas.width - img.naturalWidth)/2;
		ctx.drawImage(img,xpos,0);
	}
	else
		ctx.drawImage(img,0,0,canvas.width,canvas.height);
}

function rotate(conf) { 
     
    var roimage = new Image(); 
    roimage.src = canvas.toDataURL(), 
    roimage.onload = function() { 
            ctx.clearRect(0, 0, canvas.width, canvas.height); 
            ctx.translate(conf.x, conf.y); 
            ctx.rotate(conf.r); 
            ctx.drawImage(this, 0, 0);   
    } 
}


function rotateL(){
	conf= {
		x : 0,
		y : canvas.height,
		r : -90 * Math.PI / 180
	};
	rotate(conf);
}

function rotateR(){
	conf= {
		x : canvas.width,
		y : 0,
		r : 90 * Math.PI / 180
	};
	rotate(conf);
}

function scale(){
	ctx.scale(2,2);
}


function showdownload()
{
	document.getElementById("ocrrec").innerHTML = "Please Wait.....";
	
	var xhr = new XMLHttpRequest();

	switch(t.value()){
		case 1:
			switch(l.value()){
				case 1:
					
					break;
				case 2:
					
					break;
			}
			break;
		case 2:
			switch(l.value()){
				case 1:
					
					break;
				case 2:
					
					break;
			}
			break;
		case 3:
			switch(l.value()){
				case 1:
					
					break;
				case 2:
					
					break;
			}
			break;
	}
}