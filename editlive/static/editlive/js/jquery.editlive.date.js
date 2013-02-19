;(function($){
    /**
     * dateField - A date picker widget
     *
     * @name jQuery.fn.dateField
     * @class
     *
     */

    var dateField = {
        _type: 'date',
        widgetEventPrefix: 'editlive',
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
        this.element.show().focus()
            .parent().show()
                .find('.add-on').css('display', 'inline-block');
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
