const { defineConfig } = require("cypress");

module.exports = defineConfig({
    e2e: {
        video: true,
        supportFile: false,
        baseUrl: 'http://172.17.0.3:9292',
        setupNodeEvents(on, config) {
            on('task', {
                downloadZipFile(url, filePath) {
                console.log(url, filePath)
      
                return null
              },
            })
        },
    },
    component: {
        supportFile: false
    }
});