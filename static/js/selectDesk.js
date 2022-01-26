console.log("insode desk js")

//WorkspaceDashboard 
$("a.desk").click(function(){
    var id = $(this).attr('id');
    desk_id_obj = {}
    desk_id_obj.desk_id = id
    
    $.ajax({
        url: '/dashboard/loadDesk/',
        data: desk_id_obj,
        dataType: 'json',
        beforeSend: function() {
            
        },
        success: function(res) {
            $("#desk-AJAX-load").html(res.data);
        }
    });

});