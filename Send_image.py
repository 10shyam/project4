
def send_photo_telegram():
    import requests

    token = "5514395922:AAE31akNKsZ1GnlV10QPM9lmzo0M8WSTBRQ"
    chat_id = -1001703229995  # chat id
    file = "Total_M2M_Image.png"

    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    files = {}
    files["photo"] = open(file, "rb")
    requests.get(url, params={"chat_id": chat_id}, files=files)
