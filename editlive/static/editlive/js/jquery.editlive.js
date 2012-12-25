;(function($){

    var getJsOptions = function(el){
        var data = el.data(), opts = {}, opt,
        excluded = ['adaptor', 'type', 'fieldid', 'plugin'];

        $.each(data, function(k, v){
            if ($.inArray(k.toLowerCase(), excluded) < 0) {
                opts[k] = v;
            }
        })
        return opts;
    };
    
    $.inherit = function(p, c) {
        for (var x in c) p[x] = c[x];
    };

    $.editlive = (function($) {
        $self = this;

        return {
            load: function(el) {
                (el && $(el).find('editlive') || $('editlive')).each(function(k, v) {
                    $.editlive.loadWidget(v);
                });
            },

            loadWidget: function(el){
                var el = $(el);
                var initialized = el.data('initialized') || false;
                if (initialized) return true;
                else {
                    var widgetname = el.data('widget') || el.data('type');
                    if ($.isFunction($.editliveWidgets[widgetname])) {
                        var opts, options, input;
                        var opts  = getJsOptions(el);

                        if ($.editliveWidgets[widgetname].prototype._standalone) {
                            // Special case for ajaxforms and listactions
                            input = el;
                        }
                        else {
                            // We start by checking for a close match. Theorically there
                            // shouldn't be two fields with the same id, but in reality it
                            // does happens and it does fuck up editlive.
                            input_id = '#'+ el.data('field-id');
                            input = el.prev(input_id);
                            if (!input.get(0)) input = el.closest(input_id);
                            if (!input.get(0)) input = el.parent().find(input_id);
                            if (!input.get(0)) input = $(input_id);
                        }

                        input.data('widget.editlive', el);
                        input[widgetname]([input, opts]);
                        el.data('initialized', true);
                    }

                }
            }
        }
    
    })($); 

    $.fn.editlive = function(method, arg) {
        var editlive = $(this).data('editlive');
        if (editlive) {
            switch(method) {
                case 'link':
                    $(arg).text(editlive._get_value());
                    $(this).bind('editlivesuccess', function(){
                        $(arg).text(editlive._get_value());
                    });
                break;
                case 'val':
                    if (arg) {
                        editlive._set_value(arg);
                        editlive.change();
                        return arg;
                    }
                    else {
                        return editlive._get_value();
                    }
                break;
            }
        }
    };

    $(function(){
        $.editlive.load()
        $('[rel="tooltip"]').tooltip()
    });
})(jQuery);
