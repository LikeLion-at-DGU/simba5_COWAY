let reset_floor = 1;

function choiceB(floor){
    let floor_arr = [];
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

    if(reset_floor === floor){
        reset_floor = 0;
    }else{
        for(let i=0;i<=11;i++){
            floor_arr[i].style.display = "none";
        }
    }

    if(floor === 11){
        floor_arr[10].style.display = "table-cell";
    }else if(floor === 22){
        floor_arr[11].style.display = "table-cell";
    }else if(floor <= 10){
        for(let i=0;i<=floor-1;i++){
            floor_arr[i].style.display = "table-cell";
        }
    }
    reset_floor = floor;
}

// let colorChange = document.querySelector('.a');

// function selected(){
//     colorChange.style.backgroundColor = "#C2BDB4";
// }

// colorChange.addEventListener('click',selected);