from plyer import notification
notification_title = "GREETINGS"
notification_message = "THANK YOU"
notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 10,
    toast = False
    )
