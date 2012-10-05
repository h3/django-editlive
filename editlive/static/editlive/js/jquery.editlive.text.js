(function($){

    $.fn.autoGrowInput = function(o) {

        o = $.extend({
            width: false,
            maxwidth: 1000,
            minwidth: 0,
            comfortZone: 20,
            highlightColor: '#b3ffa0'
        }, o);

        this.filter('input:text').each(function(){

            var minwidth = o.minwidth || $(this).width(),
            val = '',
            input = $(this),
            testSubject = $('<tester/>').css({
                position: 'absolute',
                top: -9999,
                left: -9999,
                width: 'auto',
                fontSize: input.css('fontSize'),
                fontFamily: input.css('fontFamily'),
                fontWeight: input.css('fontWeight'),
                letterSpacing: input.css('letterSpacing'),
                whiteSpace: 'nowrap'
            }),
            check = function() {

                if (val === (val = input.val())) {return;}

                // Enter new content into testSubject
                var escaped = val.replace(/&/g, '&amp;').replace(/\s/g,' ').replace(/</g, '&lt;').replace(/>/g, '&gt;');
                testSubject.html(escaped);

                // Calculate new width + whether to change
                var testerWidth = testSubject.width(),
                    newWidth = (testerWidth + o.comfortZone) >= minwidth ? testerWidth + o.comfortZone : minwidth,
                    currentWidth = input.width(),
                    isValidWidthChange = (newWidth < currentWidth && newWidth >= minwidth)
                        || (newWidth > minwidth && newWidth < o.maxwidth);

                // Animate width
                if (isValidWidthChange) {
                    input.width(newWidth);
                }

            };

        testSubject.insertAfter(input);

        $(this).bind('keyup keydown blur update', check);

        });

        return this;

    };

})(jQuery);


