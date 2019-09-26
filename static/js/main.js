const header = document.querySelector('#header');
const sidebox = document.querySelector('.sidebox');
const categorybox = document.querySelector('.categorybox')


function scrollFunc(){
    // 스크롤의 정도를 볼수있다
    if(pageYOffset >=10){
        header.classList.add('on');
        sidebox.classList.add('on');
    }else{
        header.classList.remove('on');
        sidebox.classList.remove('on');
    }
}

window.addEventListener('scroll', scrollFunc);