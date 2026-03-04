
// document.addEventListener("DOMContentLoaded",function(){
//     let coupe = document.querySelectorAll(".autoshow")
//     let item = new IntersectionObserver(entries => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting){
//                 entry.target.classList.add("show")
//             }
//             else{
//                 entry.target.classList.remove("show")
//             }
//         })
//     },{threshold: 0.4 })
//     // 40% visible
//     coupe.forEach(el => item.observe(el))
// })