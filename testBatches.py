import requestsW

url="https://www.youtube.com/watch?v=ydUr87glh80"
args = []
args.append({"method": "GET", "url": "https://www.bing.com/search?q=bananas", "kwargs": {"headers": {"test": "1"}}})
args.append({"method": "GET", "url": "https://www.bing.com/search?q=bananas&first=11", "kwargs": {"headers": {"test": "1"}}})
r = requestsW.batch(args)

print(r[0].text)
print(r[1].text)
