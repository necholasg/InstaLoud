$(document).ready(function(){
    $('.slider').slider({full_width : true, height : 400, indicators:false, interval: 4500, transition: 600});
    // Pause slider
    $('.slider').slider('pause');
    // Start slider
    $('.slider').slider('start');
    // Next slide
    $('.slider').slider('next');
    // Previous slide
    $('.slider').slider('prev');
    $('.modal-trigger').leanModal({
      dismissible: true, // Modal can be dismissed by clicking outside of the modal
      opacity: .5, // Opacity of modal background
      in_duration: 300, // Transition in duration
      out_duration: 200 // Transition out duration
    });

    }); //end of document.ready
    