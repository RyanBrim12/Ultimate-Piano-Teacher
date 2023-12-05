var jingleBellsButton = $("#jingle_bells_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY JINGLE") {
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
                button.text("PLAY JINGLE");
            }
        })
    }
});
var happyBirthdayButton = $("#happy_birthday_button");
happyBirthdayButton.click(function() {
    console.log(happyBirthdayButton.text());
    if (happyBirthdayButton.text() === "PLAY HAPPY") {
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
                happyBirthdayButton.text("PLAY HAPPY");
            }
        })
    }
});

var hotCrossedBunsButton = $("#hot_crossed_buns_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY HOT CROSS") {
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
                button.text("PLAY HOT CROSS");
            }
        })
    }
});

