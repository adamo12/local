$.get('server.html',function(data){
myDiv = $(data).find('#divShow');
$('#divShow').html(myDiv.html());
})