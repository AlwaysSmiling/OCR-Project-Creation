//import Cropper from "cropper.js";

var img = document.getElementById("editable");
var canvas = document.createElement('CANVAS');
var ctx = canvas.getContext("2d");
var imagedat = "";
var rotnum;


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

function PreviewImage(event) {
  var inj = event.target;
  var reader = new FileReader();

  reader.onload = function () {
    var dataURL = reader.result;
    img.src = dataURL;
  };
  reader.readAsDataURL(inj.files[0]);
}

function previewImageByURL(event) {
  img.src = document.getElementById("upurl").value;
}

function rotatenum() {
  rotnum = document.getElementById("rotnum").value;
}

img.onload = function () {
  canvas.height = img.naturalHeight;
  canvas.width = img.naturalWidth;
  ctx.drawImage(img, 0, 0);
  imagedat = canvas.toDataURL(img);


  if (img.naturalWidth > 750 || img.naturalheight > 750) {
    if (img.naturalWidth >= img.naturalHeight) {
      img.height = img.naturalWidth - img.naturalWidth / 2;
      img.width = img.naturalWidth - img.naturalWidth / 2;
    }
  } else if (img.naturalHeight < 500 || img.naturalWidth < 500) {
    if (img.naturalWidth < img.naturalHeight) {
      img.height = img.naturalHeight - img.naturalHeigth / 2;
      img.width = img.naturalHeight - img.naturalHeigth / 2;
    }
  }
  document.getElementById("editbox").style.display = "block";
  const cropper = new Cropper(editable, {
    scalabe: false,
    zoomable: false,
    autoCrop: false,
    background: false,
    ready() {
      document.getElementById("rotateL").addEventListener("click", function () {
        cropper.rotate(-90);
      });
      document.getElementById("rotateR").addEventListener("click", function () {
        cropper.rotate(90);
      });
      document
        .getElementById("rotateCus")
        .addEventListener("click", function () {
          cropper.rotate(rotnum);
        });
      document.getElementById("resize").addEventListener("click", function () {
        cropper.crop();
      });
      document
        .getElementById("editImage")
        .addEventListener("click", function () {
          cropdat = cropper.getData();
          cropper.clear();
        });
    },
  });
};

function showOCRops() {
  document.getElementById("step3").style.display = "block";
}

var l = document.getElementById("lan");
var t = document.getElementById("typ");

function showdownload() {
  document.getElementById("ocrrec").innerHTML = "Please Wait.....";
  
  var outputtype;
  
  var xhr1 = new XMLHttpRequest();
  xhr1.open("PUT", "OCR.py",true);
  xhr1.send(imagedat);
  
  var xhr2 = new XMLHttpRequest();
  xhr2.open("PUT", "OCR.py",true);
  xhr2.send(cropdat);
  
  var xhr3 = new XMLHttpRequest();
  switch (t.value) {
    case 1:
      switch (l.value) {
        case 1:
          break;
        case 2:
          break;
      }
      outputtype = "final_output.txt";
      break;
    case 2:
      switch (l.value) {
        case 1:
          break;
        case 2:
          break;
      }
      outputtype = "final.pdf";
      break;
    case 3:
      switch (l.value) {
        case 1:
          break;
        case 2:
          break;
      }
      outputtype = "final_doc.docx";
      break;
  }

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("download").style.display = "block";
    }
  };
  xhttp.open("GET", outputtype,true);
  xhttp.send();
  
}
