;(function($){
    /**
     * dateField - A date picker widget
     *
     * @name jQuery.fn.dateField
     * @class
     * 
     * +----+----+--------------------------------------+
     * | Dj | Js | Description                          |
     * +====+====+======================================+
     * | j  | d  | day of month (no leading zero)       |
     * | d  | dd | day of month (two digit)             |
     * | z  | o  | day of the year (no leading zeros)   |
     * | z  | oo | day of the year (three digit) *      |
     * | D  | D  | day name short                       |
     * | l  | DD | day name long                        |
     * | n  | m  | month of year (no leading zero)      |
     * | m  | mm | month of year (two digit)            |
     * | M  | M  | month name short                     |
     * | F  | MM | month name long                      |
     * | y  | y  | year (two digit)                     |
     * | Y  | yy | year (four digit)                    |
     * | U  | @  | Unix timestamp (ms since 01/01/1970) |
     * +----+----+--------------------------------------+
     *
     */

    var djangoDateFormatMap = {
        j:'d', d:'dd', z:'o', z:'oo',
        D:'D', l:'DD', n:'m', m:'mm',
        M:'M', F:'MM', y:'y', Y:'yy',
        U:'@'};

    var dateField = {
        _type: 'date',
        options: { 
            showOn: 'button',
            currentText: 'Maintenant',
            closeText: 'Ok'
        }
    };

    dateField._init = function(){
        var $self = this;
        $self.options.onClose = function() {
            $self.blur();
        };

        if ($self.options.format) {
            var format = $self.options.format,
                tokens = $self.options.format.match(/(%\w+)/g);
            for (var x in tokens) {
                format = format.replace(tokens[x], djangoDateFormatMap[tokens[x].replace('%','')])
            }
            $self.options.dateFormat = format;
        }

        $self._createPlaceholder();
        $self.element.width(160).wrap('<div class="input-append" />').hide();
        $self.element.datepicker($self.options);
        $('<span class="add-on"><i class="icon-time"></i></span>')
            .hide().insertAfter($self.element)
            .bind('click.editlive', function(e){
                $self.element.datepicker('show');
            });
    };

    dateField.show = function() {
        if (this.placeholder) this.placeholder.hide();
        this.placeholder.addClass('no-blur');
        this.element.parent().show();
        this.element.next('.add-on').css('display', 'inline-block');
        this.element.show().focus();
        this._bind_kb_blur_events();
        this._set_element_width();
        this._watch_blur();
    };

    dateField.hide = function() {
        this._unwatch_blur();
        this._unbind_kb_blur_events();
        this.element.parent().hide();
        this.placeholder.removeClass('no-blur');
        if (this.placeholder) this.placeholder.show();
    };

    dateField._unwatch_blur = function() {
        this.element.parent().removeClass('no-blur').find('div, span, i, input').removeClass('no-blur');
        $('html').unbind('click.editlive_'+ this.element.attr('id'))
    };

    dateField._watch_blur = function() {
        var $self = this;
        this.element.parent().addClass('no-blur').find('div, span, i, input').addClass('no-blur');
        $('html').bind('click.editlive_'+ $self.element.attr('id'), function(e){
            var target = $(e.target),
                _parent = target.parent();
            if (!target.hasClass('ui-datepicker-current') 
                && !target.parents('.ui-datepicker').get(0) 
                && !target.parents('.ui-datepicker-header').get(0)) {
                if (!target.hasClass('no-blur')) {
                        $self.blur();
                }
                else {
                    if (_parent.hasClass('add-on')) {
                        _parent = _parent.parent();
                    }
                    if (!_parent.find('#' + $self.element.attr('id')).get(0)) {
                        $self.blur();
                    }
                }
            }
        });
    };

    $.widget('editliveWidgets.dateField', $.editliveWidgets.charField, dateField);
})(jQuery);
