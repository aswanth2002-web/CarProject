let nextbut = document.getElementById('next')
let revbut =document.getElementById('rev')
let carouselbut = document.querySelector('.main-carousel')
let listitembut = document.querySelector('.main-carousel .list')
let thumbnailbut = document.querySelector('.main-carousel .thumbnail')

nextbut.onclick = function(){
    showslider('next')
}
revbut.onclick = function(){
    showslider('rev')

}
let timerunning = 3000;
let runtimeout;
function showslider(type){
    let itemslider = document.querySelectorAll('.main-carousel .list .item')
    let itemthumbnail = document.querySelectorAll('.main-carousel .thumbnail .item')
    if(type === 'next'){
        listitembut.appendChild(itemslider[0])
        thumbnailbut.appendChild(itemthumbnail[0])
        carouselbut.classList.add('next')
    }else{
        let positionlastitem = itemslider.length - 1
        listitembut.prepend(itemslider[positionlastitem])
        thumbnailbut.prepend(itemthumbnail[positionlastitem])
        carouselbut.classList.add('rev')
    }
    clearTimeout(runtimeout);
    runtimeout = setTimeout(() => {
        carouselbut.classList.add('next')
        carouselbut.classList.add('rev')
    },timerunning)
}