setInterval(function()
{ 
    $.get(
        'statistics', function(data) {
            var parsed_data = JSON.parse(data);
            $('#total_sales').text(parsed_data.total_sales_amount)
            $('#average').text(parsed_data.average_amount_per_order)
        }
    );
}, 1000);