
function deskName() {
    var namevalidation = /^(\w+\.?)*\w+$/;
    var fName = document.getElementsByName("fileName")[0].value;
    var error =0;
    if (fName == "") {
        document.getElementById("desk_name_error").innerHTML =
        "This field cannot be left empty";
        document.getElementsByClassName("file_name")[0].classList.add("is-invalid");
        error = error + 1;
    }
    else if (namevalidation.test(fName) == false) {
        document.getElementById("desk_name_error").innerHTML =
        "Please enter name in proper format";
        document.getElementsByClassName("file_name")[0].classList.add("is-invalid");
        error = error + 1;
    }
    else {
        document.getElementsByClassName("file_name")[0].classList.remove("is-invalid");
        error=0;
    }
    if (error != 0) {
        return false;
    }
    console.log(error);
}
function WSdeskName() {
    var namevalidation = /^(\w+\.?)*\w+$/;
    var fName = document.getElementsByName("fileName")[1].value;
    var error =0;
    if (fName == "") {
        document.getElementById("WSdesk_name_error").innerHTML =
        "This field cannot be left empty";
        document.getElementsByClassName("file_name")[1].classList.add("is-invalid");
        error = error + 1;
    }
    else if (namevalidation.test(fName) == false) {
        document.getElementById("WSdesk_name_error").innerHTML =
        "Please enter name in proper format";
        document.getElementsByClassName("file_name")[1].classList.add("is-invalid");
        error = error + 1;
    }
    else {
        document.getElementsByClassName("file_name")[2].classList.remove("is-invalid");
        error=0;
    }
    if (error != 0) {
        return false;
    }
    console.log(error);
}


function WSfileName() {
    var namevalidation = /^(\w+\.?)*\w+$/;
    var fName = document.getElementsByName("fileName")[2].value;
    var error =0;
    if (fName == "") {
        document.getElementById("file_name_error").innerHTML =
        "This field cannot be left empty";
        document.getElementsByClassName("file_name")[2].classList.add("is-invalid");
        error = error + 1;
    }
    else if (namevalidation.test(fName) == false) {
        document.getElementById("file_name_error").innerHTML =
        "Please enter name in proper format";
        document.getElementsByClassName("file_name")[2].classList.add("is-invalid");
        error = error + 1;
    }
    else {
        document.getElementsByClassName("file_name")[2].classList.remove("is-invalid");
        error=0;
    }
    if (error != 0) {
        return false;
    }
    console.log(error);
}

function fileName() {
    var namevalidation = /^(\w+\.?)*\w+$/;
    var fName = document.getElementsByName("fileName")[3].value;
    var error =0;
    if (fName == "") {
        document.getElementById("file_name_error").innerHTML =
            "This field cannot be left empty";
        document.getElementsByClassName("file_name")[3].classList.add("is-invalid");
        error = error + 1;
    }
    else if (namevalidation.test(fName) == false) {
        document.getElementById("file_name_error").innerHTML =
            "Please enter name in proper format";
        document.getElementsByClassName("file_name")[3].classList.add("is-invalid");
        error = error + 1;
    }
    else {
        document.getElementsByClassName("file_name")[3].classList.remove("is-invalid");
        error=0;
    }
    if (error != 0) {
        return false;
    }
    console.log(error);
}