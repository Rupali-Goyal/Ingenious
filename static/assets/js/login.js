// for taking input
var form_fields=document.getElementsByTagName('input')

// adding class for css purpose
for(var field in form_fields){
    form_fields[field].className += 'form__input'
}

// initializing placeholder to classes
form_fields[1].placeholder='Username..';
form_fields[2].placeholder='Email..';
form_fields[3].placeholder='Enter password..';
form_fields[4].placeholder='Re-enter password..';


