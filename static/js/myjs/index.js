$(document).ready(function () {


    c2mov();//轮播开始

    var lic = 0;//起始banner
    //手动点击
    $(".carousel-control").on("click", function () {
        $(".carousel-control").css("display", "none");
        var valc = $(".c2valdiv:visible").index() + 1;
        var c2bg = "#c2bg";
        var c2val = "#c2val";
        var c2t = "#c2t";
        var f = '';
        if ($(this).attr("id") === "c2left") {
            f = 'l';
        } else {
            f = 'r';
        }

        if (f === "l") {
            lic = lic + 1;
        } else {
            lic = lic - 1;
        }

        if (lic > 4) {
            lic = 1
        }
        if (lic < 1) {
            lic = 4
        }
        $(".c2bg div").stop();
        $(".c2bg div").show();
        if (f === 'l') {
            $(".c2bg div").css("float", "left");
        } else {
            $(".c2bg div").css("float", "right");
        }
        for (i = 1; i <= 6; i++) {
            var c2 = c2bg + i;
            $(c2).stop();
            $(c2).fadeOut(200 * (i - 7) * -1);
            $(".c2val").children("div").hide();
        }
        $(c2val + lic).fadeIn(1300, function () {
            $(".carousel-control").css("display", "block");
        });
        $(c2t + lic).css("opacity", "0");

    });


//原来的页内js
    $(".i-2-bk :first").css({"padding-top": "16px"});

    $(window).on("scroll", function () {
        ding($(".ding:eq(0)"), 0, -30);
        ding($(".ding:eq(1)"), 0, -30);
        ding($(".ding:eq(2)"), 0, -30);
        ding($(".kuaisuliulan"), 0, -30);
    });

    $(".kuaisuliulan span").hover(function () {
        $(this).animate({
            opacity: '0.8'
        });
    }, function () {
        $(this).animate({
            opacity: '1'
        });
    });


    var i2run = setInterval(function () {


        $(".i-2-bk-i").each(function () {
            $(this).children("img:first").slideUp(function () {
                $(this).insertAfter($(this).nextAll().last());
            });
            $(this).next(".i-2-bk-w").children("div:first").slideUp(function () {
                $(this).insertAfter($(this).nextAll().last());
            });

        })


        $(".fangda").show();
        $(".i-2-bk-w div").show();

    }, 4000);


});

function c2mov() {
    var showtime = 30000;// 轮播间隔
    if ($(window).width() >= 650) {
        var lic = 2;
        var imgrun = setInterval(function () {
            //$(".c2t").css({"margin-top": $(".c2").height() * -0.9, "margin-left": $(".c2").width()});
            var valc = $(".c2valdiv:visible").index() + 1;
            var c2bg = "#c2bg";
            var c2val = "#c2val";
            var c2t = "#c2t";
            var cb = "#cb"
            $(".c2u li").css("color", "#ccc");
            $(cb + lic).css("color", "#349bd7");
            $(".c2bg div").show();
            if (1 < lic) {
                $(".c2bg div").css("float", "right");
            } else {
                $(".c2bg div").css("float", "left");
            }
            for (i = 1; i <= 6; i++) {
                var c2 = c2bg + i;
                $(c2).fadeOut(200 * (i - 7) * -1);
                $(".c2val").children("div").hide();
            }
            $(c2val + lic).fadeIn(
                1300,
                function () {
                    var lic1 = lic - 1;
                    if (lic1 == 0) lic1 = 4;
                    $(c2t + lic1).animate({marginLeft: ($(".c2").width() * 0.69) + "px", opacity: 0.4}, 600);
                    $(c2t + lic1).animate({opacity: 0.85}, 500);
                });
            $(c2t + lic).css("opacity", "0");
            lic++;
            if (lic > 4) lic = 1;
        }, showtime);
    } else {
        var lic = 2;
        var imgrun = setInterval(function () {
            var valc = $(".c2valdiv:visible").index() + 1;
            var c2bg = "#c2bg";
            var c2val = "#c2val";
            var c2t = "#c2t";
            var cb = "#cb";
            $(".c2val").children("div").hide();
            $(c2val + lic).fadeIn(
                100,
                function () {
                    var lic1 = lic - 1;
                    if (lic1 == 0) lic1 = 4;
                    $(c2t + lic1).animate({opacity: 0.85}, 500);
                });
            $(c2t + lic).css("opacity", "0");
            lic++;
            if (lic > 4) lic = 1;
        }, showtime);
    }
}



