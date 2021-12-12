let prev_img = 0;

window.onload = function(){ //페이지 업로드 시 초기 상태
    document.getElementById("tempLoc_img1").src = "/static/img/tempLoc/tempLoc_s1.png"; //서울 선택
    prev_img = 1;
}

function change(sv){ //selectbox value 매개변수로 받음
    let selimgname = "tempLoc_img" + sv; 
    let previmgname = "tempLoc_img" + prev_img; 
    let selectimg = document.getElementById(selimgname); //현재 선택된 객체
    let previmg = document.getElementById(previmgname); //바로 전에 선택됐던 객체

    if(prev_img !== 0){ //이후에 다른 지역 고르면
        previmg.src = "/static/img/tempLoc/tempLoc_" + prev_img + ".png"; //이전에 선택됐던 객체 초기화
        selectimg.src = "/static/img/tempLoc/tempLoc_s" + sv + ".png"; //선택된 객체 소스 변경
        prev_img = sv;
        return;
    }
}
