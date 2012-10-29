;(function($){
    
    $.widget('editliveWidgets.foreignkeyField', $.editliveWidgets.charField, {
        _type: 'foreignkey',
        sourceSelect: false,
        options: {},

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

            //$.editliveWidgets.charField.prototype._init.apply(this, arguments);
            $self.input = $('<input class="editlive" type="text" />').hide().insertAfter($self.element);
            $self.input.autocomplete($self.options)
                .data('autocomplete')._renderItem = function(ul, item){
                    return $('<li />').appendTo(ul)
                            .data( "item.autocomplete", item)
                            .append('<a>' + item.label + '</a>');
                };

            if ($self.options.maxwidth != 'auto') {
                $self.input.css('max-width', $self.options.maxwidth);
            }

            if ($self.options.width) {
                var chim = parseInt($self.element.css('padding-left').match(/\d+/)[0], 10) 
                           + parseInt($self.element.css('padding-right').match(/\d+/)[0], 10);
                $self.input.css('width', $self.options.width - chim);
            }

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
    });

    $.widget('editliveWidgets.foreignkeyFieldSelect', $.editliveWidgets.charField, {
        _type: 'foreignkey',
        _init: function(){
            this._createPlaceholder();
            if (this.options.width) {
                var chim = parseInt(this.element.css('padding-left').match(/\d+/)[0], 10) 
                           + parseInt(this.element.css('padding-right').match(/\d+/)[0], 10);
                this.element.css('width', this.options.width - chim);
            }
        },
    });

})(jQuery);
