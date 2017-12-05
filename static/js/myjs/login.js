/**
 * Created by d3qnew on 2017/11/20.
 */
$(document).ready(function () {

    $(":button").click(function () {
        $.post(
            '/checkuser',
            {
                username: $("#username").val(),
                password: $("#password").val()
            },
            function (data) {
                console.log(data);
            });

    });


});
