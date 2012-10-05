;(function($){
    $.widget('editliveWidgets.foreignkeyField', $.editliveWidgets.textField, {
        _type: 'foreignkey',
        sourceSelect: false,
        options: {
            maxlength: 10
        },

        _source_is_select: function(){
            if (typeof(this.__source_is_select) == 'undefined') {
                var src = this.options.source;
                this.__source_is_select = src && src[0] == '#' && $(src)[0].tagName == 'SELECT';
            }
            return this.__source_is_select
        },

        _parse_select_source: function() {
            var $self = this;
            $self.data = [];
            $self.sourceSelect.find('option').each(function(){ 
                $self.data.push({label: $(this).text(), value: $(this).val()});
            });
            return $self.data
        },

     ///get_display_value: function() {
     ///    var val = this._get_value();
     ///    if (this.sourceSelect) {
     ///        return this.sourceSelect.find('option[value="'+ val +'"]').text();
     ///    }
     ///    else {
     ///        return val;
     ///    }
     ///},

        _init: function(){
            var $self = this;
            if ($self._source_is_select()) {
                $self.sourceSelect  = $($self.options.source).hide();
                $self.options.source = $self._parse_select_source();

                $self.options.focus = function(e, ui) {
                    if (ui.item) {
                        $self.input.val(ui.item.label);
                        return false;
                    }
                };

                $self.options.select = function(e, ui) {
                    $self.element.val(ui.item.value);
                    $self.blur();
                    $self.input.val('');
                    return false;
                };

              //$self.options.source = function(request, response) {
              //    var rs = $.ui.autocomplete.filter($self.data, request.term);
              //    if ($self.options.maxlength) {
              //        return rs.slice(0, $self.options.maxlength);
              //    }
              //    else {
              //        return rs;
              //    }
              //};
            }

            //$.editliveWidgets.textField.prototype._init.apply(this, arguments);
            $self.input = $('<input class="editlive" style="width:'+ ($self.options.width || '') +';" type="text" />').hide().insertAfter($self.element);
            $self.input.autocomplete($self.options)
                .data('autocomplete')._renderItem = function(ul, item){
                    return $('<li />').appendTo(ul)
                            .data( "item.autocomplete", item)
                            .append('<a>' + item.label + '</a>');
                };

            $self._createPlaceholder($self.input);
        },
        get_display_value: function() {
            return this.rendered_val || this.element.find('option:selected').text();
        },

        focus: function(e){
            var $self = this;
            $self._trigger('focus')
            if (typeof($self._parent_is_btn) == 'undefined') {
                $self._parent_is_btn = $self.control.hasClass('btn');
            }
            if ($self._parent_is_btn) {
                $self.input.parents('.editlive-control-group').removeClass('btn');
            }
            $self.placeholder.hide();
            $self.input.show().focus();
            //$self._bind_kb_blur_events($self.input);
            $self._set_element_width($self.input);
            $self._watch_blur($self.input);
            $self._trigger('focused')
        },

        show: function() {
            console.log('CCC');
            this.input.show();
            if (this.placeholder) this.placeholder.hide();
        },

        hide: function() {
            this.input.hide();
            if (this.placeholder) this.placeholder.show();
        },
    })
})(jQuery);
