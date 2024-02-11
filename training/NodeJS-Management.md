# Node JS Development Steps
## Onjective: Develop React App using Node JS and Deploy using SWA( Azure Static Web Application)

### Ref: https://create-react-app.dev/docs/deployment/

### Install Node JS
- Download and Inastall Node JS: https://nodejs.org/en/download
- npm install -g serve
- npm install -g create-react-app

### Create Boilerplate Web App from default or specific template
- Change Directory: cd C:\Projects\WebApp
- npm init react-app ignaite-app
- Optional: npx create-react-app my-app --template typescript
- cd ignaite-app
- npm start
- Visit application at http://localhost:3000

### Test and Build application
- npm test
- npm run build
```
File sizes after gzip:
  46.65 kB  build\static\js\main.eaa8c1e9.js
  1.77 kB   build\static\js\592.a5c7f9b4.chunk.js
  513 B     build\static\css\main.f855e6bc.css
```

### Serve Web App on default port or specific port
- Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
- serve -s build
- serve -s build -l 4000
```
Serving!
Local:    http://localhost:4000
Network:  http://192.168.1.220:4000
```
