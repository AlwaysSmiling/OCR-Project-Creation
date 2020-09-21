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

/*function editImagef1(){
	const ImageEditor = new FilerobotImageEditor();
	const img = document.getElementById("image-field")
	ImageEditor.open("img.src");

}
function editImagef2(){
	{var featherEditor = new Aviary.Feather({
		apiKey: "8def6d87d3f24bf8aff5215edfe76545",
		apiVersion: 3,
		onSave: function(imageID, newURL){
			var img = document.getElementById(imageID);
			img.src= newURL;
		}
	});
function launchEditor(id,src){
	featherEditor.launch({
		image: id,
		url:src
	});
	return false;
}}
const img_src = document.getElementById("image-field").src
return launchEditor("image-field","img_src");
}

function editImage(){
	var croppr = new Croppr("#image-field", {
    const img_src = document.getElementById("image-field").src
    // custom aspect radio
    // e.g.
    aspectRatio: null,

    // min/max sizes
    maxSize: { width: null, height: null },
    minSize: { width: null, height: null },

    // start size of crop region
    startSize: { width: 100, height: 100, unit: '100%' },

    // real", "ratio" or "raw"
    returnMode: 'real',

    // callback functions
    onCropStart: function(data) {
      console.log(data.x, data.y, data.width, data.height);
    },
    onCropMove: function(data) {
      console.log(data.x, data.y, data.width, data.height);
    },
    onCropEnd: function(data) {
      console.log(data.x, data.y, data.width, data.height);
    },
    onInitialize: function(instance) {
      // do things here
      img_src.value =  croppr.getValue();
    }
    
});
}
*/