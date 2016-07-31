/*!
 * Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});



//////////////////////////// CUSTOM ////////////////////////////////////

$(function() {

    $('.btn-quantity').click(function (){
        var operation = $(this).data('op');
        var input = $(this).parent().find('input');
        var val = parseInt($(input).val());
        if (operation == 'add') {
            $(input).val(val + 1);
        } else if (operation == 'sub' && val > 1) {
            $(input).val(val - 1);
        }
    });
    
});


//$('#shipping-info input').removeAttr('required');
// checkout billing info checkbox
$('#id_order-shipping_same_as_billing').change(function () {
    var val = this.checked;
    if (val) {
        $('#shipping-info').hide();
        $('#shipping-info input').removeAttr('required');
    } else {
        $('#shipping-info').show();
        $('#shipping-info input').attr('required', 'required');
    }
});


