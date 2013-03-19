;(function($, _){
    /**
     * booleanField - Widget for boolean fields (drop down menu)
     *
     * @name jQuery.fn.booleanField
     * @class
     */

    var booleanField = {
        _type: 'boolean',
        widgetEventPrefix: 'editlive',
        options: {
            choices: _(' Yes| No'),
            icon_on: 'ok-sign',
            icon_off: 'minus-sign',
            class_on: 'btn',
            class_off: 'btn'
        }
    };

    booleanField._create = function() {
        var $self = this;
        $.editliveWidgets.charField.prototype._create.apply(this, arguments)
        var label = $self.options.choices.split('|');
        $self.label_on = label[0];
        $self.label_off = label[1];
        $self.element.hide();
        $self.btn = $('<a class="btn" />').insertAfter($self.element);
        $self.btn.bind('click.editlive', function() {
            $self._toggle();
        });
        $self.element.is(':checked') ? $self._set_on(true) : $self._set_off(true);
    };

    booleanField._init = function() {};

    booleanField._toggle = function() {
        this.element.is(':checked') ? this._set_off() : this._set_on();
    };

    booleanField._set_value = function(v) {
        this.value = v;
        this.element.prop('checked', v);
        return v;       
    };

    booleanField._set_on = function(nochange) {
        this._set_value(true);
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
        this._set_value(false);
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

    booleanField.blur = function(cancel){
        var $self = this;
        $self._trigger('blur', null, $self);
    };

    $.widget('editliveWidgets.booleanField', $.editliveWidgets.charField, booleanField);

})(jQuery, gettext);
