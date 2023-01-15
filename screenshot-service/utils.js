const addLoggersToPage = (page) => {
    page.on('console', message => {
        console.log(`${message.type().substr(0, 3).toUpperCase()} ${message.text()}`)
    })
    page.on('pageerror', ({ message }) => console.log(message))
    page.on('response', response => {
        console.log([
            response.status(),
            (response.timing().requestTime / 1000000).toFixed(3) + 'ms',
            response.url(),
            response.fromCache() ? '[cache]' : '',
        ].join(' '))
    })
    page.on('requestfailed', request => {
        console.log(`${request.failure().errorText} ${request.url()}`)
    })
}

module.exports = {
    addLoggersToPage,
}
