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
$(document).ready(function() {
    var ingredientsContainer = $('#ingredients-container');
    var addIngredientButton = $('#add-ingredient');
    var ingredientIndex = 1;

    addIngredientButton.click(function() {
        var newIngredient = `
            <div class="ingredient-input">
                <label for="ingredient-${ingredientIndex}">Ingredient:</label>
                <input type="text" id="ingredient-${ingredientIndex}" name="ingredients" required>
                <button type="button" class="remove-ingredient">Remove</button>
            </div>
        `;
        ingredientsContainer.append(newIngredient);
        ingredientIndex++;

        $('.remove-ingredient').click(function() {
            $(this).parent('.ingredient-input').remove();
        });
    });
});