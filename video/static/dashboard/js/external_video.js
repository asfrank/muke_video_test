
var videoEreaStatus = false;
var videoEditErea = $('#video-edit-area');

$('#open-add-video-btn').click(function () {
    if (!videoEreaStatus) {
        videoEditErea.show();
        videoEreaStatus = true;
    } else {
        videoEditErea.hide();
        videoEreaStatus = false;
    }
});