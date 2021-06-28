
var oSpan = $(".content-a a");
    $(function(){
        //
        // $(".img").each(function (){
        //     console.log($(".big-img").css("background-image")+$(this).css("background-image"));
        //     if ($(".big-img").css("background-image") === $(this).css("background-image"))
        //     {
        //         alert("true");
        //     }
        //     else {
        //         alert("false");
        //     }
        // })

        $(".img").hover(function (){
            $(".big-img").css("background-image",$(this).css("background-image"));
        })
        for(var i = 0; i< oSpan.length;i++){
            var r = parseInt(Math.random() * 255);
            var g = parseInt(Math.random() * 255);
            var b = parseInt(Math.random() * 255);
            var size = parseInt(Math.random() * 26) + 12;
            oSpan[i].style.color = 'rgb('+ r + ',' + g + ','+ b  +  ')';

            oSpan[i].style.fontSize = size + 'px';
            console.log( oSpan[i])
        }
        $("#QQ").hover(function (){
            $(".QR-code").css("background-image","url('/static/data/upload/img/QR-QQ.png')")
            $(".QR-code").css("right","0")
        },function (){
            $(".QR-code").css("right","-300px")
        })
        $("#WeChat").hover(function (){
            $(".QR-code").css("background-image","url('/static/data/upload/img/weichat.jpg')")
            $(".QR-code").css("right","0")
        },function (){
            $(".QR-code").css("right","-300px")
        })
        $("#GitHub").hover(function (){
             $(".QR-code").css("background-image","url('/static/data/upload/img/GitHub.png')")
           $(".QR-code").css("right","0")
        },function (){
            $(".QR-code").css("right","-300px")
        })
    });