
var updateButtons = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateButtons.length; i++){

    updateButtons[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        if(user === 'AnonymousUser'){
            addCookieItem(productId, action)
        }
        else {
           updateUserOrder(productId, action)
        }
    })
}
// a function to handle a guest users' activities on the site
function addCookieItem(productId, action){
    console.log('Not logged in...')
    if(action == 'add'){
        if(cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }else{
           cart[productId]['quantity'] += 1
           if(cart[productId]['quantity'] <= 0){
               delete cart[productId]
           } 
        }
    }
    if(action == 'remove'){
        cart[productId]['quantity'] -= 1
    }
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain;path=/"
    location.reload()
}
// A function to handle a logged in user's activities
function updateUserOrder(productId, action){
    console.log('User is logged, sending date...') // this is for testing. wll be removed later
    var url = 'update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'content-Type': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })


}