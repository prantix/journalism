slideIndex = 0;
carousel();

function carousel() {
    let i;
    let images = document.getElementsByClassName("myslides");
    for(i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }
    slideIndex++;
    if(slideIndex > images.length) {slideIndex=1;}
    images[slideIndex-1].style.display = "block";
    setTimeout(carousel, 4000);
}


contact_textarea = document.querySelector("#contact form textarea");
contact_textarea.setAttribute("placeholder", "Leave a message...");
