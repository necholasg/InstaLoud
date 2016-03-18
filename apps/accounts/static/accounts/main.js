$(document).ready(function(){

$(".button-collapse").sideNav();

$('button').click(function(){
    var url = "";
    url = $(this).attr("url");
    SC.oEmbed(url,{
        element: document.getElementById('widget'), iframe: true , auto_play: true, maxheight: 115, color: '#e0f2f1', show_comments: false
    });
    });

$('.comment_button').submit(function() {
        var html_string = ""
        var test = $(this).attr('post_id');
        var username = $(this).attr('user');
        var comment = $(this).val()
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


$('.like_button').on("click",function() {
    var total = parseInt($(this).attr('like_counter')) + 1
    $(this).addClass("red lighten-1");
    $(this).html("<i class='large material-icons center'>whatshot</i>" + total)
});


});
