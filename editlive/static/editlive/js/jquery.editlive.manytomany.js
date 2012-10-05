;(function($){
    $.widget('editliveWidgets.manytomanyField', $.editliveWidgets.foreignkeyField, {
        _type: 'manytomany',
        sourceSelect: false,
        selected: [],
        options: {},

        _init: function(){
            var $self = this;
            if ($self._source_is_select()) {
                $self.sourceSelect  = $($self.options.source)//.hide();
                $self.options.source = $self._parse_select_source();

                $self.options.focus = function(e, ui) {
                    if (ui.item) {
                        $self.input.val(ui.item.label);
                        return false;
                    }
                };

                $self.options.select = function(e, ui) {
                    $self._add_item(ui.item.value)
                    $self.blur();
                    $self.input.val('');
                    return false;
                };
            }

            $self.input = $('<input class="editlive" type="text" />')
                .prop('placeholder', 'Ajouter')
                .insertAfter($self.element)
                .autocomplete($self.options)

            $self.input.data('autocomplete')._renderItem = function(ul, item){
                return $('<li />').appendTo(ul)
                        .data( "item.autocomplete", item)
                        .append('<a>' + item.label + '</a>');
            };

            if ($self.options.width) {
                var chim = parseInt($self.input.css('padding-left').match(/\d+/)[0], 10) 
                           + parseInt($self.input.css('padding-right').match(/\d+/)[0], 10);
                $self.input.css('width', $self.options.width - chim);
            }

            $self._createPlaceholder($self.input);
        },

        _rm_item: function(e, el) {
            var newval = [],
                p = el.parent(),
                val = p.data('value');

            $.each(this._get_value(), function(k, v) { 
                if (v != val) newval.push(v); 
            });

            this._set_value(newval);
            this.change();
            p.slideUp(function(){
                $(this).remove();
            });
        },

        _add_item: function(v) {
            var val = this._get_value() || [],
                label = this.element.find('option[value="'+ v +'"]').text();
            val.push(v);
            this._set_value(val);
            this._create_list_item(label, v);
        },

        _create_list_item: function(label, val) {
            var $self = this,
                li = $('<li />').appendTo($self.selectedList),
                rm = $('<i class="icon-remove" />')
                        .bind('click.editlive', function(e){
                            $self._rm_item.apply($self, [e, $(this)]);
                        });
            li.text(label);
            li.data('value', val).append(rm);
        },

        _createPlaceholder: function(el) {
            var $self = this,
                out = [];
            $self.selectedList = $('<ul class="editlive editlive-m2m" />');
            $self.selectedList.hide().insertBefore($self.input).width($self.input.width());
            $self.sourceSelect.find('option').each(function(){ 
                if ($(this).is(':selected')) {
                    var s = {label: $(this).text(), value: $(this).val()}
                    $self._create_list_item(s.label, s.value);
                    $self.selected.push(s);
                }
            });
            if (this.element.find('option:selected').length > 0) {
                this.selectedList.slideDown('fast');
            }
        },

        change: function() {
            $.editliveWidgets.foreignkeyField.prototype.change.apply(this, arguments);
            if (this.element.find('option:selected').length == 0) {
                this.selectedList.slideUp();
            }
            else if (this.selectedList.not(':visible')) {
                this.selectedList.slideDown();
            }
        },

        hide: function() {},
        show: function() {}
    })
})(jQuery);