;(function($){

    $.widget('editliveWidgets.textField', {
        _type: 'text',
        _active: false,
        widgetEventPrefix: 'widget',
        value: undefined,
        options: {
            minwidth: 120,
            maxwidth: 'auto',
            emptyvalue: 'Cliquer pour modifier',
            wrapclass: 'inline',
            errorplacement: 'bottom'
        },

        // Setup the widget
        _create: function() {
            var $self = this;
            $self.value        = $self._get_value();
            $self.editlive     = $self.element.data('widget.editlive');
            $self.options      = $.extend($self.options, $self.editlive.data());
            $self.control      = $('<div class="control-group editlive-control-group '+ $self.options.wrapclass +'" />');
            $self.field_name   = $self.editlive.attr('field-name'); 
            $self.object_id    = $self.editlive.attr('object-id');
            $self.app_label    = $self.editlive.attr('app-label');
            $self.module_name  = $self.editlive.attr('module-name');
            $self.rendered_val = $self.editlive.attr('rendered-value');
            $self.tpl_filters  = $self.editlive.attr('template_filters');

            if ($self.options.maxwidth != 'auto') {
                $self.control.css('max-width', $self.options.maxwidth);
            }

            if ($self.options.width) {
                var chim = parseInt($self.element.css('padding-left').match(/\d+/)[0], 10) 
                           + parseInt($self.element.css('padding-right').match(/\d+/)[0], 10);
                $self.element.css('width', $self.options.width - chim);
            }

            $self.element.hide().wrap($self.control);
        },

        _init: function(){
            var $self = this;
            $self._createPlaceholder();
            if (!this.option.width) {
                $self.element.autoGrowInput({
                    maxwidth: $self.options.maxwidth == 'auto' && $self.element.parent().parent().width() || $self.options.maxwidth
                });
            }
            if ($self.options.width) {
                var chim = parseInt($self.placeholder.css('padding-left').match(/\d+/)[0], 10) 
                           + parseInt($self.placeholder.css('padding-right').match(/\d+/)[0], 10);
                $self.placeholder.css('width', $self.options.width - chim);
            }
        },

        _get_value: function() {
            return this.element.val();
        },

        _set_value: function(v) {
            this.value = v;
            return this.element.val(v);
        },

        _createPlaceholder: function(el) {
            var $self = this;
            $self.placeholder = $('<span class="editlive editlive-'+ $self._type +'" />')
                                    .insertAfter(el || $self.element)
            $self.placeholder.bind('click.editlive', function(e) {
                $self.focus();
            });
            $self.set_placeholder_value();
        },

        // Respond to changes to options
        _setOption: function( key, value ) {
            switch( key ) {
                case "clear":
                    // handle changes to clear option
                    break;
            }
            // In jQuery UI 1.9 and above, you use the _super method instead
            // this._super("_setOption", key, value);
            // In jQuery UI 1.8, you have to manually invoke the _setOption method from the base widget
            $.Widget.prototype._setOption.apply(this, arguments);
        },

        _get_width: function() {
            if (this.option.width) return this.option.width;
            var width = this.placeholder.width()
            if (width > this.control.width()) width = this.control.width() - 10;
            if (width < this.option.minwidth) width = this.option.minwidth;
            if (width < 0) width = 'none';
            return width;
        },

        _watch_blur: function(el) {
            // The element passed as argument
            // will not trigger the blur
            var $self = this;
            $('html').bind('click.editlive_'+ $self.element.attr('id'), function(e){
                var targetId = $(e.target).attr('id')
                if (typeof(targetId) == 'undefined') {
                    if (!$(e.target).hasClass('editlive')) {
                        $self.blur();
                    }
                }
                else {
                    if (targetId != (el || $self.element).attr('id')) {
                        $self.blur();
                    }

                }
            });
        },

        _unwatch_blur: function() {
            $('html').unbind('click.editlive_'+ this.element.attr('id'))
        },

        _bind_kb_blur_events: function(el) {
            var $self = this;
            (el || $self.element).bind('keyup.editlive', function(e){
                if (e.keyCode == 13) $self.blur();     // enter
                if (e.keyCode == 27) $self.blur(true); // escape (no save)
            });
        },

        _unbind_kb_blur_events: function(el) {
            (el || this.element).unbind('keyup.editlive');
        },

        _set_element_width: function(el) {
            var el = el || this.element;
            if (!this.options.width) el.width(this._get_width());
            if (this.control.hasClass('block')) {
                el.css('display', 'inline-block');
            }
        },

        _saved: function(data) {
            var $self = this;
            if (data.error) {
                $self.error(data);
            }
            else {
                $self.success(data);
            }
        },

        _display_errors: function(errors) {
            var $self = this;
            $.each(errors, function(k, v) {
                var el = $('[name="'+ v.field_name +'"]');
                el.tooltip({
                    title: v.message,
                    placement: $self.options.errorplacement
                }).tooltip('show');
            });
        },

        focus: function(e){
            console.log('111');
            var $self = this;
            $self._trigger('focus')
            $self.show();
            if (typeof($self._parent_is_btn) == 'undefined') {
                $self._parent_is_btn = $self.control.hasClass('btn');
            }
            $self.control.removeClass('btn');
            $self._trigger('focused')
        },

        blur: function(cancel){
            var $self = this;
            if ($self._parent_is_btn) {
                $self.input.parents('.editlive-control-group').addClass('btn');
            }
            if (cancel) {
                $self._set_value($self.value);
                $self.hide();
            }
            else if ($self.value != $self._get_value()) {
                $self.value = $self._get_value();
                $self.change();
            }
            else {
                $self.hide();
            }
            $self._trigger('blur');
        },

        show: function() {
            console.log('ZZZ');
            this._bind_kb_blur_events();
            this._set_element_width();
            this._watch_blur();
            if (this.placeholder) this.placeholder.hide();
            this.element.show().focus();
            this.element.next('.add-on').css('display', 'inline-block');
        },

        hide: function() {
            this._unwatch_blur();
            this._unbind_kb_blur_events();
            this.element.hide();
            if (this.placeholder) this.placeholder.show();
        },

        change: function(){
            var $self = this;
            $self.save();
            $self._trigger('change');
        },

        get_display_value: function() {
            return this.rendered_val || this.element.val();
        },

        set_placeholder_value: function(display) {
            if (this.placeholder) {
                var val = display || this.get_display_value() || this.options.emptyvalue;
                this.placeholder.text(val);
            }
        },

        save: function() {
            var $self = this;
            $self._trigger('save');
            Dajaxice.editlive.save($.proxy($self._saved, $self), {
                field_value:   $self._get_value(), 
                field_name:    $self.field_name, 
                object_id:     $self.object_id,
                app_label:     $self.app_label,
                module_name:   $self.module_name,
                tpl_filters:   $self.tpl_filters
            });
        },

        success: function(data) {
            var $self = this;
            if (data.rendered_value) {
                $self.rendered_val = data.rendered_value;
            }
            $self.set_placeholder_value();
            $self.control.removeClass('error');
            $self.blur(true);
            if (!$self._parent_is_btn && $self.placeholder) {
                var oldColor = $self.placeholder.css('background-color');
                $self.placeholder
                    .css('background-color', $self.options.highlightColor)
                    .animate({backgroundColor: oldColor});
            }
            $self._trigger('success');
        },

        error: function(data) {
            var $self = this;
            $self.control.addClass('error');
            $self._display_errors(data.messages);
            $self._trigger('error');
        },

        // Clean up any modifications made to the DOM
        destroy: function() {
            var $self = this;
            // In jQuery UI 1.9 and above, you would define _destroy instead of 
            // destroy and not call the base method
            $.Widget.prototype.destroy.call($self);
            $self.element.show();
            if ($self.placeholder) {
                $self.placeholder.remove();
            }
        }
    })
})(jQuery);

//.delegate( "li.multi-option-item", "click", $.proxy( this._itemClick, this ) );
