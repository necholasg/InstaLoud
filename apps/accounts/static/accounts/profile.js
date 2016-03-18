$(document).ready(function(){

$(".button-collapse").sideNav();

$('.btn-large').click(function(){
    var url = "";
    url = $(this).attr("url");
    SC.oEmbed(url,{
        element: document.getElementById('widget'), iframe: true , auto_play: true, maxheight: 115, color: '#e0f2f1', show_comments: false
    });
    });
$('.modal-trigger').leanModal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .1, // Opacity of modal background
      in_duration: 0, // Transition in duration
      out_duration: 0 // Transition out duration
    });

$('#follow').click(function() {
        var html_string = "<p style='font: 400 38px 'Pacifico', Helvetica, sans-serif;'>Followed!</p>"
        $.ajax({
            url: $(this).attr('href'),
            success: function(res){

            $('#follow1').html(html_string);
            },
            error: function(xhr, status, error) {
                $('#follow1').html("<h4>Sorry</h4>");
            }
        });
        return false;
});


$(document).on('click','.like_form', function() {

        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            cache: false,
            success: function(res){

            $(this).unbind('submit');
            }
        });
        return false;
});

$('.like_button').one("click",function() {
    var total = parseInt($(this).attr('like_counter')) + 1
    $(this).addClass("red lighten-1");
    $(this).html("<i class='large material-icons center'>whatshot</i>" + total)
});

$('.comment_button').submit(function() {
        var html_string = ""
        var test = $(this).attr('post_id');
        var username = $(this).attr('user');
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(res){
            html_string += res[res.length -1].fields.content;
            $('#comments'+test).append('<div class="row"><div class="chip"><a class="teal-text text-lighten-2" href= /profile/' + username + '">' + username + '</a></div>' + html_string + '</div>');
            }
        });
        return false;
});

});
