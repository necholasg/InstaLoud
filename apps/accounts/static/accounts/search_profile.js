$(document).ready(function() {
    $('#search').submit(function() {
        var html_string = ""
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(res){
            if (res){
                for(var i = 0; i < res.length; i++){
                console.log(res)
                
                html_string += "<div class='col s12'> <div class='card hoverable'> <div class='card-content '> <span class='card-title teal-text text-lighten-1'>User Name: "+ res[i].fields.username + "</span> <a href='/profile/"+ res[i].fields.username + "/'><button class='waves-effect waves-light btn-large right' url = '/profile/"+ res[i].fields.username + "/' id='follow'> View Profile<i class='large material-icons right'>perm_identity</i></button></a></div></div></div>";
                }
                $('#results').html(html_string);
            }
            else{
                $('#results').html("Sorry, that user could not be found--- :(");
            }


            },
            error: function(xhr, status, error) {
                $('#results').html("<h4>Sorry, that user could not be found :( Please search Again</h4>");
            }
        });
        return false;
});

    $(".button-collapse").sideNav();
    $(".dropdown-button").dropdown();
});
