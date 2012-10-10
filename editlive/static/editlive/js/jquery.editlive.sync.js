;(function($){

    var objects = {};

    $.editlive.sync = function() {
        $('editlive').each(function(){
            var el = $(this);
            if (el.attr('app-label') && el.attr('module-name') && el.attr('field-name') && el.attr('object-id')) {
                var model = el.attr('app-label') +'.'+ el.attr('module-name');
                if (!objects[model]) objects[model] = [];
                objects[model].push({
                    app_label: el.attr('app-label'),
                    field_name: el.attr('field-name'),
                    //field_type: el.data('type'),
                    rendered_value: el.attr('rendered-value'),
                    object_id: el.attr('object-id'),
                    template_filters: el.attr('template_filters'),
                    module_name: el.attr('module-name'),
                    formset: el.attr('formset'),
                    value: $('#'+ el.data('field-id')).val()
                    //data: el.data()
                });
            }
        });
    };

    var synched = function(data) {
        console.log(data);
    }

    $.editlive.do_sync = function() {
        Dajaxice.editlive.sync(synched, objects);
    };

    $(function(){
        $.editlive.sync();
    });
})(jQuery);
