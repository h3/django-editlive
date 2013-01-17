;(function($){
    /**
     * dateField - A date picker widget
     *
     * @name jQuery.fn.dateField
     * @class
     *
     * We have to deal with 4 different date formatting syntax. As if
     * it wasn't enough some of them conflict..
     *
     *  1. JavaScript: The JavaScript date and time picker needs 2 different
     *     formats. One for the date and the other for the time. 
     *
     *  2. Django as it's own implementation which is used for template tags.
     *     settings.DATE_FORMAT
     *     settings.DATETIME_FORMAT
     *     https://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
     *
     *  3. Python also has it's own date time format which is used for input 
     *     fields
     *     settings.DATE_INPUT_FORMAT
     *     settings.DATETIME_INPUT_FORMAT
     *     http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
     * 
     * +----+----+----+---------------------------------------+
     * | Py | Dj | Js | Description                           |
     * +====+====+====+=======================================+
     * |    | j  | d  | day of month (no leading zero)        |
     * | d  | d  | dd | day of month (two digit)              |
     * |    | z  | o  | day of the year (no leading zeros)    |
     * | j  | z  | oo | day of the year (three digit) *       |
     * | a  | D  | D  | day name short                        |
     * | A  | l  | DD | day name long                         |
     * |    | n  | m  | month of year (no leading zero)       |
     * | m  | m  | mm | month of year (two digit)             |
     * | b  | M  | M  | month name short                      |
     * | B  | F  | MM | month name long                       |
     * | y  | y  | y  | year (two digit)                      |
     * | Y  | Y  | yy | year (four digit)                     |
     * |    | U  | @  | Unix timestamp (ms since 01/01/1970)  |
     * +----+----+----+---------------------------------------+
     * | H  | h-H| hh | Hour, 12/24-hour format.              |
     * |    | g  | h  | Hour, 12/24-hour format without zeros |
     * | M  | i  | mi | Minutes with zeros.                   |
     * |    |    | m  | Minutes (unsupported by django)       |
     * | S  | s  | ss | Seconds, 2 digits with leading zeros  |
     * |    |    | s  | Seconds (unsupported by django)       |
     * | f  | u  | l  | Microseconds                          |
     * | Z  | T  | z  | Time zone                             |
     * |    |    | t  | AM/PM (unsupported by django)         |
     * | P  | A  | tt | AM/PM                                 |
     * +----+----+----+---------------------------------------+
     *
     */

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

        $self._createPlaceholder();
        $self.element.width(160).wrap('<div class="input-append" />').hide();
        $self.element.datepicker($self.options);
        $('<span class="add-on"><i class="icon-calendar"></i></span>')
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
        if (!this.control.hasClass('error')) {
            this._unwatch_blur();
            this._unbind_kb_blur_events();
            this.element.parent().hide();
            this.placeholder.removeClass('no-blur');
            if (this.placeholder) this.placeholder.show();
        }
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
                && !$self.control.hasClass('error')
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
