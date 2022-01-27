$(document).ready(function () {
  //muncipal
  $("#create-modal-folder-button").click(function () {
    var folder_name = $("#modal-folder-name-id").val();
    var desk_id = $(".folder-modal-add-button").attr("id");
    console.log(desk_id);

    data = {};
    data.folder_name = folder_name;
    data.desk_id = desk_id;

    $.ajax({
      url: "/dashboard/create-folder/",
      data: data,
      dataType: "json",
      success: function (res) {
        var host = window.location.host;
        console.log(host);
        $.getScript("../../static/js/RefreshFolderModal.js", function () {});
        //$("div.modalSelectFolderAJAX").html(res.data);
      },
    });
  });
});

// worksapce dash board modal
$("#create-workspace-folder-button").click(function () {
  var folder_name = $("#workspace-folder-name-id").val();
  var desk_id = $(".desk-title").attr("id");
  console.log(desk_id);

  data = {};
  data.folder_name = folder_name;
  data.desk_id = desk_id;

  $.ajax({
    url: "/dashboard/create-folder/",
    data: data,
    dataType: "json",
    success: function (res) {
      var host = window.location.host;
      console.log(host);
      $.getScript(
        "../../static/js/DisplayWorkSpaceFolderList.js",
        function () {}
      );
      console.log(res);
      //$("div.modalSelectFolderAJAX").html(res.data);
    },
  });
});
