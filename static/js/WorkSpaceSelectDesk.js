$("a.select-desk").click(function () {
    console.log("clicked on desk")
  var id = $(this).attr("id");
  desk_id_obj = {};
  desk_id_obj.desk_id = id;

  $.ajax({
    url: "/dashboard/workspace-inside-desk/",
    data: desk_id_obj,
    dataType: "json",
    beforeSend: function () {},
    success: function (res) {
      $("#desk-AJAX-load").html(res.data);
    },
  });
});