const child = document.querySelectorAll('.child')
const canceller = document.querySelectorAll('.flexer i')
const checkr = document.querySelectorAll('input[type=checkbox]')
function cleicker (){
    for (let i = 0; i < child.length; i++) {
        const element = child[i];
        element.addEventListener('click', function(event){
        const clickednode = Array.prototype.indexOf.call(child, event.target)
        if(child[clickednode].classList.contains('checked') == false){
            child[clickednode].classList.toggle('checked')
            canceller[clickednode].classList.toggle('bxs-x-circle')
            canceller[clickednode].classList.toggle('bxs-check-circle')
            checkr[clickednode].checked=true
            checkr[clickednode].value='on'
        }
        else{
        child[clickednode].classList.toggle('checked')
        canceller[clickednode].classList.toggle('bxs-x-circle')
        canceller[clickednode].classList.toggle('bxs-check-circle')
        checkr[clickednode].checked=false
        checkr[clickednode].value='off'
        }
        })
    }
}
cleicker()
