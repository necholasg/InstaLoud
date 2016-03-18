$(document).ready(function() {
    $('#check_button').click(function() {
        var url = "http://api.soundcloud.com/resolve?url=";
        url += $('#id_song_url').val();
        url += "&client_id=78e1af2348744cd4ef538bba33cf82fa";
        $.ajax({
          url: url,
          success: function(data) {
                var html_string = "";
                $('#errors').html("");
                html_string = data.artwork_url.substring(0, data.artwork_url.length - 10);
                html_string += "-t500x500.jpg";
                $('#target_pic').attr('src',html_string);
                $('#errors').html("Found your song!");
                $('#url_status').attr('value','True');
                $('#album_art').attr('value',html_string);
                $('#id_song_url').attr('readonly','readonly');
          },
          error: function(xhr, status, error) {
            $('#target_pic').attr('src','http://www.shutterstock.com/music/static/1.0.37/implementation/images/album_artwork_placeholder_detail.jpg');
            $('#errors').html("<p><b>Could not find song. Please put a correct URL.</b></p>");
          }
         
        });
         return false;

    });
    


});