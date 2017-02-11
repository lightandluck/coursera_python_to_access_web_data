//  require cheerio
const cheerio = require('cheerio')
const request = require('request')

const LINKPOS = 18
const REPS = 7
const URL = 'http://python-data.dr-chuck.net/known_by_Kinnon.html'

function crawllinks(url, linkpos, reps) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      const $ = cheerio.load(body)

      let index = linkpos - 1
      let tag = $('a').get(index)
      let new_url = tag.attribs.href
      let text = tag.children[0].data

      reps -= 1

      // return console.log because async nature of requests will not return a 
      // proper value to function call. Logs 'undefined'
      return reps > 0 ? crawllinks(new_url, linkpos, reps) : console.log(text)
    }
  })
}

crawllinks(URL, LINKPOS, REPS)