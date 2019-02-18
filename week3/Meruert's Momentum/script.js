

var to_add = document.getElementById("add_button").onclick = function(){
    function inputLength() {
        return input.value.length;
    }
    
    function addListAfterKeypress(event) {
        if (inputLength() > 0 && event.keyCode === 13) {
            createListElement();
        }
    }
    var input = document.getElementById("userInput");
    var items = input.value;
    var ul = document.getElementById("list");
    var li = document.createElement("li");
    var lbl = document.createElement("span");
   
    
    lbl.innerHTML = items;
    var done=document.createElement("input");
    done.type = "checkbox";

    done.name = "completed";
    done.onchange = function(){
        var gv = document.getElementsByName("completed");
        for(var i = 0; i < gv.length;i++){
            var pnt = gv[i].parentElement;
            if(gv[i].checked){
                pnt.style.setProperty("text-decoration","line-through");
            }else{
                pnt.style.setProperty("text-decoration","none");
            }
        }
    };
    var todo = document.createElement("article");
    var my_form = document.createElement("form");
    var icon = document.createElement("img");
    icon.src = "trash.png";

    my_form.className = "trash_can";
    icon.style.width = "24px";

    icon.onclick = function(pass){
        var del = pass.currentTarget;
        var clear = del.parentElement
       
        clear.parentElement.remove();
    }
    


    input.addEventListener("keypress", addListAfterKeypress);
    my_form.appendChild(icon);

    li.appendChild(done);

    li.appendChild(lbl);

    li.appendChild(my_form);

    ul.appendChild(li);
    input.value ="";
};
function showTime(){
    var date = new Date();
    var h = date.getHours();
    var m = date.getMinutes();
    var session = "AM";
    var timeOfDay = (h < 12) ? session = "AM" : session = "PM";
    h = (h > 12) ? h-12 : h;
    h = (h==0) ? 12 : h;
    h = (h<10) ? "0"+ h : h;
    m = (m<10) ? "0"+ m : m;
   
    
    var time = h + ":" + m + " " + session;
    document.getElementById("clock").innerText = time;
    document.getElementById("clock").textContent = time;
    setTimeout(showTime, 1000);
}
showTime();
function changeImg(imgNumber)	{
    var myImages = ["images/1.jpg", "images/2.jpg", "images/3.jpg", "images/4.jpg",
    "images/5.jpg", "images/6.jpg", "images/7.jpg", "images/8.jpg","images/9.jpg"
,"images/10.jpg","images/11.jpg", "images/12.jpg", "images/13.jpg", "images/14.jpg", "images/15.jpg",
"images/16.jpg"]

    var imgShown = document.body.style.backgroundImage;
    var newImgNumber =Math.floor(Math.random()*myImages.length);
    document.body.style.backgroundImage = 'url('+myImages[newImgNumber]+')';
}
window.onload=changeImg;

var randomText = new Array ("The truth. It is a beautiful and terrible thing, and should therefore be treated with caution.", "It is our choices, Harry, that show what we truly are, far more than our abilities.",
"It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.", "It does not do to dwell on dreams and forget to live.", "One can never have enough socks.", 
"Numbing the pain for a while will make it worse when you finally feel it.", "It is a curious thing, Harry, but perhaps those who are best suited to power are those who have never sought it." );

var i = Math.random();
var arrayLength=randomText.length;
i=Math.floor(i*arrayLength);
document.getElementById("lblMessage").innerHTML = randomText[i];



