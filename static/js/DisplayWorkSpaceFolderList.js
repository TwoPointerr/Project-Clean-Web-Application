$(document).ready(function () {
  console.log("inside Load Desk AJAX")
  displayFolderDesks();
  function displayFolderDesks() {
    var desk_id = $(".desk-title").attr("id");
    console.log("Inside Display WS Folder list JS:"+desk_id);

    data = {};
    data.desk_id = desk_id;

    $.ajax({
      url: "/dashboard/display-workspace-desk-folders/",
      data : data,
      dataType: "json",
      beforeSend: function () {},
      success: function (res) {
        console.log("inside display Folders");
        $("#folder-list-AJAX-load").html(res.data);
      },
    });
  }
});

