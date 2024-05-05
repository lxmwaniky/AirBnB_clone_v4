$(document).ready(function () {
        let amount = {};
        $(document).on('change', "input[type='checkbox']", function () {
            if (this.checked) {
                amount[$(this).data('id')] = $(this).data('name');
            } else {
                delete amount[$(this).data('id')];
            }
            let lst = Object.values(amount);
            if (lst.length > 0) {
                $('div.amenities > h4').text(Object.values(amount).join(', '));
            } else {
                $('div.amenities > h4').html('&nbsp;');
            }
        });
    });
