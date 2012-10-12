;(function($){

    $.widget('editliveWidgets.textField', $.editliveWidgets.charField, {
        _type: 'text',
        options: {},
        _create: function() {
            var $self = this;
            if (!$self.options.width) {
                // Restric native textarea resizing to vertical only
                $self.element.css('min-width', $self.element.parent().width() - 17) 
                             .css('max-width', $self.element.parent().width() - 17);
            }
            if (!$self.options.width) {
                $self.element.css('min-height', $self.element.height(200));
            }
            $.editliveWidgets.charField.prototype._create.apply(this, arguments);
        },

        _bind_kb_blur_events: function(el) {
            var $self = this;
            (el || $self.element).bind('keyup.editlive', function(e){
                // Same as the parent's _bind_kb_blur_events except that
                // it does not blur on "enter" since it's a textarea. To
                // achieve the same result you must use shift+enter.
                if (e.keyCode == 13 && e.shiftKey) { // enter
                    $self.blur();
                    e.preventDefault(); // otherwise a \n will be inserted
                }
                if (e.keyCode == 27) $self.blur(true); // escape (no save)
            });
        }
    });

})(jQuery);
