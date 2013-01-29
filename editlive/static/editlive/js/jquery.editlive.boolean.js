;(function($){
    /**
     * booleanField - Widget for boolean fields (drop down menu)
     *
     * @name jQuery.fn.booleanField
     * @class
     */

    var booleanField = {
        _type: 'boolean',
        options: {
            choices: ' Oui| Non',
            icon_on: 'ok-sign',
            icon_off: 'minus-sign',
            class_on: 'btn',
            class_off: 'btn'
        }
    };

    booleanField._init = function() {
        var $self = this,
            label = $self.options.choices.split('|')

        $self.label_on = label[0];
        $self.label_off = label[1];
        $self.element.hide();
        $self.btn = $('<a class="btn" />').insertAfter($self.element);
        $self.btn.bind('click.editlive', function() {
            $self._toggle();
        });

        $self.element.is(':checked') ? $self._set_on(true) : $self._set_off(true);
    };

    booleanField._toggle = function() {
        this.element.is(':checked') ? this._set_off() : this._set_on();
    };

    booleanField._set_on = function(nochange) {
        this.element.prop('checked', true);
        this.btn.empty();
        if (this.options.icon_off) {
            this.btn.append('<i class="icon icon-'+ this.options.icon_on +'"></i>');
        }
        this.btn.removeClass(this.options.class_off)
            .addClass(this.options.class_on).append(this.get_value_display());
        if (typeof(nochange) == 'undefined') {
            this.change();
        }
    };

    booleanField._set_off = function(nochange) {
        this.element.prop('checked', false);
        this.btn.empty();
        if (this.options.icon_off) {
            this.btn.append('<i class="icon icon-'+ this.options.icon_off +'"></i>');
        }
        this.btn.removeClass(this.options.class_on)
            .addClass(this.options.class_off).append(this.get_value_display());
        if (typeof(nochange) == 'undefined') {
            this.change();
        }
    };

    booleanField._display_errors = function(errors) {
        var $self = this;
        $.each(errors, function(k, v) {
            $self.btn.tooltip({
                title: v.message,
                placement: $self.options.errorplacement
            }).tooltip('show');
        });
    };

    booleanField.get_value_display = function() {
        var $self = this;
        if ($self.element.is(':checked')) {
            return $self.label_on;
        }
        else {
            return $self.label_off;
        }
    };

    booleanField._get_value = function() {
        if (this.element.is(':checked')) return true;
        else return false;
    };

    $.widget('editliveWidgets.booleanField', $.editliveWidgets.charField, booleanField);

})(jQuery);
