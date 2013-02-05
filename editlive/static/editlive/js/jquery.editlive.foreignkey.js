;(function($){
    /**
     * foreignkeyField - Autocomplete widget for foreignkey field
     *
     * @name jQuery.fn.foreignkeyField
     * @class
     */
    var foreignkeyField = {
        _type: 'foreignkey',
        sourceSelect: false,
        options: {}
    };

    foreignkeyField._source_is_select = function(){
        if (typeof(this.__source_is_select) == 'undefined') {
            var src = this.options.source;
            this.__source_is_select = src && src[0] == '#' && $(src)[0].tagName == 'SELECT';
        }
        return this.__source_is_select
    };

    foreignkeyField._parse_select_source = function() {
        var $self = this;
        $self.data = [];
        $self.sourceSelect.find('option').each(function(){ 
            $self.data.push({label: $(this).text(), value: $(this).val()});
        });
        return $self.data
    };

    foreignkeyField._init = function(){
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
    };

    foreignkeyField.get_display_value = function() {
        return this.rendered_val || this.element.find('option:selected').text();
    };

    foreignkeyField.focus = function(e){
        var $self = this;
        $self._trigger('focus', null, $self)
        $self.placeholder.hide();
        $self.input.show().focus();
        $self._set_element_width($self.input);
        $self._watch_blur($self.input);
        $self._trigger('focused', null, $self)
    };

    foreignkeyField.show = function() {
        this.input.show();
        if (this.placeholder) this.placeholder.hide();
    };

    foreignkeyField.hide = function() {
        this.input.hide();
        if (this.placeholder) this.placeholder.show();
    }
    
    $.widget('editliveWidgets.foreignkeyField', $.editliveWidgets.charField, foreignkeyField);

    /**
     * foreignkeyFieldSelect - Standard dropdown select for foreignkey field
     *
     * @name jQuery.fn.foreignkeyFieldSelect
     * @class
     */
    var foreignkeyFieldSelect = {
        _type: 'foreignkey',
        options: {}
    };

    foreignkeyFieldSelect._init = function(){
        this._createPlaceholder();
        if (this.options.width) {
            var chim = parseInt(this.element.css('padding-left').match(/\d+/)[0], 10) 
                       + parseInt(this.element.css('padding-right').match(/\d+/)[0], 10);
            this.element.width(this.options.width - chim + 6);
            var chim = parseInt(this.placeholder.css('padding-left').match(/\d+/)[0], 10) 
                       + parseInt(this.placeholder.css('padding-right').match(/\d+/)[0], 10);
            this.placeholder.width(this.options.width - chim + 8);
            this.element.css('margin-bottom', this.placeholder.css('margin-bottom'));
        }
    };

    $.widget('editliveWidgets.foreignkeyFieldSelect', $.editliveWidgets.charField, foreignkeyFieldSelect);

})(jQuery);
