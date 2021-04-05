let data = {
    categories: JSON.parse(document.getElementById('categoriesData').textContent),
    all_classys: JSON.parse(document.getElementById('classysData').textContent),
    lang: JSON.parse(document.getElementById('lang').textContent),
    projectID: 812923448506,
    clHeadRu: `<h4>Ищете работу? Хотите познакомиться? Хотите снять квартиру? Просмотрите наши объявления.
                    Ищете сотрудников? Хотите сдать квартиру в рент? Разместите свое объявление.</h4>
                <details>
                    <summary>Подать объявление</summary>
                    <h3>Правила подачи объявлений</h3>
                    <h4>Объявления можно подавать и оплачивать любым из следующих способов:</h4>
                    <ol>
                        <li><strong>Купон: </strong>
                            Заполните купон из газеты, вложите в конверт вместе с чеком или money order на имя Ethnic Media
                            и отправьте почтой по адресу: Ethnic Media, 25 Telser, P.O. Box 261, Lake Zurich, IL 60047
                            Отправьте объявление текстовым сообщением на номер 312-999-0609, в тексте укажите количество
                            выходов (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции
                            перезвонит Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li><strong>СМС: </strong>
                            Отправьте объявление текстовым сообщением на номер 312-999-0609, в тексте укажите количество 
                            выходов (сколько недель публиковать объявление) и контактный телефон. 
                            Сотрудник редакции перезвонит вам в течение ближайшего рабочего дня и примет оплату.         
                        </li>
                        <li><strong>Электронная почта: </strong>
                            Отправьте объявление по ЭЛЕКТРОННОЙ ПОЧТЕ на info@ethnicmedia.us, укажите количество выходов
                            (сколько недель публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит
                            Вам в течение ближайшего рабочего дня и примет оплату.
                        </li>
                        <li><strong>Факс: </strong>
                            Отправьте текст объявления по факсу 866-710-0220, укажите количество выходов (сколько недель
                            публиковать объявление) и Ваш контактный телефон. Сотрудник редакции перезвонит Вам в течение
                            ближайшего рабочего дня и примет оплату.
                        </li>
                    </ol>
                    <h4>Общие правила для раздела “Объявления”</h4>
                    <ul>
                        <li>Стоимость объявления в одном номере газеты: 50¢ за слово.</li>
                        <li>Номер телефона считается как за одно слово.</li>
                        <li>Слова, выделенные <strong>жирными</strong> или ЗАГЛАВНЫМИ буквами: 60¢ за слово.</li>
                        <li>Если вы хотите поместить свое объявление в нескольких номерах, то сумму умножьте на количество
                            публикаций.
                        </li>
                        <li>Фотография в объявлении: $5.</li>
                        <li>Объявление в рамке: $5 за модуль (1”х1,5”)</li>
                    </ul>
                    <h4>Поздравление с праздником (день рождения, юбилей, свадьба) в рамке (текст и фотография) - 
                        от $10, в зависимости от размера объявления. Некрологи, соболезнования (текст и фотография),
                        публикуются БЕСПЛАТНО</h4>
                </details>`,
    clHeadEn: `<h4>Looking for a job? Would you like to meet me? Do you want to rent an apartment? View our ads.
                   Looking for employees? Do you want to rent an apartment? Place your ad.</h4>
                <details>
                    <summary>How do I place an ad in the 7 Days newspaper?</summary>
                    <h3>Ads can be submitted and paid for in one of the following ways:</h3>
                    <h4>Объявления можно подавать и оплачивать любым из следующих способов:</h4>
                    <ol>
                        <li><strong>Coupon: </strong>
                            Fill out a coupon from the 7 Days newspaper, put it in an envelope along with a check or a 
                            money order in favor of Ethnic Media and mail it to - Ethnic Media, 25 Telser, 
                            P.O. Box 261, Lake Zurich, IL 60047
                        </li>
                        <li><strong>Email: </strong>
                            Email the text of your ad to info@ethnicmedia.us, specify the number of issues 
                            (how many weeks to publish your ad) and your contact phone number. One of out 
                            representatives will call you back within the next business day and accept payment.         
                        </li>
                        <li><strong>Text message: </strong>
                            Send the text of your ad as a text message to 312-999-0609, specify the number of issues 
                            (how many weeks to publish your ad) and your contact phone number. One of out 
                            representatives will call you back within the next business day and accept payment.
                        </li>
                        <li><strong>Fax: </strong>
                            Fax the text of your ad to 866-710-0220, specify the number of issues (how many weeks to 
                            publish your ad) and your contact phone number. One of out representatives will call you 
                            back within the next business day and accept payment.
                        </li>
                    </ol>
                    <h4>Rules and rates for private messages publication in the ‘Ads’ section</h4>
                    <ul>
                        <li>The price of an ad in 1 issue of the newspaper is 50¢ per 1 word.</li>
                        <li>Phone number counts as 1 word.</li>
                        <li>Words in <strong>bold</strong> or CAPITAL letters are 60¢ per 1 word.</li>
                        <li>If you want to place your ad in more than one issue, multiply the amount by the 
                            number of publications.
                        </li>
                        <li>Photo in ad: $5.</li>
                        <li>Framed ad: $5 per module (1 "x1.5")</li>
                    </ul>
                    <h4>Congratulations (birthday, anniversary, wedding) in a frame (text and photo) - from $10, 
                        depending on the size of the ad. Obituaries, condolences (text and photo) are 
                        published for FREE</h4>
                </details>`
}

const app = Vue.createApp({
    data() {
        const cats = []
        data.categories.forEach(cat => {
            data.all_classys.forEach(cl => {
                if (cat.id === cl.categories_id) {
                    if (cats.indexOf(cat) < 0) {
                        cats.push(cat)
                    }
                }
            })
        });
        return {
            all_classys: data.all_classys,
            categories: cats,
            classys: data.all_classys,
            lang: data.lang,
            clHead: data.clHeadRu,
            category_active: 0,
            categoryName: 'Все',
            isActive: false
        }
    },
    methods: {
        filterCat(id, name) {
            btns = document.getElementsByClassName('btn_cat')
            const clArr = []
            if (this.category_active === id) {
                this.classys = this.all_classys
                for (let i = 0; i < btns.length; i++) {
                    btns[i].classList.remove('active')
                }
                this.category_active = 0
                if (this.lang === 'ru') {
                    this.categoryName = 'Все'
                } else {
                    this.categoryName = 'All'
                }

            } else {
                this.all_classys.forEach(el => {
                    if (el['categories_id'] === id) {
                        clArr.push(el)
                    }
                })
                this.classys = clArr;
                for (let i = 0; i < btns.length; i++) {
                    btns[i].classList.remove('active')
                }
                document.getElementById('btn_cat' + id).className = "btn_cat active"
                this.category_active = id
                this.categoryName = name
            }
        },
        showCats() {
            if (document.getElementById('aside').className === 'active') {
                document.getElementById('aside').className = ''
            } else {
                document.getElementById('aside').className = 'active'
            }
        },
        changeLang() {
            if (this.lang === 'ru') {
                this.lang = 'en'
                this.clHead = data.clHeadEn
            } else {
                this.lang = 'ru'
                this.clHead = data.clHeadRu
            }
        }
    }
}).mount('#app');

