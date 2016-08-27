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


// Newsletter form
$( ".newsletter-form" ).submit(function( event ) {
    // Stop form from submitting normally
    event.preventDefault();

    var form = this;
    var alerts = $(form).find(".newsletter-alerts")

    $.ajax({
        type: "POST",
        url: newsletter_form_url,
        data: $(form).serialize(),
        success: function(data){
            $(alerts).children().remove();
            var message = "Email byl úspěšně přidán.";
            var message_type = "success";
            if ('success_message' in data) {
                message = data.success_message
            }
            if ('email' in data) {  
                var message = data.email;
                var message_type = "warning";
            } 
            $(alerts).append('<div class="alert alert-' + message_type + '" role="alert" id="flash_alert">' + message + '</div>');
            $(form).find('input#id_email').val('');
            setTimeout(function() {$(alerts).children().fadeOut(2000)}, 4000);
        },
        error: function(data, textStatus, jqXHR) {
            $(alerts).children().remove(); 
            $(alerts).append('<div class="alert alert-warning" role="alert" id="flash_alert">' + data.responseJSON.email[0] + '</div>');
            setTimeout(function() {$(alerts).children().fadeOut(2000)}, 4000);
        },
        dataType: "json"
    });
});
