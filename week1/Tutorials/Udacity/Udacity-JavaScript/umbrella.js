/*
 * Programming Quiz: Umbrella (7-1)
 */

var umbrella = {
    color: "pink",
    isOpen: true,
    open: function() {
        if (umbrella.isOpen === true) {
            return "The umbrella is already opened!";
        } else {
            umbrella.isOpen = true;
            return "Julia opens the umbrella!";
        }
    },
    isClose:true,
    close: function(){
        if(umbrella.isClosed === true){
            return "The umbrealls is already closed!";
        }else{
            umbrella.isClose = true;
            umbrella.isOpen = false;
            return "Julia closes the umbrella!";
        }
    },
};
console.log(umbrella);