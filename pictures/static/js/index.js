    let foot = document.getElementsByClassName("grid-foot")[0];
    let left = document.getElementById("scroll-left-button");
    let right = document.getElementById("scroll-right-button");
    let timer;
    left.addEventListener('mousedown', function () {
        timer = setInterval(function(){
          foot.scrollLeft -= 2;
     }, 10);
    })
    right.addEventListener('mousedown', function () {
        timer = setInterval(function(){
          foot.scrollLeft += 2;
     }, 10);

    })
    document.addEventListener("mouseup", function(){
        if (timer) clearInterval(timer)
    });

    function checkPosition(){
        console.log("XD");
        console.log(foot.scrollLeft);
        if (foot.scrollLeft === 0) {
            right.style.display = 'none';
        } else if (foot.scrollLeft === -(foot.scrollWidth - foot.offsetWidth)) {
            left.style.display = 'none';
        }else {
            left.style.display = 'flex';
            right.style.display = 'flex';
        }
    }
    document.getElementsByClassName('grid-foot')[0].addEventListener('scroll', checkPosition);


    let pres_mode = false;
    function presentation(){
        if (!pres_mode){
            //pres mode ON
            document.getElementsByClassName('grid-foot')[0].style.display = 'none';
            document.getElementsByClassName('grid-body')[0].style.height = '90vh';
            document.getElementsByClassName('grid-container')[0].classList.add('grid-container-pres');
            document.getElementsByClassName('grid-container')[0].classList.remove('grid-container');
        }else{
            //pres mode OFF
            document.getElementsByClassName('grid-foot')[0].style.display = 'block';
            document.getElementsByClassName('grid-body')[0].style.height = '70vh';
            document.getElementsByClassName('grid-container-pres')[0].classList.add('grid-container');
            document.getElementsByClassName('grid-container-pres')[0].classList.remove('grid-container-pres');
        }
        pres_mode = !pres_mode;
    }

    document.getElementById('presentation_button').addEventListener('click', presentation)