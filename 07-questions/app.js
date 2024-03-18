const btns = document.querySelectorAll('.question-btn');

btns.forEach(function(){
    btn.addEventListener('click', function(e){
        console.log(e.currentTarget);
    })
})