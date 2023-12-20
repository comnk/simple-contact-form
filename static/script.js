let submit = document.getElementById("submit");

function validate() {
    let msg = document.getElementById("msg");

    if (msg.value == "") {
        alert("Text Content is Empty!");
        return false;
    }
}

submit.addEventListener("click", validate);