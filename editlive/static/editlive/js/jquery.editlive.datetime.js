;(function($){

    $.widget('editliveWidgets.datetimeField', $.editliveWidgets.dateField, {
        _type: 'datetime',
        options: {},

        _init: function(){
            var $self = this;
            $self.options.onClose = function() {
                $self.blur();
            };
            $self._createPlaceholder();
            $self.element.width(160).wrap('<div class="input-append" />').hide();
            $self.element.datetimepicker($self.options);
            $('<span class="add-on"><i class="icon-time"></i></span>')
                .hide().insertAfter($self.element)
                .bind('click.editlive', function(e){
                    $self.element.datetimepicker('show');
                });
        }
    });
})(jQuery);
