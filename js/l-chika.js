var url = './api/api-button.cgi';

$(function() {
    setInterval(getButtonStatus, 100);
});

var getButtonStatus = function() {
    $.getJSON(url, function(data) {
	var status = data[0]['data'];
	if (status == '1') {
	    $('body').removeClass('off').addClass('on');
	} else {
	    $('body').removeClass('on').addClass('off');
	}
    });
}
