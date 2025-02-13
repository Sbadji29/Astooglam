var phone_navbar = document.getElementById("mobile-nav");
var navbar_opener = document.getElementById("open-mobile");
var navbar_closer = document.getElementById("close-mobile");
navbar_opener.addEventListener("click",()=>{
    if(!phone_navbar.classList.contains("opened")){
        phone_navbar.style.left = "0";
        phone_navbar.classList.toggle("opened");
    }
});
navbar_closer.addEventListener("click",()=>{
    if(phone_navbar.classList.contains("opened")){
        phone_navbar.style.left = "-100%";
        phone_navbar.classList.toggle("opened");
    }
});