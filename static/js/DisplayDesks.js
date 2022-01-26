console.log("insode desk js");
//WorkspaceDashboard
$(document).ready(function () {
  displayNewDesk()
  function sendRequest() {
    $.ajax({
      url: "/dashboard/display-desk-cont/",
      success: function (data) {
        console.log("insode send reuest cont");
        $("#desk-AJAX-load").html(data.data); //insert text of test.php into your div
      },
      complete: function () {
        // Schedule the next request when the current one's complete
        setInterval(sendRequest, 5000); // The interval set to 5 seconds
      },
    });
  }

  function displayNewDesk() {
    $.ajax({
      url: "/dashboard/display-desk-cont/",
      dataType: "json",
      beforeSend: function () {},
      success: function (res) {
          console.log("inside displayNew Desk")
        $("#desk-AJAX-load").html(res.data);
      },
    });
  }
});


