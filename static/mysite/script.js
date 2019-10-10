let deleteButtons = document.getElementsByClassName("deleteButton");
document.onclick = function(e){
    e = e || event;
    e = e.target;
    if (e.className != "deleteButton")
    return;
    if (!confirm("Delete this")){
    return false
    }
    }


