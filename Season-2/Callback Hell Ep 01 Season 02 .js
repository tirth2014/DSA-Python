// Callback Hell Ep 01 Season 02 - Namaste JavaScript
// Learnings:

// 0. Importance of callbacks
// 1. Issues with callbacks:
        // 0. Callback Hell
        // 1. Inversion of Control

// JS synchronous single threaded language chhe but what if we need asynchronous behavior
//  for ex:

console.log("Namste");
// what if we need to make below code wait 5 sec. before executing
// then we'll use setTimeout() and we'll pass this inside a callback function
// So, basically asynchronysm in JS exists bcz of callbacks
console.log("I need break");   
console.log("JavaScript");

console.log("Namste");
setTimeout(function(){
    console.log("I need break");  
},5000) 
console.log("JavaScript");


//Issues with callbacks:
//  0. Callback hell:
// ex:

const cart = ["shoes","pant","earbuds","mouse","atta"]

// async api createOrder
api.createOrder(cart,function(){
    api.proceedToPayment(function(){
        api.showOrderSummary(
            function(){
                api.updateWallet()
            }
        )
    })
})
// this structure is known as a pyramid of doom

// 1. Inversion of Control

// upar createOrder function run thai jay pachhi j aapne proceedToPayment karvu chhe...so what we did is passed proceedToPayment as a callback function inside createOrder api
// And now it's responsibility of createOrder api to call the proceedToPayment function after execution of itself. ahiya aapne createOrder api par 100% TRUST mukyo chhe 
// But, createOrder no code game tene lakhyo hoi sake (for ex. some intern) ane ram jane ema proceedToPayment ne call karayu chhe ke nahi. ane call karayu hoy to pn somehow work na kare who knows!! so we can't be sure that it'll execute or not. ane what if createOrder api aapna proceedToPayment callback function ne 2-3 vaar execute karavi de to!!
// So, in short here we have given the control of proceedToPayment to createOrder api. which is very very Risky!.
