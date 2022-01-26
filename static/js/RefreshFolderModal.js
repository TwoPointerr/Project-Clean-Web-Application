$(document).ready(function () {
  refreshAJAX();
  function refreshAJAX() {
    var desk_id = $(".folder-modal-add-button").attr("id");
    desk_id_obj = {};
    desk_id_obj.desk_id = desk_id;
    $.ajax({
      url: "/dashboard/display-modal-folder-list/",
      data: desk_id_obj,
      dataType: "json",
      success: function (res) {
        console.log(res);
        $("div.modalSelectFolderAJAX").html(res.data);
      },
    });
  }
});

