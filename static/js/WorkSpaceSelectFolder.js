$("a.select-folder").click(function () {
  
  var id = $(this).attr("id");
  folder_id_obj = {};
  folder_id_obj.folder_id = id;
  console.log("clicked on folder ID :"+id)

  $.ajax({
    url: "/dashboard/workspace-inside-folder/",
    data: folder_id_obj,
    dataType: "json",
    beforeSend: function () {},
    success: function (res) {
      $("#desk-AJAX-load").html(res.data);
    },
  });
});