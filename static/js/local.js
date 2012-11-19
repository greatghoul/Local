$(function() {
    $('.alert-messages .alert').delay(2000).slideUp();
    
    $('[data-confirm]').on('click', function() {
        return confirm($(this).data('confirm'));
    });
});
