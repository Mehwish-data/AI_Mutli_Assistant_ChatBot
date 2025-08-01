{
  "version": 2,
  "builds": [
    {
      "src": "vercel_wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "50mb",
        "runtime": "python3.11"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/api/(.*)",
      "dest": "vercel_wsgi.py"
    },
    {
      "src": "/(.*)",
      "dest": "vercel_wsgi.py"
    }
  ]
}
