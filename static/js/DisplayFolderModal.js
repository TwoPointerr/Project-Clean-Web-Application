$("a.modal_desk_icon").click(function () {
  var id = $(this).attr("id");
  console.log(id);

  desk_id_obj = {};
  desk_id_obj.desk_id = id;

  $.ajax({
    url: "/dashboard/display-modal-folder-list/",
    data: desk_id_obj,
    dataType: "json",
    success: function (res) {
      console.log("inside Display Folder modal JS");
      $("div.modalSelectFolderAJAX").html(res.data);
    },
  });
});
