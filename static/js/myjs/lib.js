/**
 * Created by d3qnew on 2017/12/24.
 */

    var formatdaste = function(str) {
        var t = str || '2017-1-12';
        var tarr = t.split("-");
        var tr = tarr[0]+'年'+tarr[1]+'月'+tarr[2]+'日';
        return tr;
    }
