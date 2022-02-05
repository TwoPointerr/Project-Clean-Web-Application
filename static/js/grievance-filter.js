$(document).ready(function() {
    var _filterObj = {};
    $(".ajaxLoader").hide();
    var desk_id = $("h2.desk-title").attr("id");
    var folder_id = $("h2.folder-title").attr("id");

    filterFunctionsAJAX();
    
    $("#grievance_cat,  #sort_by, #voteFilterBtn, #grievance_stat, #gri_loc, #reset_btn").on('click', function() {
        //console.log("inside filter");
        filterFunctionsAJAX();
    });
    
    function filterFunctionsAJAX(){
        console.log("inside filter");
        var _minVote = $('#minVote').val();
        var _maxVote = $('#maxVote').val();
        _filterObj.minVote = _minVote;
        _filterObj.maxVote = _maxVote;
        $("#grievance_cat").each(function(index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
                return el.value;
            });
        });
        

        $("#grievance_stat").each(function(index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
                return el.value;
            });
        });

        $("#gri_loc").each(function(index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
                return el.value;
            });
        });

        // $("#article_type").each(function(index, ele) {
        //     var _filterVal = $(this).val();
        //     var _filterKey = $(this).data('filter');
        //     _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
        //         return el.value;
        //     });
        // });

        $("#sort_by").each(function(index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            // console.log(_filterVal);
            // console.log(_filterKey);
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
                return el.value;
            });
        });

        // $("#color_filter").each(function(index, ele) {
        //     console.log("this is the color list");
        //     var _filterVal = $(this).val();
        //     var _filterKey = $(this).data('filter');
        //     _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
        //         return el.value;
        //     });
        // });
        _filterObj.desk_id = desk_id;
        _filterObj.folder_id = folder_id;
        // console.log(_filterObj)
            //Ajax Functionality
        $.ajax({
            url: '/dashboard/filter-data',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function() {
                $(".ajaxLoader").show();
            },
            success: function(res) {
                // console.log("inside filter");
                $("#filteredGrievances").html(res.data);
                $(".ajaxLoader").hide();
            }
        });
    }
});