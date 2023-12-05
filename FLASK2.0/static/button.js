var jingleBellsButton = $("#jingle_bells_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY") {
        $.ajax({
            url: "/play_jingle_bells",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/stop_jingle_bells",
            type: "post",
            success: function() {
                button.text("PLAY");
            }
        })
    }
});
var happyBirthdayButton = $("#happy_birthday_button");
happyBirthdayButton.click(function() {
    console.log(happyBirthdayButton.text());
    if (happyBirthdayButton.text() === "PLAY") {
        $.ajax({
            url: "/play_happy_birthday",
            type: "post",
            success: function(response) {
                console.log(response);
                happyBirthdayButton.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/stop_happy_birthday",
            type: "post",
            success: function() {
                happyBirthdayButton.text("PLAY");
            }
        })
    }
});

var hotCrossedBunsButton = $("#hot_crossed_buns_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY") {
        $.ajax({
            url: "/play_hot_crossed_buns",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/stop_hot_crossed_buns",
            type: "post",
            success: function() {
                button.text("PLAY");
            }
        })
    }
});

