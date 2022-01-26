$(document).ready(function () {
  displayNewDesk();
  function displayNewDesk() {
    data = {};
    data.template_name = "workspace";
    $.ajax({
      url: "/dashboard/display-desks-list/",
      data: data,
      dataType: "json",
      beforeSend: function () {},
      success: function (res) {
        console.log("inside displayNew Desk");
        $("#desk-AJAX-load").html(res.data);
      },
    });
  }
});
