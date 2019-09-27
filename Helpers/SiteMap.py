class SiteMap:
    siteMapString = """
<li>clickable: <a href=\"/academiccalendar/cacheversion/\">/academiccalendar/cacheversion/</a></li>
<li>clickable: <a href=\"/shuttleschedule/cacheversion/\">/shuttleschedule/cacheversion/</a></li>
<li>clickable: <a href=\"/shuttleschedule2/111/cacheversion/\">/shuttleschedule2/111/cacheversion/</a></li>
<li>clickable: <a href=\"/upcomingevents/cacheversion/\">/upcomingevents/cacheversion/</a></li>
<li>clickable: <a href=\"/upcomingevents/raw/\">/upcomingevents/raw/</a></li>
<li>clickable: <a href=\"/announcements/cacheversion/\">/announcements/cacheversion/</a></li>
<li>clickable: <a href=\"/cafeteriamenu/cacheversion/\">/cafeteriamenu/cacheversion/</a></li>
<li>clickable: <a href=\"/alacartemenu/cacheversion/\">/alacartemenu/cacheversion/</a></li>
<li>clickable: <a href=\"/phonebook/cacheversion/\">/phonebook/cacheversion/</a></li>
<li>clickable: <a href=\"/phonebook/raw/\">/phonebook/raw/</a></li>
<li>clickable: <a href=\"/booklets/cacheversion/\">/booklets/cacheversion/</a></li>
<li>clickable: <a href=\"/brochures/cacheversion/\">/brochures/cacheversion/</a></li>
<li>clickable: <a href=\"/shuttle/location/\">/shuttle/location/</a></li>
<li>clickable: <a href=\"/shuttle/location/multipleshuttles/\">/shuttle/location/multipleshuttles/</a></li>
<li>clickable: <a href=\"/ip/cacheversion/\">/ip/cacheversion/</a></li>
<li>clickable: <a href=\"/academiccalendarnew/\">/academiccalendarnew/</a></li>
<li>clickable: <a href=\"/academiccalendar/\">/academiccalendar/</a></li>
<li>clickable: <a href=\"/shuttleschedule/\">/shuttleschedule/</a></li>
<li>clickable: <a href=\"/shuttleschedule2/\">/shuttleschedule2/</a></li>
<li>clickable: <a href=\"/upcomingevents/\">/upcomingevents/</a></li>
<li>clickable: <a href=\"/cafeteriamenu/\">/cafeteriamenu/</a></li>
<li>clickable: <a href=\"/alacartemenu/\">/alacartemenu/</a></li>
<li>clickable: <a href=\"/phonebook/\">/phonebook/</a></li>
<li>clickable: <a href=\"/booklets/\">/booklets/</a></li>
<li>clickable: <a href=\"/brochures/\">/brochures/</a></li>
<li>clickable: <a href=\"/ip/\">/ip/</a></li>
<li>clickable: <a href=\"/\">/</a></li>
<li>clickable: <a href=\"/announcements/category/0\">/announcements/category</a></li>
<li>clickable: <a href=\"/cafeteria/rating/\">POST: /cafeteria/rating/</a></li>

"""



""""
def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route("/site-map/")
def site_map():
    links = []
    responseString = ""
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)
            responseString += "<li>clickable: <a href=\""+str(url)+"\">"+str(url)+"</a></li>"
    # links is now a list of url, endpoint tuples
    return responseString"""
