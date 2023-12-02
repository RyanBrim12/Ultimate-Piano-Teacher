var button = $("#led_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY JINGLE") {
        $.ajax({
            url: "/redled_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/redled_off",
            type: "post",
            success: function() {
                button.text("PLAY JINGLE");
            }
        })
    }
});
var button2 = $("#led_button2");
button2.click(function() {
    console.log(button2.text());
    if (button2.text() === "PLAY HAPPY") {
        $.ajax({
            url: "/yellowled_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button2.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/yellowled_off",
            type: "post",
            success: function() {
                button2.text("PLAY HAPPY");
            }
        })
    }
});

var button = $("#led_button3");
button.click(function() {
    console.log(button.text());
    if (button.text() === "PLAY HOT CROSS") {
        $.ajax({
            url: "/led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("PLAYING");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button.text("PLAY HOT CROSS");
            }
        })
    }
});

