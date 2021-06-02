var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return typeof sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
    return false;
};

var returnConsole = function returnConsole(sValue) {
    console.log(sValue, '-------------------------');
};

window.onload = function(event) {
    //event.stopPropagation(true);
    var job_id = getUrlParameter('job_id');
    console.log(job_id);
    
    if (job_id) {
    
        $("#selector-sample").val("?job_id="+job_id);
        $('#selector-sample').prop('disabled', function (index, value) {  
           
            return !value;
        })
    }
};