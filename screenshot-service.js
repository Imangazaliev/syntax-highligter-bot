const express = require('express')
const expressWinston = require('express-winston')
const hljs = require('highlight.js')
const { nanoid } = require('nanoid')
const nunjucks = require('nunjucks')
const puppeteer = require('puppeteer')
const winston = require('winston')
const serveStatic = require('serve-static')

const { addLoggersToPage } = require('./screenshot-service/utils')

require('express-async-errors')

const DEBUG = true
const PORT = 8080
const HOST_URL = `http://127.0.0.1:${ PORT }`
const ROOT_PATH = __dirname
const SCREENSHOTS_DIR = ROOT_PATH + '/screenshots'
const LOG_FILE = ROOT_PATH + '/logs/screenshot-service.log'
const HL_THEME = 'github'

const app = express()

app.use(express.json())
app.set('view engine', 'html')
app.use(serveStatic(ROOT_PATH + '/assets', {
    immutable: true,
    maxAge: 5 * 60 * 1000,
}))

nunjucks.configure('views', { autoescape: true })

let browser

puppeteer
    .launch({
        args: [
            // disable CORS security to load assets from local server
            '--disable-web-security',
        ],
        headless: true,
    })
    .then(instance => {
        browser = instance

        console.log('Browser launched!')
    })

app.post('/generate-image', async (req, res) => {
    console.time('Generate image')

    const screenshotPath = SCREENSHOTS_DIR + `/${ nanoid() }.png`

    // generate HTML
    const { code } = req.body
    const highlightedCodeHtml = hljs.highlightAuto(code).value
    const html = nunjucks.render('template.html', {
        code: highlightedCodeHtml,
        cssUrl: HOST_URL + '/css/styles.css',
        hljsCssUrl: HOST_URL + `/hljs-styles/${ HL_THEME }.css`,
    })

    // generate screenshot
    const page = await browser.newPage()

    if (DEBUG) {
        addLoggersToPage(page)
    }

    await page.setContent(html)
    await page.screenshot({ path: screenshotPath })
    await page.close()

    console.timeEnd('Generate image')

    res.json({
        path: screenshotPath,
    })
})

app.use((req, res, next) => {
    res.status(404).json({
        message: 'Page not found.',
    })
})

app.use(expressWinston.logger({
    transports: [
        new winston.transports.File({
            filename: LOG_FILE,
            level: 'error',
        }),
        new winston.transports.Console(),
    ],
    meta: false,
    msg: "HTTP {{res.statusCode}} {{req.method}} {{res.responseTime}}ms {{req.url}}",
    expressFormat: true,
    colorize: false,
}))

app.listen(PORT, () => {
    console.log(`Listening port ${ PORT }...`)
})
