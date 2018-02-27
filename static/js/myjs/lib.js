/**
 * Created by d3qnew on 2017/12/24.
 */

var formatdate = function (str) {
    var t = str || '2017-1-12';
    var tarr = t.split("-");
    var tr = tarr[0] + '年' + tarr[1] + '月' + tarr[2] + '日';
    return tr;
}


var ding = function (obj, b, t) {

    var obj = obj;
    var b = b + 'px';
    var t = t + 'px';
    var toDom = obj.get(0);
    var top = toDom.getBoundingClientRect().top //元素顶端到可见区域顶端的距离
    var se = document.documentElement.clientHeight //浏览器可见区域高度。
    if ((top) < se) {
        obj.stop().animate({marginTop: t}, 100);
    } else {
        obj.css({"margin-top": b});
    }
}