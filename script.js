function openCity(cityName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(cityName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


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

function selectedFile(event){
  var typeOfFile = document.getElementById(event.target.id)
  var selectfile = document.getElementById("selectfile")
  var temp = selectfile.innerHTML
  selectfile.innerHTML = typeOfFile.innerHTML
  typeOfFile.innerHTML = temp
  var x = document.getElementById("drpdwn");
  x.className = x.className.replace(" w3-show", "");
}