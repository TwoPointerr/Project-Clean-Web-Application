$(document).ready(function () {
    $("#reject-gri-modal-button").click(function(){
        data ={}
        data.gri_id = selectedGrievanceID

        $.ajax({
            url: "/dashboard/reject-gri/",
            data: data,
            dataType: "json",
            success: function (res) {
              console.log("inside Move gri file move to folder "+res);
              $.getScript("../../static/js/grievance-filter.js", function () {});
            },
          });
        console.log("Clicked on reject modal button "+selectedGrievanceID);
    });
});