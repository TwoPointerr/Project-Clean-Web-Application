$(document).ready(function () {

    //move to folder
    $("a.folder-modal-list").click(function(){
        var folder_id = $(this).attr("id");
        data = {};
        data.folder_id = folder_id;
        data.gri_id = selectedGrievanceID;
        console.log("Inside Move Gri ID "+selectedGrievanceID);
        console.log("Click on move button in MoveGri.js "+folder_id);

        $.ajax({
            url: "/dashboard/move-gri-to-folder/",
            data: data,
            dataType: "json",
            success: function (res) {
              console.log("inside Move gri file move to folder "+res);
              $.getScript("../../static/js/grievance-filter.js", function () {});
            },
          });
    });

    $("#move-to-desk-button").click(function(){
        var desk_id = $("a.folder-modal-add-button").attr("id");
        console.log(desk_id+"clicked on MOve here button")

        data = {};
        data.desk_id = desk_id;
        data.gri_id = selectedGrievanceID;
        console.log("Inside Move Gri ID "+selectedGrievanceID);
        

        $.ajax({
            url: "/dashboard/move-gri-to-desk/",
            data: data,
            dataType: "json",
            success: function (res) {
              console.log("inside Move gri file move to desk "+res);
              $.getScript("../../static/js/grievance-filter.js", function () {});
            },
          });
    });
});
