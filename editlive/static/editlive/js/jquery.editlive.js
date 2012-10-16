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
                    var widgetname = el.data('type');
                    if ($.isFunction($.editliveWidgets[widgetname])) {
                        var opts, options, input;
                        opts  = getJsOptions(el);
                        input = $id(el.data('field-id'));

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
