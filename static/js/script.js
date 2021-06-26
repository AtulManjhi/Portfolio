$(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar').addClass("sticky");
        }else{
            $('.navbar').removeClass("sticky");
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
            $('.menu-btn .menu2').addClass("active");
            
        }else{
            $('.scroll-up-btn').removeClass("show");
            $('.menu2').removeClass("active");
        }
    });

    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0})
    });

    $('.menu-btn').click(function(){
        $('.navbar .menu').toggleClass("active");
        $('.bar1').toggleClass("switch");
        $('.bar2').toggleClass("switch");
        $('.bar3').toggleClass("switch");  
    });

    $('.row_element').hover(
        function(){ $(this).addClass('active') },
        function(){ $(this).removeClass('active') }
 )
});