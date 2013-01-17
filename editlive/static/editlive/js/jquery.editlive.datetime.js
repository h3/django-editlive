;(function($){
    /**
     * datetimeField - A datetime picker widget
     *
     * @name jQuery.fn.datetimeField
     * @class
     */
    var datetimeField = {
        _type: 'datetime',
        options: {}
    };

    datetimeField._init = function(){
        var $self = this;
        $self.options.onClose = function() {
            $self.blur();
        };

        if ($self.options.format) {
            $self.options.dateFormat = $self._translate_date_format();
            console.log($self.options.dateFormat);
        }

        $self._createPlaceholder();
        $self.element.width(160).wrap('<div class="input-append" />').hide();
        $self.element.datetimepicker($self.options);
        $('<span class="add-on"><i class="icon-time"></i></span>')
            .hide().insertAfter($self.element)
            .bind('click.editlive', function(e){
                $self.element.datetimepicker('show');
            });
    };

    $.widget('editliveWidgets.datetimeField', $.editliveWidgets.dateField, datetimeField);

})(jQuery);
