function myFunction(){
    var copyText = document.getElementById("myInput");
    copyText.select();
    copyText.setSelectionRange(0, 99999)
    document("copy");
    alert("Copied the link: " + copyText.value);
  }