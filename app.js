let boxes = document.querySelectorAll(".box");
let resetBtn = document.querySelector("#reset-btn");
let newGameBtn = document.querySelector("#new-btn");
let msgContainer = document.querySelector(".msg-container");
let msg = document.querySelector("#msg");

let turnO = true;
const winPatterns = [
    [0, 1, 2], 
    [3, 4, 5], 
    [6, 7, 8], 
    [0, 3, 6], 
    [1, 4, 7], 
    [2, 5, 8],
    [0, 4, 8], 
    [2, 4, 6]  
];

const resetGame = () =>{
    turnO = true;
    enableBoxes();
    msgContainer.classList.add("hide");
}

boxes.forEach((box) => {
    box.addEventListener("click",()  => {
        if (turnO){
            box.innerText = "O";
            box.classList.add("O");
            turnO = false;
        }else{
            box.innerText = "X";
            box.classList.add("X");
            turnO = true;
        }
        box.disabled = true;
        checkWinner();

    })
});

const disablesBoxes = () =>{
    for (box of boxes){
        box.disabled = true;
    }
}
const enableBoxes = () => {
    for(box of boxes){
        box.disabled = false;
        box.innerText = "";
    }
}


const showWinner = (winner) => {
    msg.innerText = `Congratulations, Winner is ${winner}`;
    msgContainer.classList.remove("hide");
    disablesBoxes();

}
const checkWinner = () => {
    for(let pattern of winPatterns){

        let pos1Val = boxes[pattern[0]].innerText
        let pos2Val = boxes[pattern[1]].innerText
        let pos3Val = boxes[pattern[2]].innerText

        if (pos1Val != "" && pos2Val != "" && pos3Val != ""){
            if(pos1Val === pos2Val && pos2Val === pos3Val){
                console.log("winner!", pos1Val);
                showWinner(pos1Val);
            }
        }
      
    }
    checkDraw();
}
const checkDraw = () => {
    let isDraw = true;
    boxes.forEach((box) => {
        if(box.innerText == ""){
            isDraw = false;
        }
    })
    if (isDraw){
        msg.innerText = "It's a DRAW!";
        msgContainer.classList.remove("hide");
    }
}
newGameBtn.addEventListener("click", resetGame);
resetBtn.addEventListener("click", resetGame);