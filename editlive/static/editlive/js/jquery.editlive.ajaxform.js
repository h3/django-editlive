;(function($){

    $.fn.serializeJSON = function() {
        var o = {}, a = this.serializeArray();
        $.each(a, function() {
            if (o[this.name]) {
                if (!o[this.name].push) o[this.name] = [o[this.name]];
                o[this.name].push(this.value || '');
            } else {
                o[this.name] = this.value || '';
            }
        });
        return o;
    };

    $.widget('editliveWidgets.ajaxform', {
        _type: 'ajaxform',
        _selector: 'editlive[data-type="ajaxform"]',
        options: {
            errorPlacement: 'bottom',
            refreshElement: false
        },

        _create: function() {
            var $self = this;
            console.log(this.element);
            $self.form = $('#'+ $self.element.data('form-id'));
            $self.options = $.extend(this.options, $self.element.data());
            $self.form.find('[type="submit"]').bind('click.ajaxform', function(e){
                e.preventDefault();
                $self.submit();
                return false;
            });
        },

        _get_post_data: function() {
            var out = { meta: {}, data: this.form.serializeJSON() };
            $.each(this.options, function(k, v){
                if (typeof(v) != 'object') {
                    out.meta[k] = v;
                }
            });
            return out;
        },

        _get_field_name: function(fieldname) {
            if (this.options.formPrefix) {
                return this.options.formPrefix +'-'+ fieldname;
            }
            else {
                return fieldname;
            }
        },

        _display_errors: function(errors) {
            var $self = this;
            $.each(errors, function(k, v) {
                var el = $('[name="'+ $self._get_field_name(v.field_name) +'"]');
                el.parents('.control-group').addClass('error');
                el.tooltip({
                    title: v.message,
                    placement: $self.options.errorPlacement
                }).tooltip('show');
            });
        },

        error: function(data) {
            var $self = this;
            this.form.addClass('error');
            this._display_errors(data.messages);
            this._trigger('error');
        },

        success: function(data) {
            var $self = this;
            $self.form[0].reset();
            $self.form.removeClass('error');
            $self.form.find('.control-group.error').removeClass('error');
            $self._trigger('success');
            if ($self.options.refreshElement) {
                var url = window.location.pathname + ' #' + $self.options.refreshElement
                $('#'+ $self.options.refreshElement).load(url, function(){
                    $.editlive.load(this);
                    $(this).children().first().unwrap();
                    $self._trigger('refreshed');
                });
            }
        },

        submit: function() {
            this._trigger('submit');
            Dajaxice.editlive.save_form($.proxy(this.submited, this), this._get_post_data());
        },

        submited: function(data) {
            if (data.error) {
                this.error(data);
            }
            else {
                this.success(data);
            }
        }

    });
})(jQuery);
