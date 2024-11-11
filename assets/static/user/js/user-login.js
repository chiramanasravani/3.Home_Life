function validation(){
    var email = document.myform.email
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var password = document.myform.password
  

    if (!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
       } 
   
    if (password.value==''){
        alert("password should not be emty")
        password.focus();
        return false;
       }
   
    else{
       return true;
    }
}