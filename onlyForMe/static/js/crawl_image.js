$(document).ready(function(){
    $('#search_image').click(function(){
        $.ajax({
            url:'/oduck/crawl_image/search/',
            type:'post',
            data:$('form').serialize(),
            success: function(data){
                console.log('data : ', data)
                if( data.success == 'true'){
                    $.each(data.urls, function( index, value ) {
                        console.log( index + ": " + value );
                        $('.gallery')
                        .append('<div class="img"><a href="' + value + '" download><img src=' +
                          value + ' alt="load failed" class="crawl_image" width="300" height="200"></a></div>')
                    });
                    // if( $('#login_error').length )
                    //         $('#login_error').remove();
                    // $('#popupLogin').popup("open");
                    console.log('oh yeah')
                }

                else{
                    // if( $('#login_error').length )
                    //     $('#login_error').html(data);
                    // else
                    //     $('<h1 class="ui-bar ui-bar-d ui-mini ui-corner-all" id="login_error">'+data+'</h1>').prependTo('#login_form');
                    console.log('fuck you')
                }
            }
        });
        return false;
    });

    $('.crawl_image').on('click')
});
