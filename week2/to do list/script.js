
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
    var lbl = document.createElement("label");

    
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
    var my_form = document.createElement("form");
    var icon = document.createElement("img");
    icon.src = "trash_can.png";

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
