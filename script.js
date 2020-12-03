

var img = document.getElementById("editable");
var canvas = document.createElement("CANVAS");
var ctx = canvas.getContext("2d");
var imagedat = "";
var rotnum;


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
  imagedat = canvas.toDataURL();

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
var outputtype;
var langtype;

t.addEventListener("change", function() {
  if (t.value == 1){ outputtype = "final_output.txt";}
  else if(t.value == 2){ outputtype = "final.pdf";}
  else if(t.value == 3){ outputtype = "final_doc.docx";}
} );

l.addEventListener("change", function() {
  if (l.value == 1){ langtype = "eng";}
  else if(l.value == 2){ langtype = "hin";}
} );

function showdownload() {
  document.getElementById("ocrrec").innerHTML = "Please Wait.....";

  fetch("OCR.py " + langtype + " " + outputtype, {
    method: "POST",
    body: imagedat + " " + JSON.stringify(cropdat),
    headers: {
      "Content-Type": "text/plain"
    },
    credentials: "same-origin"
  }).then(function(response) {
    console.log(response.status)     
    console.log(response.statusText) 
    console.log(response.headers)    
    console.log(response.text())       
  }).then(function() {
    fetch(outputtype)
    .then(function(response) {
      console.log(response.status)     
      console.log(response.statusText) 
      console.log(response.headers)    
      console.log(response.url)        
      showdwnldbutton(response.url)
    })
  })
}

function showdwnldbutton(param){
  document.getElementById("ocrrec").style.display = "none";
  document.getElementById("download").style.display = "block";
  document.getElementById("downloadbttn").href = param;
}


function read1() {
  var readMoreText = document.getElementById("readmore1");
  var readMoreButton = document.getElementById("read1Button");

  if (readMoreText.style.display === "none") {
    readMoreText.style.display = "block";
    readMoreButton.innerHTML = "Read less";
  } else {
    readMoreText.style.display = "none";
    readMoreButton.innerHTML = "Read More";
  }
}

function read2() {
  var readMoreText = document.getElementById("readmore2");
  var readMoreButton = document.getElementById("read2Button");

  if (readMoreText.style.display == "none") {
    readMoreText.style.display = "block";
    readMoreButton.innerHTML = "Read less";
  } else {
    readMoreText.style.display = "none";
    readMoreButton.innerHTML = "Read More";
  }
}

function read3() {
  var readMoreText = document.getElementById("readmore3");
  var readMoreButton = document.getElementById("read3Button");

  if (readMoreText.style.display == "none") {
    readMoreText.style.display = "block";
    readMoreButton.innerHTML = "Read less";
  } else {
    readMoreText.style.display = "none";
    readMoreButton.innerHTML = "Read More";
  }
}

function read4() {
  var readMoreText = document.getElementById("readmore4");
  var readMoreButton = document.getElementById("read4Button");

  if (readMoreText.style.display == "none") {
    readMoreText.style.display = "block";
    readMoreButton.innerHTML = "Read less";
  } else {
    readMoreText.style.display = "none";
    readMoreButton.innerHTML = "Read More";
  }
}
