import webbrowser

url = "https://api.ltp-cloud.com/analysis/?api_key="
api_key = "4240U6S4s4kYFxXFncnDPfYHVdTGTwrEcPti8GEf"
text = "我是中国人。"
pattern = "dp"
textFormat = "plain"

url = url + api_key + "&text=" + text + "&pattern=" + pattern + "&format=" + textFormat

print("Fetching: " + url)

webbrowser.open(url)