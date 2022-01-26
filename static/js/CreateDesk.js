
// for Muncipal Dashboard Modal
$("#create-modal-desk-button").click(function(){
  var desk_name  = $("#modal-desk-name-id").val();

  data = {}
  data.desk_name = desk_name
  
  $.ajax({
    url: "/dashboard/create-desk/",
    data: data,
    dataType: "json",
    success: function (res) {
      $.getScript("../../static/js/DisplayDeskModal.js",function(){});
      console.log(res);
      //$("div.modalSelectFolderAJAX").html(res.data);
    }
  });

});


$("#create-workspace-desk-button").click(function(){
  var desk_name  = $("#workspace-desk-name-id").val();

  data = {}
  data.desk_name = desk_name
  
  $.ajax({
    url: "/dashboard/create-desk/",
    data: data,
    dataType: "json",
    success: function (res) {
      $.getScript("../../static/js/DisplayWorkSpaceDeskList.js",function(){});
      console.log(res);
      //$("div.modalSelectFolderAJAX").html(res.data);
    }
  });

});










