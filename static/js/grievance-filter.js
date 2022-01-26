$(document).ready(function() {
    console.log("inside filter");
    $(".ajaxLoader").hide();
    $("#grievance_cat,  #sort_by, #voteFilterBtn, #grievance_stat").on('click', function() {
        //console.log("inside filter");
        var _filterObj = {};
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

        // $("#brand_cat").each(function(index, ele) {
        //     console.log("this is the brand list");
        //     var _filterVal = $(this).val();
        //     var _filterKey = $(this).data('filter');
        //     _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
        //         return el.value;
        //     });
        // });

        // $("#article_type").each(function(index, ele) {
        //     var _filterVal = $(this).val();
        //     var _filterKey = $(this).data('filter');
        //     _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function(el) {
        //         return el.value;
        //     });
        // });

        $("#sort_by").each(function(index, ele) {
            console.log("this is the sort by list");
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            console.log(_filterVal);
            console.log(_filterKey);
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

        console.log(_filterObj)
            //Ajax Functionality
        $.ajax({
            url: '/dashboard/filter-data',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function() {
                $(".ajaxLoader").show();
            },
            success: function(res) {
                console.log("inside filter");
                $("#filteredGrievances").html(res.data);
                $(".ajaxLoader").hide();
            }
        });

    });
});