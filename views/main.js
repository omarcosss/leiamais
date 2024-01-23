searchForm = document.querySelector('.form-busca');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
}

let loginForm = document.querySelector('.login-form-container');

document.querySelector('#login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}

document.querySelector('#close-login-btn').onclick = () => {
    loginForm.classList.toggle('active');
}


window.onscroll = () =>{
    if(window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

window.onload = () =>{
    if(window.scrollY > 80) {
        document.querySelector('.header .header-2').classList.add('active');
    }else{
        document.querySelector('.header .header-2').classList.remove('active');
    }
}

var swiper = new Swiper(".books-slider", {
    slidesPerView: 3,
    spaceBetween:150,
    centeredSlides:false,
    breakpoints: {
        0: {
          slidesPerView: 1,
        },
        768: {
          slidesPerView: 2,
        },
        1024: {
          slidesPerView: 3,
        },
      },
});

var swiper = new Swiper(".slider-destaques", {
    spaceBetween:20,
    centeredSlides:false,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
            centeredSlides: true,
        },
        768: {
            slidesPerView: 2,
            centeredSlides:false,
        },
        1024: {
            slidesPerView: 4,
            centeredSlides:false,
        },
    },
});

var swiper = new Swiper(".slider-novidades", {
    spaceBetween:10,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    breakpoints: {
        0: {
            slidesPerView: 1,
            centeredSlides: true,
        },
        768: {
            slidesPerView: 2,
            centeredSlides:false,
        },
        1024: {
            slidesPerView: 4,
            centeredSlides:false,
        },
    },
});
