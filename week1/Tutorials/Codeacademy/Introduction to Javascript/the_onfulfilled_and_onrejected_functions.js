const {checkInventory} = require('./library.js');

const order = [['sunglasses', 1], ['bags', 2]];

// Write your code below:
const handleSuccess = (resolvedValue) => {
    console.log(resolvedValue);
};

const handleFailure = (rejectReason) => {
    console.log(rejectReason);
};

checkInventory(order)
    .then(handleSuccess, handleFailure);



