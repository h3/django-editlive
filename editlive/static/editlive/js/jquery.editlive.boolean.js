;(function($){

    $.widget('editliveWidgets.booleanField', $.editliveWidgets.charField, {
        _type: 'boolean',
        options: {
            choices: 'Oui|Non'
        },
        _init: function() {
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
        },

        _populate: function() {
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
        },

        _display_errors: function(errors) {
            var $self = this;
            $.each(errors, function(k, v) {
                var el = $self.btn_group;
                el.tooltip({
                    title: v.message,
                    placement: $self.options.errorplacement
                }).tooltip('show');
            });
        },

        get_value_display: function() {
            var $self = this;
            if ($self.element.is(':checked')) {
                return $self.label_on;
            }
            else {
                return $self.label_off;
            }
        },

        _get_value: function() {
            if (this.element.is(':checked')) return true;
            else return false;
        }
    });

})(jQuery);
