document.addEventListener('keydown', (event) => {
  // var name = event.key;
  let code = event.code;

  if (code==="KeyP")
    presentationMode();
}, false);

function showImage(index, previous){
    document.getElementById('img_pres_'+previous).style.display = 'none';
    document.getElementById('img_pres_'+index).style.display = 'block';
}

let p_mode_off = document.getElementById('presentation-mode-off');
let p_mode = document.getElementById('presentation-mode');

let presentationModeFlag = false;
let img_counter = 1;

let timer;
function presentationMode(){
    if (!presentationModeFlag){
        console.log("ON");
        p_mode_off.style.display = 'none';
        p_mode.style.display = 'flex';
        timer = setInterval(function(){
            prev = img_counter - 1 > 0 ? img_counter - 1 : images_count;
            showImage(img_counter, prev)
            img_counter += 1;
            if (img_counter > images_count)
                img_counter = 1;
     }, 1000);
    }else{
        console.log("OFF");
        p_mode_off.style.display = 'block';
        p_mode.style.display = 'none';
        if (timer) clearInterval(timer)
    }
    presentationModeFlag = !presentationModeFlag;
}
