;(function($){
    $.widget('editliveWidgets.listactions', {
        _type: 'listactions',
        _standalone: true,
        _selector: 'editlive[data-type="listactions"]',
        options: {},

        _init: function(){
            var $self = this;
            $self.editlive = $($self.element.data('widget.editlive'));
            $self.items    = $($self.element.data('actions'));
            $self.options  = $.extend(this.options, $self.element.data());
            $self.menu     = $($self.element.data('menu')).hide();

            $self.items
                .unbind('change.editlive')
                .bind('change.editlive', function(e){
                    $self.select($(this));
                    return false;
                });

            $self.menu.find('a[data-action]')
                .unbind('click.editlive')
                .bind('click.editlive', function(e) {
                    var a = $(this)
                        confirmMsg = a.data('confirm-message') || "Are you sure ?";
                    e.preventDefault();
                    if (!a.data('confirm') || 
                        (a.data('confirm') && $self.doConfirm(confirmMsg)))  {
                        $self.action.apply($self, [a.data('action'), a.data('callback') || function(){}]);
                    }
                });
        },

        doConfirm: function(msg) {
            return confirm(msg);
        },

        action: function(action, callback) {
            var $self = this,
                ns = action.split('.'),
                djx = window[ns[0]][ns[1]][ns[2]],
                out = [],
                m = {};

            if (!$.isFunction(callback)) {
                callback = window[callback];
            }

            this.items.filter(':checked').each(function() {
                out.push($(this).data('object-id'));
            });

            $.each(this.editlive.data(), function(k, v) {
                if (k != 'listactions' && k != 'widget.editlive') { 
                    m[k] = v;
                }
            });

            djx($.proxy(callback, this), {
                meta: m,
                objects: out
            });
            
            if (/delete|remove/.test(ns[2])) {
                $.each(out, function(k, v) {
                    $self.items.filter('[data-object-id="'+ v +'"]').each(function() {
                        if ($(this).data('row')) {
                            $(this).parents($(this).data('row'))
                                .slideUp(function(){ $(this).remove()});
                        }
                    });
                });
            }
        },

        refresh: function() {
            if (this.items.filter(':checked').length > 0) {
                this.menu.show();
            }
            else {
                this.menu.hide();
            }
            this.updateButtonText();
        },

        updateButtonText: function() {
            var msg, 
                selected = this.items.filter(':checked').filter('[data-row]').length,
                text = this.menu.find('.text');

            if (text.get(0)) {
                if (selected == 0) { 
                    msg = 'Aucun itème sélectionné'   
                }
                else {
                    if (selected == 1) {
                        msg = '1 itèmes sélectionné';
                    }
                    else {
                        msg = selected + ' éléments sélectionnés';
                    }
                }
                this.menu.find('.text').text(msg);
            }
        },

        select: function(el) {
            if (el.data('object-id') == 'all') {
                var checked = el.prop('checked');
                this.items.each(function() {
                    var el = $(this);
                    el.prop('checked', checked);
                    if (el.data('row')) {
                        if (checked) el.parents(el.data('row')).addClass('selected');
                        else el.parents(el.data('row')).removeClass('selected');
                    }
                });
            }

            if (el.data('row')) {
                if (el.prop('checked')) el.parents(el.data('row')).addClass('selected');
                else el.parents(el.data('row')).removeClass('selected');
            }
            this.refresh();
        }

    });

})(jQuery);
