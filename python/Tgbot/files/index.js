xCoord = 0

function f(event) {


    if (event.code == "ArrowRight") {
        xCoord += 10
    }
    if (event.code == "ArrowLeft") {
        xCoord -= 10
    }
    elem = document.getElementById('number')

    elem.innerHTML = parseInt(elem.innerHTML) + 1

    elem.style.position = 'relative'
    elem.style.left = xCoord + 'px'


    console.log(elem.innerHTML)
}

document.addEventListener('keydown', f)