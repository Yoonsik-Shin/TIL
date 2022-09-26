const container = document.querySelector("#container");
const button = document.querySelector("#btn");
const resetButton = document.querySelector("#reset");

button.addEventListener("click", () => {
    const lottoNums = _.sampleSize(_.range(1, 46), 7); // 로또번호
    const numberContainer = document.createElement("div");
    numberContainer.classList.add("flex");
    container.append(numberContainer);

    for (lottoNum of lottoNums) {
        const number = document.createElement("div");
        switch (parseInt((lottoNum - 1) / 10)) {
            case 0:
                number.classList.add("yellow");
                break;
            case 1:
                number.classList.add("blue");
                break;
            case 2:
                number.classList.add("red");
                break;
            case 3:
                number.classList.add("grey");
                break;
            case 4:
                number.classList.add("green");
                break;
        }
        number.classList.add("ball");
        number.innerText = lottoNum;
        numberContainer.append(number);
    }
});

resetButton.addEventListener("click", () => {
    const balls = document.querySelectorAll(".ball");
    for (ball of balls) {
        ball.remove();
    }
});
