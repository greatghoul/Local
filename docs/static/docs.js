$(function() {
    // Show add document panel.
    $('#add-doc-btn').click(function() {
        // Remove previous panel.
        $('#add-doc').remove()

        // Show a new add document panel
        $("#tpl-add-doc").mustache({ }).prependTo("#doc-list");
        $('#add-doc').slideDown();

        // Event bindings
        $('#add-doc-save').click(function() {
            alert('New document created.');
            $('#add-doc').slideUp(function() {
                $(this).remove();
            });
            return false;
        });
        $('#add-doc-cancel').click(function() {
            $('#add-doc').slideUp(function() {
                $(this).remove();
            });
            return false;
        });
    });
    
});
