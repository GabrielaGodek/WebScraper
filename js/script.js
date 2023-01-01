const eur_pln = document.querySelector('.statistic-page .title-radio input#eur_pln')
const usd_pln = document.querySelector('.statistic-page .title-radio input#usd_pln')
const eur_usd = document.querySelector('.statistic-page .title-radio input#eur_usd')

document.querySelector('main').style.height = document.querySelector('.statistic-page .charts .eur_pln img').scrollHeight + 'px'

document.querySelectorAll('.statistic-page .title-radio input').forEach(radio => {
    radio.addEventListener('click', () => {
        if (eur_pln.checked) {
            document.querySelector('.statistic-page .charts .eur_pln').style.maxHeight = document.querySelector('.statistic-page .charts .eur_pln').scrollHeight + 'px'
        } else {
            document.querySelector('.statistic-page .charts .eur_pln').style.maxHeight = '0'
        }

        if (usd_pln.checked) {
            document.querySelector('.statistic-page .charts .usd_pln').style.maxHeight = document.querySelector('.statistic-page .charts .usd_pln').scrollHeight + 'px'
        } else {
            document.querySelector('.statistic-page .charts .usd_pln').style.maxHeight = '0'
        }

        if (eur_usd.checked) {
            document.querySelector('.statistic-page .charts .eur_usd').style.maxHeight = document.querySelector('.statistic-page .charts .eur_usd').scrollHeight + 'px'
        } else {
            document.querySelector('.statistic-page .charts .eur_usd').style.maxHeight = '0'
        }
    })
})

