function validation(){
    var name = document.myform.name
    var email = document.myform.email
    var mailformat = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    var mobile_number = document.myform.mobile_number
    var address = document.myform.address
    // var logo = document.myform.logo
    // var license = document.myform.license
    var password = document.myform.password
    var confirmpassword =document.myform.confirmpassword
    var letter = /[a-z]/;
    var upper = /[A-Z]/;
    var number = /[0-9]/;


    if (name.value=='' || name.value.length <4){
        alert(" Parlour name should be more than 4 alphabets" )
        return false;
    }
    if (!email.value.match(mailformat)){
        alert("invalid email")
        email.focus();
        return false;
       } 
    if (mobile_number.value=='' || mobile_number.value.length !=10 ){
        alert("Mobile number should be 10 digits")
        mobile_number.focus();
        return false;
    }
    if (address.value==''){
        alert("address should not be emty")
        address.focus();
        return false;
    }
    // if (logo.value==''){
    //     alert("logo should not be emty")
    //     logo.focus();
    //     return false;
    //    }
    // if (license.value==''){
    //     alert("license should not be emty")
    //     license.focus();
    //     return false;
    //    }
    if (password.value==''){
        alert("password should not be emty")
        password.focus();
        return false;
       }
    if (confirmpassword.value==''){
        alert("confirmpassword should not be emty")
        confirmpassword.focus();
        return false;
       }
    if (!letter.test(password.value)){
        alert(" Please  make sure password Includes a lowercase letter ")
        return false;
       }
    if (!upper.test(password.value)){
        alert(" Please  make sure password Includes a uppercasw letter ")
        return false;
       }
    if (!number.test(password.value)){
        alert("Please  make sure pass")
        return false;
       }
    else{
       return true;
    }
}