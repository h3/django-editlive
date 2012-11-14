;(function($){

    var $id = function(i){ return $('#'+i) };

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
                (el && $(el).find('editlive') || $('editlive')).each(function(k, v){
                    $.editlive.loadWidget(v);
                });
            },

            getByFieldId: function(fieldId) {
                if (fieldId[0] == '#') fieldId = fieldId.slice(1);
                return $('editlive[data-field-id="'+ fieldId +'"]');
            },

            loadWidget: function(el){
                var el = $(el), initialized = el.data('initialized') || false;
                if (initialized) return true;
                else {
                    var widgetname = el.data('widget') || el.data('type');
                    if ($.isFunction($.editliveWidgets[widgetname])) {
                        var opts, options, input;
                        var opts  = getJsOptions(el);
                        input_id = $id(el.data('field-id'));

                        // We start by checking for a close match. Theorically there
                        // shouldn't be two fields with the same id, but in reality it
                        // does happens and it does fuck up editlive.
                        input = el.prev(input_id);
                        if (!input.get(0)) input = el.closest(input_id);
                        else if (!input.get(0)) input = el.parent().find(input_id);
                        else input = $(input_id);

                        if (!input.length && $.editliveWidgets[widgetname].prototype._selector) {
                            input = $($.editliveWidgets[widgetname].prototype._selector);
                        }

                        input.data('widget.editlive', el);
                        input[widgetname]([input, opts]);
                        el.data('initialized', true);
                    }

                }
            }
        }
    
    })($); 

    $(function(){
        $.editlive.load()
        $('[rel="tooltip"]').tooltip()
    });
})(jQuery);
