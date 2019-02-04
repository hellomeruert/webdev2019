/*
 * Programming Quiz: Facebook Friends (7-5)
 */

// your code goes here
var facebookProfile = {
    name:"Meruert Amamabayeva",
    friends: 33,
    messages:["In Almaty!", "In Kostanay!", "In New York!"],
    postMessage(message){
        facebookProfile.messages.push(message);
    },
    deleteMessage(index){
        facebookProfile.messages.splice(index, 1);
    },
    addFriend(){
        facebookProfile.friends+=1;
    },
    removeFriend(){
        facebookProfile.friends = facebookProfile.friends - 1;
    },
};
 facebookProfile.removeFriend();
 facebookProfile.friends;
 console.log(facebookProfile);