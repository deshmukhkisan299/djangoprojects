function display_data(){
var myform = document.getElementById('formdiv');
var mydata = document.getElementById('datadiv');
var sfbtn = document.getElementById('sfbtn');
if (sfbtn.style.display == 'none'){
myform.style.display ='none'
mydata.style.display='block'
sfbtn.style.display='block'
}else{
myform.style.display ='block'
mydata.style.display='none'
sfbtn.style.display='none'
}}
function editinfo(){
}