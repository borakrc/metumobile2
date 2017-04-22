#
# api.openweathermap.org/data/2.5/forecast/daily?lat=35.248&lon=33.024&cnt=2&APPID=14a4c3738b03e20a1f3afd0133710529
# https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20u='c' and woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22kapouti%2C%20cy%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys
class Weather:
    def __init__(self):
        pass

    def getDaily(self):
        import urllib, json
        url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20u='c' and woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22kapouti%2C%20cy%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        # resource = urllib.urlopen(url)
        # return str(resource.read().decode('utf-8'))
        response = urllib.urlopen(url).read()
        jsonEndpointData = json.loads(response)
        currentAndForecastWeather = {}
        currentAndForecastWeather['units'] = jsonEndpointData['query']['results']['channel']['units']
        currentAndForecastWeather['current'] = jsonEndpointData['query']['results']['channel']['item']['condition']
        currentAndForecastWeather['today'] = jsonEndpointData['query']['results']['channel']['item']['forecast'][0]
        currentAndForecastWeather['tomorrow'] = jsonEndpointData['query']['results']['channel']['item']['forecast'][1]

        currentAndForecastWeather['current']['imageUrl'] = self.getImageLink(currentAndForecastWeather['current']['code'])
        currentAndForecastWeather['today']['imageUrl'] = self.getImageLink(currentAndForecastWeather['today']['code'])
        currentAndForecastWeather['tomorrow']['imageUrl'] = self.getImageLink(currentAndForecastWeather['tomorrow']['code'])
        #
        # for dayForecast in currentAndForecastWeather['forecast']:
        #     dayForecast['imageUrl'] = self.getImageLink(dayForecast['code'])
            
        return currentAndForecastWeather

    def getImageLink(self, code):
        if int(code)==0: return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        if int(code)==1: return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        if int(code)==2: return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        if int(code)==3: return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        if int(code)==4: return 'http://l.yimg.com/a/i/us/we/52/0.gif'
        if int(code)==5: return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        if int(code)==6: return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        if int(code)==7: return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        if int(code)==8: return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        if int(code)==9: return 'http://l.yimg.com/a/i/us/we/52/9.gif'
        if int(code)==10: return 'http://l.yimg.com/a/i/us/we/52/12.gif'
        if int(code)==11: return 'http://l.yimg.com/a/i/us/we/52/12.gif'
        if int(code)==12: return 'http://l.yimg.com/a/i/us/we/52/12.gif'
        if int(code)==13: return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        if int(code)==14: return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        if int(code)==15: return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        if int(code)==16: return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        if int(code)==17: return 'http://l.yimg.com/a/i/us/we/52/17.gif'
        if int(code)==18: return 'http://l.yimg.com/a/i/us/we/52/17.gif'
        if int(code)==19: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==20: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==21: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==22: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==23: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==24: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==25: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==26: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==27: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==28: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==29: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==30: return 'http://l.yimg.com/a/i/us/we/52/26.gif'
        if int(code)==31: return 'http://l.yimg.com/a/i/us/we/52/31.gif'
        if int(code)==32: return 'http://l.yimg.com/a/i/us/we/52/32.gif'
        if int(code)==33: return 'http://l.yimg.com/a/i/us/we/52/31.gif'
        if int(code)==34: return 'http://l.yimg.com/a/i/us/we/52/32.gif'
        if int(code)==35: return 'http://l.yimg.com/a/i/us/we/52/35.gif'
        if int(code)==36: return 'http://l.yimg.com/a/i/us/we/52/32.gif'
        if int(code)==37: return 'http://l.yimg.com/a/i/us/we/52/37.gif'
        if int(code)==38: return 'http://l.yimg.com/a/i/us/we/52/37.gif'
        if int(code)==39: return 'http://l.yimg.com/a/i/us/we/52/39.gif'
        if int(code)==40: return 'http://l.yimg.com/a/i/us/we/52/39.gif'
        if int(code)==41: return 'http://l.yimg.com/a/i/us/we/52/41.gif'
        if int(code)==42: return 'http://l.yimg.com/a/i/us/we/52/41.gif'
        if int(code)==43: return 'http://l.yimg.com/a/i/us/we/52/41.gif'
        if int(code)==44: return 'http://l.yimg.com/a/i/us/we/52/44.gif'
        if int(code)==45: return 'http://l.yimg.com/a/i/us/we/52/45.gif'
        if int(code)==46: return 'http://l.yimg.com/a/i/us/we/52/14.gif'
        if int(code)==47: return 'http://l.yimg.com/a/i/us/we/52/45.gif'
        return 'http://l.yimg.com/a/i/us/we/52/3200.gif'
