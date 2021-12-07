const slides = document.querySelector('.slides'); //전체 슬라이드 컨테이너
const slideImg = document.querySelectorAll('.slides img'); //모든 슬라이드들
let currentIdx = 0; //현재 슬라이드 index
const slideCount = slideImg.length;
const prev = document.querySelector('.prev') // 이전 버튼
const next = document.querySelector('.next'); // 다음 버튼
const slideWidth = 300; // 슬라이드 하나의 넓이
const slideMargin = 100; // 슬라이드 간 margin 값

// 전체 슬라이드 컨테이너 넓이 설정
slides.style.width = (slideWidth + slideMargin) * slideCount + 'px';

function moveSlide(num) {
    slides.style.left = -num * 200 + 'px';
    currentIdx = num;
}

prev.addEventListener('click', function() {
    // 첫 번째 슬라이드로 표시됐을 때는 이전 버틑 눌러도 아무 반응 안나오도록 currentIdx != 0일 때만 moveSlide 함수 불러옴
    if(currentIdx !==0) moveSlide(currentIdx - 1);
});

next.addEventListener('click', function() {
    if(currentIdx !== slideCount / 2 - 1){
        moveSlide(currentIdx + 1);
    }
});