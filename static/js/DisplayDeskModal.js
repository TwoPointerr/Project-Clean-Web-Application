console.log("insode desk js");
displayDeskListModal();
function displayDeskListModal() {
  data = {}
  data.template_name = "muncipal_dashboard"
  $.ajax({
    url: "/dashboard/display-desks-list/",
    data: data,
    dataType: "json",
    beforeSend: function () {},
    success: function (res) {
        console.log("inside displayNew Desk")
      $("#modal-desk-list").html(res.data);
    },
  });
}

