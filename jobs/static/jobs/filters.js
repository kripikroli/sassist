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

var buildUrl = function buildUrl(sParam, sVal) {
    var sPageURL = window.location.search.substring(1),
        mURL = window.location.href.split('?')[0],
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        newUrlParams = ''
        newUrl = '';

    var isParamExist = getUrlParameter(sParam);
    if (isParamExist) {
        for (let i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');
            if (sParameterName[0] === sParam) {
                sParameterName[1] = sVal
                if (i == sURLVariables.length - 1) {
                    newUrlParams += sParameterName.join('=')
                }
                else {
                    newUrlParams += sParameterName.join('=') + '&'
                }
            }
            else {
                if (sParameterName[0] !== 'job_id') {
                    if (i == sURLVariables.length - 1) {
                        newUrlParams += sParameterName.join('=')
                    }
                    else {
                        newUrlParams += sParameterName.join('=') + '&'
                    }
                }
            }   
        }
    }
    else {
        newUrlParams += sParam + '=' + sVal + '&'
            for (let i = 0; i < sURLVariables.length; i++) {
                sParameterName = sURLVariables[i].split('=');

                if (sParameterName[0] !== 'job_id') {
                    if (i == sURLVariables.length - 1) {
                        newUrlParams += sParameterName.join('=')
                    }
                    else {
                        newUrlParams += sParameterName.join('=') + '&'
                    }
                }
            }
    }
    
    newUrl = mURL + '?' + newUrlParams

    return newUrl;
};

var returnConsole = function returnConsole(sValue) {
    console.log(sValue, '-------------------------');
};

window.onload = function(event) {
    //event.stopPropagation(true);
    // var job_id = getUrlParameter('job_id');
    // console.log(job_id);
    
    // if (job_id) {
    
    //     $("#selector-sample").val("?job_id="+job_id);
    //     $('#selector-sample').prop('disabled', function (index, value) {  
           
    //         return !value;
    //     })
    // }

    


};







$('#div_dd_date_posted_options button').on('click', function(){
    // $('#btn_span_date_posted').text($(this).text());
    try {

        if ($(this).text() == 'Last 24 hours') {
            window.location = buildUrl('fromage', '1')
        }

        if ($(this).text() == 'Last 3 days') {
            window.location = buildUrl('fromage', '3')
        }

        if ($(this).text() == 'Last 7 days') {
            window.location = buildUrl('fromage', '7')
        }

        if ($(this).text() == 'Last 14 days') {
            window.location = buildUrl('fromage', '14')
        }

        if ($(this).text() == 'Last day visited') {
            window.location = buildUrl('fromage', 'last')
        }

    } catch (error) {
        console.log('error', error)
    }
});

// $(document).ready(function() {
//     //$('#btn_span_date_posted').text($("#div_dd_date_posted_options button[id='default-option']").text());
// });