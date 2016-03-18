$(document).ready(function() {
    $('#search').submit(function() {
        var url = "https://api.soundcloud.com/tracks?q=";
        url += $('#search_input').val();
        url += "&client_id=78e1af2348744cd4ef538bba33cf82fa&limit=20";
        var csrftoken = getCookie('csrftoken');
        $.get(url, function(res) {
            var html_string = ""
            for(var i = 0; i < res.length; i++)
            {
                html_string+=
                "<div class='row'> <div class='col s12'> <div class='card hoverable'> <div class='card-content '> <span class='card-title teal-text text-lighten-1'>" + res[i].title + "</span><br> <img src='" + res[i].artwork_url + "'><br><p>Number of plays: " + res[i].playback_count + "</p></div> <div class='card-action teal-text text-lighten-1'style ='padding-bottom:70px'><button class='waves-effect waves-light btn-large left' url = '" + res[i].permalink_url + "' id='play_button'>Play<i class='large material-icons right'>play_circle_outline</i></button> <form action='/add/' method='post' id='form" + i + "'> <input type='hidden' name='csrfmiddlewaretoken' value='" + csrftoken + "'><input type='hidden' name='add_song' value='" + res[i].permalink_url + "'> </form><button style='display:inline-block;' form = 'form" + i + "' type='submit' class='waves-effect waves-light btn-large right'><i class='large material-icons right'>add</i>Post Song</button></div></div></div></div>";
            }
            $('#results').html(html_string);
        }, 'json');

        return false;
    });

    $(document).on("click","#play_button",function(){
        var url = "";
        url = $(this).attr("url");
        SC.oEmbed(url,{
            element: document.getElementById('widget'), iframe: true , auto_play: true, maxheight: 115, color: '#e0f2f1', show_comments: false
        });
    })

    $(".button-collapse").sideNav();
    $(".dropdown-button").dropdown();


});




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
