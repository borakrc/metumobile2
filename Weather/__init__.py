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

        for dayForecast in currentAndForecastWeather['forecast']:
            dayForecast['imageUrl'] = 'http://l.yimg.com/a/i/us/we/52/' + dayForecast['code'] + '.gif'
            
        return currentAndForecastWeather


        # mealDetails = jsonEndpointData
        # meal['tr_name'] = mealDetails['tr_name']


        # import urllib2, urllib, json
        # baseurl = "https://query.yahooapis.com/v1/public/yql?"
        # yql_query = "select wind from weather.forecast where woeid=2460286"
        # yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
        # result = urllib2.urlopen(yql_url).read()
        # data = json.loads(result)
        # print data['query']['results']
