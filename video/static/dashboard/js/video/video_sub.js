var inputNumber = $('#number');
var inputUrl = $('#url');
var videoSubInputId= $('#videosub-input-id');

$('.update-btn').click(function () {
    var videoSubId = $(this).attr("data-id");
    var videoSubNumber = parseInt($(this).attr("data-number"));
    var videoSubUrl = $(this).attr("data-url");

    inputNumber.val(videoSubNumber);
    inputUrl.val(videoSubUrl);
    videoSubInputId.val(videoSubId);
});