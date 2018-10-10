import urllib3

def download(url, user_agent='wswp', num_retries=2):
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    http = urllib3.PoolManager()
    try:
        request = http.request(url, headers=headers)
        html = request.data
    except urllib3.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600
                return download()
    return html;