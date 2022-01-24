function addButton() {
  $.ajax({
    url: "/dashboard/getDeskInfo/",
    dataType: "json",
    success: function (data) {console.log(data);}
  });
}

$("#add-desk-button").click(addButton);
