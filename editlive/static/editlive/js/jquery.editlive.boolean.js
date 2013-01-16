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
            choices: 'Oui|Non'
        }
    };

    booleanField._init = function() {
        var $self = this,
            label = $self.options.choices.split('|')

        $self.label_on = label[0];
        $self.label_off = label[1];
        $self.element.hide();
        $self.btn_group = $('<div class="btn-group" />').insertAfter($self.element);
        $self.btn_label = $('<button class="btn" />').appendTo($self.btn_group);
        $self.choices   = $('<ul class="dropdown-menu" />').appendTo($self.btn_group);
        $self.btn_toggle = $(['<button class="btn dropdown-toggle" data-toggle="dropdown">',
                              '<span class="caret"></span></button>'].join(''))
                              .insertAfter($self.btn_label);
        $self._populate();
    };

    booleanField._populate = function() {
        var $self = this;
        if ($self.element.is(':checked')) {
            $('<li><a href="#off">'+ $self.label_off +'</a></li>')
                .appendTo($self.choices)
                .bind('click.editlive', function(){
                    $self.btn_group.removeClass('open');
                    $self.choices.find('li').remove();
                    $self.element.prop('checked', false);
                    $self.change();
                    $self._populate();
                    return false;
                });
        }
        else {
            $('<li><a href="#on">'+ $self.label_on +'</a></li>')
                .appendTo($self.choices)
                .bind('click.editlive', function(){
                    $self.btn_group.removeClass('open');
                    $self.choices.find('li').remove();
                    $self.element.prop('checked', true);
                    $self.change();
                    $self._populate();
                    return false;
                });
        }
        $self.btn_label.text(this.get_value_display());
    };

    booleanField._display_errors = function(errors) {
        var $self = this;
        $.each(errors, function(k, v) {
            var el = $self.btn_group;
            el.tooltip({
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


    /**
     * booleanFieldButton - a widget for boolean fields (switch button)
     *
     * @name jQuery.fn.booleanFieldButton
     * @class
     */
    var booleanFieldButton = {
        _type: 'boolean',
        options: {
            choices: ' Oui| Non',
            icon_on: 'ok-sign',
            icon_off: 'minus-sign',
            class_on: 'btn',
            class_off: 'btn'
        }
    };

    booleanFieldButton._init = function() {
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

    booleanFieldButton._toggle = function() {
        this.element.is(':checked') ? this._set_off() : this._set_on();
    };

    booleanFieldButton._set_on = function() {
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

    booleanFieldButton._set_off = function(nochange) {
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

    booleanFieldButton._display_errors = function(errors) {
        var $self = this;
        $.each(errors, function(k, v) {
            $self.btn.tooltip({
                title: v.message,
                placement: $self.options.errorplacement
            }).tooltip('show');
        });
    };

    booleanFieldButton.get_value_display = function() {
        var $self = this;
        if ($self.element.is(':checked')) {
            return $self.label_on;
        }
        else {
            return $self.label_off;
        }
    };

    booleanFieldButton._get_value = function() {
        if (this.element.is(':checked')) return true;
        else return false;
    };

    $.widget('editliveWidgets.booleanFieldButton', $.editliveWidgets.charField, booleanFieldButton);

})(jQuery);
