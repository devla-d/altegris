'use strict';

(function($) {

    $(document).ready(function() {
        /* ----------------------------------------------------------- */
        /*  BOOTSTRAP CAROUSEL
       

        $("#heroslider").carousel({
            pause: true,
            interval: 100000,
        });
        console.log("Heello")
         /* ----------------------------------------------------------- */


        /* ----------------------------------------------------------- */
        /* Header Scroll
        /* ----------------------------------------------------------- */
        $(window).scroll(function() {
            if ($(this).scrollTop() > 100) {
                $('.inner-header').addClass("scroll"), 1000;
                $('#topbar nav').addClass("scroll"), 1000;
            } else {
                $('.inner-header').removeClass("scroll"), 1000;
                $('#topbar nav').removeClass("scroll"), 1000;
            }
        });

        /* ----------------------------------------------------------- */
        /* Set  Backgroud Image
        /* ----------------------------------------------------------- */
        $('.set-bg').each(function() {
            var bg = $(this).data('bg');
            $(this).css('background-image', 'url(' + bg + ')');

        });
        /* ----------------------------------------------------------- */
        /* Testimony Caroussel
        /* ----------------------------------------------------------- */
        $(".owl-carousel1").owlCarousel({
            autoplay: true,
            autoplayTimeout: 3000,
            autoplayHoverPause: false,
            loop: true,
            center: true,
            margin: 0,
            responsiveClass: true,
            nav: false,
            responsive: {
                0: {
                    items: 1,
                    nav: false
                },
                680: {
                    items: 2,
                    nav: false,
                    loop: false
                },
                1000: {
                    items: 3,
                    nav: true
                }
            }
        });


        /*
	    Wow
	*/
        new WOW().init();





        /* ----------------------------------------------------------- */
        /* Dashboard sidebar
        /* ----------------------------------------------------------- */
        var is_toggled = false
        $('.hamburger').on('click', function() {
            if (is_toggled === false) {
                $('.sidebar, .hamburger').addClass('active');
                is_toggled = true
            } else {
                $('.sidebar, .hamburger').removeClass('active');
                is_toggled = false
            }

        })


        $('.sidebar').mCustomScrollbar({
            theme: "minimal-dark"
        });






    });



})(jQuery);