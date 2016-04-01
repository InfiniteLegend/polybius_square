var start_coding = function() {
    var data = {
        "text": $("#text1").val(),
        "password": $("#password").val()
    };
    if($("#decode-radio").is(':checked')) {
        send_request("/api/decode", data);
    }
    else {
        send_request("/api/encode", data);
    }
};


var send_request = function(url, data) {
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function(response) {
            var text = JSON.parse(response).result;
            $("#text2").val(text);
        },
        error:  function(response) {

        }
    });
};
