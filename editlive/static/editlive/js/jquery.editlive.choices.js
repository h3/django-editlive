;(function($){

    $.widget('editliveWidgets.choicesField', $.editliveWidgets.charField, {
        _type: 'choices',
        options: {
            choices: []
        },
        _init: function() {
            var $self = this;

            $self.element.hide();

            $self.element.find('option').each(function(k, v){
                var opt = $(v), item = {value: opt.val(), label: opt.text()};
                $self.options.choices.push(item);
                if (opt.is(':selected')) $self.selected = item;
            });

            $self.btn_group = $('<div class="btn-group" />').insertAfter($self.element);
            $self.btn_label = $('<button class="btn" />').appendTo($self.btn_group);
            $self.choices   = $('<ul class="dropdown-menu" />').appendTo($self.btn_group);
            $self.btn_toggle = $(['<button class="btn dropdown-toggle" data-toggle="dropdown">',
                                  '<span class="caret"></span></button>'].join(''))
                                  .insertAfter($self.btn_label);

            if ($self.options.mini)  $self.btn_label.add($self.btn_toggle).addClass('btn-mini');
            if ($self.options.small) $self.btn_label.add($self.btn_toggle).addClass('btn-small');
            if ($self.options.large) $self.btn_label.add($self.btn_toggle).addClass('btn-large');

            $self._populate();
        },

        _populate: function() {
            var $self = this;
            $self.choices.empty();
            $.each($self.options.choices, function(k, item) {
                if (item.value != $self.selected.value) {
                    $('<li><a href="#'+ item.value +'">'+ item.label +'</a></li>')
                        .appendTo($self.choices)
                        .bind('click.editlive', function(){
                            $self.btn_group.removeClass('open');
                            $self.selected.label = $(this).find('a').text();
                            $self.selected.value = $(this).find('a').attr('href').slice(1);
                            $self._set_value($self.selected.value);
                            $self.choices.find('li').remove();
                            $self.element.prop('selected', false);
                            $self.change();
                            $self._populate();
                            return false;
                        });
                }
            });
            if ($self.selected) {
                $self.btn_label.text($self.selected.label);
            }
            else {
                $self.btn_label.text('------');
            }
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
            return this.element.find('option:selected').val()
        },

        success: function(data) {
            var $self = this;
            $self._populate();
            $self._trigger('success');
        },

        error: function(data) {
            var $self = this;
            $self.control.addClass('error');
            $self._display_errors(data.messages);
            $self._trigger('error');
        }
        
    })
})(jQuery);
