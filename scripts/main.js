let myImage = document.querySelector('img');

myImage.onclick = function() {
    let mySrc = myImage.getAttribute('src');
    if(mySrc === 'images/ebube3.jpg') {
      myImage.setAttribute('src', 'images/ebube2.jpg');
    } else {
      myImage.setAttribute('src', 'images/ebube3.jpg');
    }
}
 
