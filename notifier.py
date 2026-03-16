# Notification module for sending alerts when availability is found
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import (
    EMAIL_ENABLED,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECIPIENT,
    SMTP_SERVER,
    SMTP_PORT,
)


def format_email_body(results):
    import calendar
    from config import RESERVE_BASE_URL

    body = "🏕️ New Campground Availability Detected!\n\n"
    body += "=" * 60 + "\n\n"

    for result in results:
        month_name = calendar.month_name[result["month"]]
        campground_name = result["campground_name"]
        campground_id = result["campground_id"]

        body += f"{campground_name}: {month_name}\n"
        body += f"🔗 {RESERVE_BASE_URL}/{campground_id}\n\n"

        for site_id, site_data in result["sites_info"].items():
            site_name = site_data["site_name"]
            dates = site_data["available_dates"]

            formatted_dates = []
            for date in dates:
                date_part = date.split("T")[0]
                year, month, day = date_part.split("-")
                formatted_dates.append(f"{int(month)}/{int(day)}")

            body += f"* {site_name}\n"
            body += f"Dates: {', '.join(formatted_dates)}\n\n"

        body += "-" * 60 + "\n\n"

    body += "Book quickly before they're gone!\n"

    return body


def send_email_notification(results):
    if not EMAIL_ENABLED:
        print("Email notifications disabled in config")
        return False

    if not EMAIL_SENDER or not EMAIL_PASSWORD or not EMAIL_RECIPIENT:
        print("Email credentials not configured in .env file")
        return False

    try:
        # create msg
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECIPIENT
        msg["Subject"] = "🏕️ New Campground Availability Alert!"
        # add body
        body = format_email_body(results)
        msg.attach(MIMEText(body, "plain"))
        # send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email notificaiton sent to {EMAIL_RECIPIENT}")
        return True
    except Exception as error:
        print(f"Failed to send email: {error}")
        return False
