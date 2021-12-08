let prev_img = 0;

window.onload = function(){
    document.getElementById("tempLoc_img1").src = "/static/img/tempLoc/tempLoc_s1.png";
    prev_img = 1;
}

function change(sv){
    let selimgname = "tempLoc_img" + sv;
    let previmgname = "tempLoc_img" + prev_img;
    let selectimg = document.getElementById(selimgname);
    let previmg = document.getElementById(previmgname);
    console.log("sv: " + sv);
    console.log("sel_img: " + selimgname);
    console.log("prev_img1: " + prev_img);
    if(prev_img === 0){ //초기상태에서 value값 변하면
        selectimg.src = "/static/img/tempLoc/tempLoc_s" + sv + ".png";
        prev_img = sv;
        console.log("prev_img2: " + prev_img);
        return;
    }
    if(prev_img !== 0){ //이후에 다른 지역 고르면
        previmg.src = "/static/img/tempLoc/tempLoc_" + prev_img + ".png";
        selectimg.src = "/static/img/tempLoc/tempLoc_s" + sv + ".png";
        prev_img = sv;
        console.log("prev_img3: " + prev_img);
        return;
    }
}
