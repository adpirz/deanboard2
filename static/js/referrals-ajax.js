$(document).ready(function() {
	$('#alphathepup').hide();
	$('#clickforpup').click(function() {
		$('#alphathepup').toggle();
	});
	$(".click-row").click(function() {
        window.document.location = $(this).data("href");
    });
    $.fn.dataTable.moment('ddd, MMM M');
    $('#previous-table, #all-table').DataTable({
    	'lengthChange':false,
    	'pageLength':40,
    	'order':[[0,'desc']]
    });
});
