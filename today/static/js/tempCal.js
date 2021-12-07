//--------------------------달력 생성-------------------------------
let date = new Date();
const renderCal = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

//n년 n월
    document.querySelector('.tempCal_yearmonth').textContent = `${viewYear}. ${viewMonth + 1}`;

//지난달 마지막 날, 이번달 마지막 날
    const prevLast = new Date(viewYear, viewMonth, 0); //이번달 0 = 저번달 마지막날
    const thisLast = new Date(viewYear, viewMonth + 1, 0); //다음달 0,1 = 이번달 마지막날
    const PLDate = prevLast.getDate(); //지난달 마지막 날짜
    const PLDay = prevLast.getDay(); //지난달 마지막 요일
    const TLDate = thisLast.getDate(); //이번달 마지막 날짜
    const TLDay = thisLast.getDay(); //이번달 마지막 요일

//dates 배열
    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1); 
// 처음에 빈배열이라 array iterator 생성(0~n-1) -> n=TLDate+1 전해주면 0~TLDate -> slice로 0 삭제 = 1~TLDate
    const nextDates = [];

//prevDates
    if (PLDay !== 6) { //이전달 마지막 요일이 토요일이 아니면
        for (let i = 0; i < PLDay + 1; i++) {
        prevDates.unshift(PLDate - i); //이전달 뒤쪽 날짜 넣기
        }
    }

//nextDates
    for (let i = 1; i < 7 - TLDay; i++) { //다음달 앞쪽 날짜 넣기
        nextDates.push(i);
    }

//dates = prev + +this + next, 이전달 마지막 & 다음달 앞부분 투명하게, 12월 제외 모두 투명
    const dates = prevDates.concat(thisDates, nextDates); //prevDates + thisDates + nextDates
    const firstDate = dates.indexOf(1);
    const lastDate = dates.indexOf(TLDate);
    dates.forEach((date, i) => {
        const condition = i >= firstDate && i < lastDate + 1 && viewMonth+1 === 12
                        ? 'this'
                        : 'other';
        dates[i] = `<div class="tempCal_date"><span class="${condition}">${date}</span></div>`; //html로 변환
        if(5 < date && date < 14){ //6~13일만 선택하도록 노란박스
            dates[i] = `<div class="tempCal_date2" onclick="changered(this)">${date}</div>`;
        }
    })
    document.querySelector('.tempCal_dates').innerHTML = dates.join(''); 
}
renderCal();

//--------------------------버튼 이동-------------------------------
const prevMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() - 1);
    renderCal();
  }
  
  const nextMonth = () => {
    date.setDate(1);
    date.setMonth(date.getMonth() + 1);
    renderCal();
  }
  
  const goToday = () => {
    date = new Date();
    renderCal();
  }

//---------------------------날짜 선택-----------------------------
let prev_date = "";
let next_date = "";
let clicktime = 0;

function changered(seldate){
    if(clicktime === 0){ // 한번도 클릭안했으면
        seldate.classList.add("sel"); //클릭한 날짜 색바꾸고
        clicktime = 1; //클릭횟수 증가
        prev_date = seldate.textContent; //prev_date = 현재 날짜
        console.log("prev_date1: " + prev_date);
        return;
    }
    if(clicktime !== 0){ //한번이라도 클릭했으면
        if(prev_date === seldate.textContent){ //같은 날짜 고르면
            seldate.classList.remove("sel"); //색 원래대로
            prev_date = seldate.textContent;
            console.log("prev_date2: " + prev_date);
            return;
        }
        if(prev_date !== seldate.textContent){ //다른 날짜 고르면
            let date2 = document.getElementsByClassName("tempCal_date2");
            for(let i=0; i< date2.length; i++){
                date2[i].classList.remove("sel"); //전체색 원래대로
            }
            seldate.classList.add("sel"); //해당 날짜만 색 바꿈
            prev_date = seldate.textContent;
            console.log("prev_date3: " + prev_date);
            return;
        }
    }
    
}