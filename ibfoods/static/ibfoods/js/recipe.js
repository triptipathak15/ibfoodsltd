$(function() {
    $('.table').DataTable();
    var nav = document.getElementById('sidebar_ul')
    var anchor = nav.getElementsByTagName('a')
    var current = window.location.pathname.split('/')[1];
    for (var i = 0; i < anchor.length; i++) {
        split_array = anchor[i].href.split('/')
        selected = split_array[split_array.length-1]
        if(selected == current) {
            anchor[i].className="active nav-link"
        }
    }
});
function show_popup(msg){
    document.getElementById('popup_text').innerText = msg
    $("#confirmation_modal").show()
}
function reload(){
    location.reload()
}
function view_recipe(recipe_id) {
    window.location.href = "/recipe/"+recipe_id;
}

function cancel_request() {

}