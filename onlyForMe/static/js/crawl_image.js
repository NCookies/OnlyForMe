$(document).ready(function(){
    $('#search_image').click(function(){
        $.ajax({
            url:'/oduck/crawl_image/search/',
            type:'post',
            data:$('form').serialize(),
            success: function(data){
                console.log('data : ', data)
                if( data.success == 'true'){
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

    $('')
});
