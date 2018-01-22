/**
 * Created by d3qnew on 2017/11/20.
 */


var ding = function (obj) {

    var obj = obj;
    var toDom = obj.get(0);
    var top = toDom.getBoundingClientRect().top //元素顶端到可见区域顶端的距离
    var se = document.documentElement.clientHeight //浏览器可见区域高度。
    if ((top) < se) {
        obj.stop().animate({marginTop: '0px'}, 100);
    } else {
        obj.css({"margin-top": "40px"});
    }
}


var bling = function () {

}



    var toplink = $("#toplink");
    console.log(toplink.get(0).getBoundingClientRect().top);

