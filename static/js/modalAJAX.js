
// $("#add-desk-button").click(addButton);

$("a.modal_desk_icon").click(function () {
  var id = $(this).attr("id");
  console.log(id)

  desk_id_obj = {}
  desk_id_obj.desk_id = id

  $.ajax({
    url: "/dashboard/getDeskInfo/",
    data: desk_id_obj,
    dataType: "json",
    success: function (res) {
      console.log(res);
      $("div.modalSelectFolderAJAX").html(res.data);
    }
  });

  
});
