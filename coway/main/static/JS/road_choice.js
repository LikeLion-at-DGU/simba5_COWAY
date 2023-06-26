// road_choice.js
let reset_floor = 1;
let start_spot=['',''];
let end_spot=['',''];

let startBuildingInput = document.getElementById("startBuildingInput");
let startFloorInput = document.getElementById("startFloorInput");
let endBuildingInput = document.getElementById("endBuildingInput");
let endFloorInput = document.getElementById("endFloorInput");

const bName = document.getElementsByClassName('bName');
const fName = document.getElementsByClassName('fName');

const floor_arr = [];
floor_arr[0] = document.querySelector('.choiceF_1');
floor_arr[1] = document.querySelector('.choiceF_2');
floor_arr[2] = document.querySelector('.choiceF_3');
floor_arr[3] = document.querySelector('.choiceF_4');
floor_arr[4] = document.querySelector('.choiceF_5');
floor_arr[5] = document.querySelector('.choiceF_6');
floor_arr[6] = document.querySelector('.choiceF_7');
floor_arr[7] = document.querySelector('.choiceF_8');
floor_arr[8] = document.querySelector('.choiceF_9');
floor_arr[9] = document.querySelector('.choiceF_10');
floor_arr[10] = document.querySelector('.choiceF_6m');
floor_arr[11] = document.querySelector('.choiceF_1m');
floor_arr[12] = document.querySelector('.choiceF_b1');
floor_arr[13] = document.querySelector('.choiceF_b2');
floor_arr[14] = document.querySelector('.choiceF_b3');

function choiceB(event,floor){
    for(let i=0;i<bName.length;i++){//건물 선택 초기화
        bName[i].style.backgroundColor = '#ffffff';
    }
    for(let i=0;i<fName.length;i++){//층수 선택 초기화
        fName[i].style.backgroundColor = '#ffffff';
    }
    if(start_spot[0]!=='' && start_spot[1]===''){
        start_spot[0]='';
    }else if(end_spot[0]!==''){
        end_spot[0]='';
    }

    let target = event.target;//선택된 건물 

    if(start_spot[0]===''||(start_spot[1]=='' && end_spot[0]=='')){//출발지
        target.style.backgroundColor='#C2BDB4';
        start_spot[0]=target.textContent;
        startBuildingInput.value=start_spot[0];
        startBuildingInput.style.color = '#FEA218';
    }else{//도착지
        target.style.backgroundColor='#C2BDB4';
        end_spot[0]=target.textContent;
        endBuildingInput.value=end_spot[0];
        endBuildingInput.style.color = '#FEA218';
    }

    if(reset_floor === floor){
        reset_floor = 0;
    }else{
        for(let i=0;i<floor_arr.length;i++){
            floor_arr[i].style.display = "none";
        }
    }

    if(floor === 11){
        floor_arr[10].style.display = "table-cell";
    }else if(floor === 22){
        floor_arr[11].style.display = "table-cell";
    }else if(floor === 12){//지하1층 ~ 4층
        for(let i=0;i<4;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";
    }else if(floor === 13){//지하2층 ~ 4층
        for(let i=0;i<4;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";floor_arr[13].style.display = "table-cell";
    }else if(floor === 14){//지하1층 ~ 6층
        for(let i=0;i<6;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";
    }else if(floor === 15){//지하2층 ~ 6층
        for(let i=0;i<6;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";floor_arr[13].style.display = "table-cell";
    }else if(floor === 16){//지하3층 ~ 4층
        for(let i=0;i<4;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";floor_arr[13].style.display = "table-cell";floor_arr[14].style.display = "table-cell";
    }else if(floor === 17){//지하1층 ~ 5층
        for(let i=0;i<5;i++){
            floor_arr[i].style.display = "table-cell";
        }floor_arr[12].style.display = "table-cell";
    }else if(floor <= 10){
        for(let i=0;i<=floor-1;i++){
            floor_arr[i].style.display = "table-cell";
        }
    }
    reset_floor = floor;
}

function choiceF(event){
    for(let i=0;i<fName.length;i++){//층수 선택 초기화
        fName[i].style.backgroundColor = '#ffffff';
    }
    if(start_spot[0]==''){
        start_spot[1]='';
    }else if(end_spot[0]==''){
        end_spot[1]='';
    }

    let target = event.target;
    
    if(end_spot[0]!==''){//도착지 층수 입력
        target.style.backgroundColor='#C2BDB4';
        end_spot[1]=target.textContent;
        endFloorInput.value = end_spot[1];
    }else{//출발지 층수 입력
        target.style.backgroundColor='#C2BDB4';
        start_spot[1]=target.textContent;
        startFloorInput.value = start_spot[1];
    }
}

document.querySelector('.start_b').addEventListener('click',function(){
    start_spot[0]='';
    start_spot[1]='';
    startBuildingInput.value = null;
    startFloorInput.value = null;
    for(let i=0;i<bName.length;i++){//건물 선택 초기화
        bName[i].style.backgroundColor = '#ffffff';
    }
    for(let i=0;i<fName.length;i++){//층수 선택 초기화
        fName[i].style.backgroundColor = '#ffffff';
    }
})
document.querySelector('.end_b').addEventListener('click',function(){
    end_spot[0]='';
    end_spot[1]='';
    endBuildingInput.value = null;
    endFloorInput.value = null;
    for(let i=0;i<bName.length;i++){//건물 선택 초기화
        bName[i].style.backgroundColor = '#ffffff';
    }
    for(let i=0;i<fName.length;i++){//층수 선택 초기화
        fName[i].style.backgroundColor = '#ffffff';
    }
})

