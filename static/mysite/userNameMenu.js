let userName = document.getElementById("userName");
let userNameMenu = document.getElementById("userNameMenu");

userName.onclick = function(e) {
	e.preventDefault();
	e = e||event;
	e = e.target;
	let coords = userName.getBoundingClientRect()
	userNameMenu.style.left = coords.left + "px";
	userNameMenu.style.top = userName.clientHeight + "px";
	userNameMenu.style.width = userName.clientWidth + "px";
	console.log(userNameMenu.style.visibility);
	if ( userNameMenu.style.visibility =="hidden") {
		userNameMenu.style.visibility = "visible";
	}
	else{
	 userNameMenu.style.visibility = "hidden";}

  };
