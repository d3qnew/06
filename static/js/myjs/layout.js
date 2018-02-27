/**
 * Created by d3qnew on 2017/11/20.
 */









var bling = function () {

}

var toplink = $("#toplink");
//console.log(toplink.get(0).getBoundingClientRect().top);




$(document).ready(function () {

    var newtime = 0;
    var oldtime = 0;
    var t = null;


    function timedCount(st, sp, z) {
        if (sp < 104) {
            $("#topnavbar").show();
        }

        var stoptt = function () {
            clearTimeout(t);
        }
        if (st === sp) {
            //console.log("this is stop and zt:"+z);
            //console.log(sp);
            if (sp >= 105) {
                if (z === 'u') {
                    $("#topnavbar").slideDown();
                    ;
                } else {
                    if (z === 'd') {
                        $("#topnavbar").hide();
                    }
                }
            } else {
                $("#topnavbar").show();
            }


            stoptt();
        } else {
            t = setTimeout(function () {
                timedCount(oldtime, newtime, z)
            }, 100);
        }
    }


    $(window).scroll(function (e) {
        if (t != null) {
            clearTimeout(t);
        }
        newtime = $(this).scrollTop();
        var tmp = '';
        if (oldtime <= newtime) {
            tmp = 'd';
        }
        else {
            if (oldtime > newtime) {
                tmp = 'u';
            }
        }
        //console.log(tmp);
        timedCount(oldtime, newtime, tmp);
        oldtime = newtime;

        //console.log(zhuangtai);
        //setTimeout(function(){t=p;},5000);
    });


    //cebianlan

    $(".cebianlan a").hover(function () {
        if (typeof($(this).attr("id")) != 'undefined') {
            var s = eval('$(".cebianlan-' + $(this).attr("id") + '")');
            s.show();
        }

    }, function () {
        if (typeof($(this).attr("id")) != "undefined") {
            var s = eval('$(".cebianlan-' + $(this).attr("id") + '")');
            s.hide();
        }
    });

    $("#cebianlan1").hover(function () {
        $(this).find('img').attr("src","../static/img/service.png");

    },function () {
        $(this).find('img').attr("src","../static/img/service.gif");
    });


});





