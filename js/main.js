/*
 * Copyright Aneesh Dogra 2013 <lionaneesh-at-gmail>
 */

$(function () {
    'use strict';

    function shuffle(o){ //v1.0
        for(var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
        return o;
    };

    $.getJSON('user_photos.json', function (data) {
        var gallery = $('#gallery');
        shuffle(data);
        for (var id in data) {
            var name = data[id][0]
            var url  = data[id][1];

            var a = $('<a/>')
                      .prop('href', "http://facebook.com/" + id)
                      .prop('alt', name)
                      .append($('<img>').prop('src', url))
                      .appendTo(gallery);
        }
    });
});
