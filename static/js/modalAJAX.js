
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

$("#create-desk-button").click(function(){
  var desk_name  = $("#desk-name-id").val();

  data = {}
  data.desk_name = desk_name
  
  $.ajax({
    url: "/dashboard/create-desk/",
    data: data,
    dataType: "json",
    success: function (res) {
      $.getScript("../../static/js/DisplayDesks.js",function(){});
      console.log(res);
      //$("div.modalSelectFolderAJAX").html(res.data);
    }
  });

});




