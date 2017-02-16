$(function() {
    $('.tf_keyword')
        .focus(function() {
            $('.box_search').addClass('box_search_on');
        })
        .blur(function() {
            $('.box_search').removeClass('box_search_on');
        });
});
