$(document).ready(function () {
    let amnt = {};
    $(document).on('change', "input[type='checkbox']", function () {
      if (this.checked) {
        amnt[$(this).data('id')] = $(this).data('name');
      } else {
        delete amnt[$(this).data('id')];
      }
    /**
     * Represents a list of values.
     * @type {Array}
     */
      let lst = Object.values(amnt);
      if (lst.length > 0) {
        $('div.amenities > h4').text(Object.values(amnt).join(', '));
      } else {
        $('div.amenities > h4').html('&nbsp;');
      }
    });

  $.get('http://0.0.0.0:5001/api/v1/status/', function (data, textStatus) {
    if (textStatus === 'success') {
      if (data.status === 'OK') {
        $('#api_status').addClass('available');
      } else {
        $('#api_status').removeClass('available');
      }
    }
  });
});  