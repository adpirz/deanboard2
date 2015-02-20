$(document).ready(function() {
	$('#alphathepup').hide();
	$('#clickforpup').click(function() {
		$('#alphathepup').toggle();
	});
	$(".click-row").click(function() {
        window.document.location = $(this).data("href");
    });
});